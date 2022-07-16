#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import datetime
import socket
import requests
import subprocess
import os
import uuid
import shutil
import json
import time
from time import strftime
from pathlib import Path

target = sys.argv[1]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://$2:9200/'+target+'-webvuln/_doc?refresh'
auth=('admin', $3)
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'webscanner'
dic_web = {}
x = str(uuid.uuid1()).split('-')[0]

def parse():
    dic_web['server.ip'] = '37.59.174.225' 
    dic_web['server.address'] = 'businesscorp.com.br'
    dic_web['server.domain'] = 'businesscorp.com.br'
    dic_web['server.port'] = '80'
    dic_web['network.protocol'] = 'http'
    dic_web['service.name'] = 'http'
    dic_web['http.response.status_code'] = '200'
    dic_web['url.original'] = 'http://businesscorp.com.br'
    dic_web['url.full'] = 'http://businesscorp.com.br'
    dic_web['vulnerability.description'] = 'Desc Vulnerabilidade 01'
    dic_web['vulnerability.name'] = 'Vulnerabilidade 01'
    dic_web['vulnerability.severity'] = 'High'
    dic_web['url.path'] = '/'
    data = {
	'@timestamp':hora,
	'server.address':dic_web['server.address'],
	'server.domain':dic_web['server.domain'],
	'server.ip':dic_web['server.ip'],
	'server.port':dic_web['server.port'],
	'network.protocol':dic_web['network.protocol'],
	'url.path':dic_web['url.path'],
	'http.response.status_code':dic_web['http.response.status_code'],
	'vulnerability.description':dic_web['vulnerability.description'],
	'vulnerability.name':dic_web['vulnerability.name'],
	'vulnerability.severity':dic_web['vulnerability.severity'],
	'url.original':dic_web['url.original'],
	'url.full':dic_web['url.full'],
	'vulnerability.scanner.vendor':scanner
    }
    #print(data)
    r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
    print (r.text)
def main():
    parse()
    
if __name__== '__main__':
    main()

