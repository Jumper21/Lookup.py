#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of Lookup tool.
    Copyright (C) 2016-2017 Jumper
    
    Lookup - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = 'Jumper'

from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Green(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintLookup(self, Lookup):
        """print IP Geolocation information to terminal"""
        self.PrintResult('\nTarget', Lookup.Query)
        self.PrintResult('IP', Lookup.IP)
        self.PrintResult('ASN', Lookup.ASN)
        self.PrintResult('City', Lookup.City)
        self.PrintResult('Country', Lookup.Country)
        self.PrintResult('Country Code', Lookup.CountryCode)
        self.PrintResult('ISP', Lookup.ISP)
        self.PrintResult('Latitude', str(Lookup.Latitude))
        self.PrintResult('Longtitude', str(Lookup.Longtitude))
        self.PrintResult('Organization', Lookup.Organization)
        self.PrintResult('Region Code', Lookup.Region)
        self.PrintResult('Region Name', Lookup.RegionName)
        self.PrintResult('Timezone', Lookup.Timezone)
        self.PrintResult('Zip Code', Lookup.Zip)
        self.PrintResult('Google Maps', Lookup.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
    