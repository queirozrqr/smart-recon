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
url = 'https://localhost:9200/'+target+'-webenum/_doc?refresh'
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'gobuster'
dic_web = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-gobuster'
saida = 'gobuster-'+x+'.xml'
subdomain = sys.argv[2]
ip = sys.argv[3]
sistema = sys.argv[4]

def executa(sistema):
    result = subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/scripts/:/scripts kali-tools:2.0 gobuster dir -u "'+sistema+'" -w /scripts/webdir.txt -q  || true', shell=True)
    return(result.decode("utf-8").rstrip('\n').replace(' ','').split('\n'))

def parse():
	list_uri = executa(sistema)
	for uri in list_uri:
		dic_web['server.address'] = subdomain
		dic_web['server.domain'] = subdomain
		dic_web['server.ip'] = ip 
		dic_web['network.protocol'] = sys.argv[5]
		dic_web['url.path'] = uri.replace('\r','').split('(')[0]
		dic_web['http.response.status_code'] = uri.split(':')[1].split(')')[0]
		dic_web['url.original'] = sistema
		dic_web['server.port'] = sys.argv[6]
		dic_web['url.full'] = sistema+dic_web['url.path']
		data = {
			'@timestamp': hora,
			'server.address': subdomain,
			'server.domain': subdomain,
			'server.ip': ip,
			'server.port': dic_web['server.port'],
			'network.protocol': dic_web['network.protocol'],
			'url.path': dic_web['url.path'],
			'http.response.status_code': dic_web['http.response.status_code'],
			'url.original': dic_web['url.original'],
			'url.full': dic_web['url.original']+dic_web['url.path'],
			'vulnerability.scanner.vendor': scanner
		}	
		#print(data)
		r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
		print (r.text)

def main():
    parse()
    
if __name__== '__main__':
    main()

