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
scanner = 'nikto'
dic_web = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-nikto'
saida = 'nikto-'+x+'.xml'
sistema = sys.argv[2]

def executa(sistema):
    result = subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data kali-tools:2.0 nikto -host '+sistema+' -output /data/'+saida+' || true', shell=True)

def parse():
    executa(sistema)
    tree = ET.parse('/docker/data/'+target+'/temp/'+saida)
    #tree = ET.parse('/docker/data/'+target+'/temp/nikto.xml')
    root = tree.getroot()
    for i in root.iter('scandetails'):
        dic_web['server.ip'] = i.attrib['targetip']
        dic_web['server.address'] = i.attrib['targethostname']
        dic_web['server.domain'] = i.attrib['targethostname']
        dic_web['server.port'] = i.attrib['targetport']
        dic_web['network.protocol'] = i.attrib['sitename'].split(':')[0]
        dic_web['service.name'] = i.attrib['sitename'].split(':')[0]
        dic_web['http.response.status_code'] = '200'
        dic_web['url.original'] = sistema
        for scan in i:
            if(scan.tag == 'item'):
                for item in scan:
                    if(item.tag == 'description'):
                        dic_web['vulnerability.description'] = item.text.replace('\n ','').replace(' \n','')
                        dic_web['vulnerability.name'] = item.text.replace('\n ','').replace(' \n','')
                        dic_web['vulnerability.severity'] = 'N/A'
                    if(item.tag == 'uri'):
                        dic_web['url.path'] = item.text.replace('\n ','').replace(' \n','')
                    if(item.tag == 'namelink'):
                        dic_web['url.full'] = item.text.replace('\n ','').replace(' \n','')
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

