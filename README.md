# Lookup
====
* A tool to retrieve IP location information
* Powered by [ip-api](http://ip-api.com/docs/)
* git clone https://github.com/Jumper21/Lookup.py.git

Requirements
=====
* Python 3.x
* termcolor
* colorama


Download/Installation
====
* git clone 
* pip3 install -r requirements.txt --user

if pip3 is missing:
* apt-get install python3-setuptools
* easy_install3 pip
* pip3 install -r requirements.txt


Features
====
* Retrieve IP or Domain location.
* Retrieve your own IP location.
* Retrieve location for IPs or Domains loaded from file. Each target in new line.
* Define your own custom User Agent string.
* Select random User-Agent strings from file. Each User Agent string in new line.
* Proxy support.
* Select random proxy from file. Each proxy URL in new line.
* Open IP location in Google Maps using the default browser.
* Export results to csv, xml and txt format.


location Information
====
* ASN
* City
* Country
* Country Code
* ISP
* Latitude
* Longtitude
* Organization
* Region Code
* Region Name
* Timezone
* Zip Code


Usage
====
```
$ ./lookup.py
usage: lookup.py [-h] [-m] [-t TARGET] [-T file] [-u User-Agent]
                        [-U file] [-g] [--noprint] [-v] [--nolog] [-x PROXY]
                        [-X file] [-e file] [-ec file] [-ex file]

Lookup.py V3

-[ Retrieve IP location information from ip-api.com
-[ Copyright (c) 2016-2017 Jumper
-[ ip-api.com service will automatically ban any IP addresses doing over 150 requests per minute.

optional arguments:
  -h, --help            show this help message and exit
  -m, --my-ip           Get location info for my IP address.
  -t TARGET, --target TARGET
                        IP Address or Domain to be analyzed.
  -T file, --tlist file
                        A list of IPs/Domains targets, each target in new line.
  -u User-Agent, --user-agent User-Agent
                        Set the User-Agent request header (default: lookup 2.0.3).
  -U file, --ulist file
                        A list of User-Agent strings, each string in new line.
  -g                    Open IP location in Google maps with default browser.
  --noprint             lookup will print IP location info to terminal. It is possible to tell lookup n
ot to print results to terminal with this option.
  -v, --verbose         Enable verbose output.
  --nolog               lookup will save a .log file. It is possible to tell lookup not to save those log
files with this option.
  -x PROXY, --proxy PROXY
                        Setup proxy server (example: http://127.0.0.1:8080)
  -X file, --xlist file
                        A list of proxies, each proxy url in new line.
  -e file, --txt file   Export results.
  -ec file, --csv file  Export results in CSV format.
  -ex file, --xml file  Export results in XML format.
```
  

Examples
====
**Retrieve your IP location**
* ./lookup.py -m

**Retrieve IP location**
* ./lookup.py -t 0.0.0.0

**Retrieve Domain location**
* ./lookup.py -t example.com

**Do not save .log files**
* ./lookup.py -t example.com --nolog

**Custom User Agent string** 
* ./lookup.py -t 0.0.0.0 -u "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"

**Using Proxy**
* ./lookup.py -t 0.0.0.0 -x http://127.0.0.1:8080

**Using random Proxy**
* ./lookup.py -t 0.0.0.0 -X /path/to/proxies/filename.txt

**Pick User-Agent string randomly**
* ./lookup.py -t 0.0.0.0 -U /path/to/user/agent/strings/filename.txt

**Retrieve IP location and open location in Google maps with default browser**
* ./lookup.py -t 0.0.0.0 -g

**Export results to CSV file**
* ./lookup.py -t 0.0.0.0 --csv /path/to/results.csv

**Export results to XML file**
* ./lookup.py -t 0.0.0.0 --xml /path/to/results.xml

**Export results to TXT file**
* ./lookup.py -t 0.0.0.0 -e /path/to/results.txt

**Retrieve IP location for many targets**
* ./lookup.py -T /path/to/targets/targets.txt

**Retrieve IP location for many targets and export results to xml**
* ./lookup.py -T /path/to/targets/targets.txt --xml /path/to/results.xml

**Do not print results to terminal**
* ./lookup.py -m -e /path/to/results.txt --noprint 


Credit
===
Made By Jumper

Discord: Jumper#7065
