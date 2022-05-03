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
scanner = 'wayback'
dic_web = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-wayback'
saida = 'wayback-'+x+'.xml'
url2 = sys.argv[2]
subdomain = sys.argv[3]
ip = sys.argv[4]

def executa(url2):
    result = subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data kali-tools:2.0 echo "'+url2+'" | waybackurls || true', shell=True)
    return(result.decode("utf-8")[:-1].split('\n'))
def parse():
	list_sistemas = executa(url2)
	for sistema in list_sistemas:
		if(sistema != '' or sistema != None):
			dic_web['network.protocol'] = sistema.split(':')[0]
			try:
				dic_web['server.port'] = sistema.split(':')[2].split('/')[0]
			except:
				if(dic_web['network.protocol'] == 'http'):
					dic_web['server.port'] = '80'
				else:
					dic_web['server.port'] = '443'
			path = len(sistema.split('/'))
			if(path == 3):
				dic_web['url.path'] = '/'
				dic_web['url.original'] = sistema
			else:
				i = 3
				dic_web['url.path'] = ''
				dic_web['url.original'] = dic_web['network.protocol']+'://'+sistema.split('/')[2]
				while i < path:
					dic_web['url.path'] = dic_web['url.path']+'/'+sistema.split('/')[i]
					i += 1

			data = {
			'@timestamp': hora,
			'server.address': subdomain,
			'server.domain': subdomain,
			'server.ip': ip,
			'server.port': dic_web['server.port'],
			'network.protocol': dic_web['network.protocol'],
			'url.path': dic_web['url.path'],
			'http.response.status_code': '200',
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

