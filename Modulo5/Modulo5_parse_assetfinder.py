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
domain = sys.argv[2]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://$2:9200/'+target+'-subdomain/_doc?refresh'
auth=('admin', $3)
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'assetfinder'
dic_subdomain = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-assetfinder'
saida = 'assetfinder-'+x+'.txt'

def rdap_ip(ip):
    try:
        consulta1 = subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+':/data kali-tools:2.0 /root/go/bin/rdap '+ip+' --json || true', shell=True) 
        json_rdap_ip = json.loads(consulta1)
        blocoip = json_rdap_ip['handle']
        return(blocoip)
    except:
        return('')

def rdap_domain(domain):
    nameserver = ''
    try:
        consulta2 = requests.get('https://rdap.registro.br/domain/'+domain)
        json_rdap = json.loads(consulta2.text)
        for ns in json_rdap['nameservers']:
            nameserver = nameserver+ns['ldhName']
        return(nameserver)
    except:
        return('')

def executa():
    subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data kali-tools:2.0 assetfinder -subs-only '+domain+' >> /docker/data/'+target+'/temp/'+saida+' || true', shell=True)

def parse():
    with open ('/docker/data/teste/temp/'+saida) as file:
        for line in file:
            dic_subdomain['timestamp'] = hora
            dic_subdomain['server.address'] = line.rstrip('\n')
            dic_subdomain['server.domain'] = line.rstrip('\n')
            try:
                dic_subdomain['server.ip'] = socket.gethostbyname(line.rstrip('\n'))
            except:
                dic_subdomain['server.ip'] = '0.0.0.0'
            dic_subdomain['vulnerability.scanner.vendor'] = scanner
            dic_subdomain['server.ipblock'] = rdap_ip(dic_subdomain['server.ip']) 
            dic_subdomain['server.nameserver'] = rdap_domain(dic_subdomain['server.domain'])
            data = {
                    '@timestamp':dic_subdomain['timestamp'],
                    'server.address':dic_subdomain['server.address'],
                    'server.domain':dic_subdomain['server.domain'],
                    'server.ip':dic_subdomain['server.ip'],
                    'server.ipblock':dic_subdomain['server.ipblock'],
                    'server.nameserver':dic_subdomain['server.nameserver'],
                    'vulnerability.scanner.vendor':dic_subdomain['vulnerability.scanner.vendor']
            }
            #r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
            #print (r.text)
            print(data)

def main():
    executa()
    parse()
    
if __name__== '__main__':
    main()
