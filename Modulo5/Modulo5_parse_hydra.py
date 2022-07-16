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
url = 'https://$2:9200/'+target+'-infravuln/_doc?refresh'
auth=('admin', $3)
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'hydra'
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-hydra'
saida = 'hydra-'+x+'.json'
ip = sys.argv[2]
dic_infra = {}
porta = sys.argv[3]
servico = sys.argv[4]
scanner = 'hydra'

def executa(ip,porta,servico):
    subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data -v /docker/scripts:/scripts kali-tools:2.0 hydra -I -L /scripts/users.txt -P /scripts/passwords.txt -e nsr -o /data/'+saida+' -b json -t 1 '+ip+' '+servico+' -s '+porta+' || true', shell=True)

def parse():
    executa(ip,porta,servico)
    with open('/docker/data/'+target+'/temp/'+saida) as jsonfile:
        jsondata = json.load(jsonfile)
        for i in jsondata['results']:
            dic_infra['server.address'] = i['host']
            dic_infra['server.ip'] = ip
            dic_infra['server.port'] = i['port']
            dic_infra['network.protocol'] = i['service']
            dic_infra['service.name'] = i['service']
            dic_infra['vulnerability.description'] = 'Broken username/password '+i['login']+':'+i['password']
            dic_infra['vulnerability.name'] = 'Broken username/password'
            dic_infra['vulnerability.severity'] = 'High'
            data = {
            '@timestamp':hora,
            'server.address':dic_infra['server.address'],
            'server.ip':dic_infra['server.ip'],
            'server.port':dic_infra['server.port'],
            'network.protocol':dic_infra['network.protocol'],
            'service.name' : 'N/A',
            'vulnerability.description':dic_infra['vulnerability.description'],
            'vulnerability.name':dic_infra['vulnerability.name'],
            'vulnerability.severity':dic_infra['vulnerability.severity'],
            'vulnerability.scanner.vendor':scanner
            }
            #print(data)
            r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
            print (r.text)
def main():
    parse()
    
if __name__== '__main__':
    main()
