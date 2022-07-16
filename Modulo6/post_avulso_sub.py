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
import telegram
from time import strftime
from pathlib import Path

target = sys.argv[1]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://$2:9200/'+target+'-subdomain-temp/_doc?refresh'
auth=('admin', $3)
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'monitora_subs'
dic_subdomain = {}

def parse():
    dic_subdomain['timestamp'] = hora
    dic_subdomain['server.address'] = 'teste7-smart-recon.businesscorp.com.br'
    dic_subdomain['server.domain'] = 'teste7-smart-recon.businesscorp.com.br'
    dic_subdomain['server.ip'] = '37.59.174.225'
    dic_subdomain['vulnerability.scanner.vendor'] = scanner
    dic_subdomain['server.ipblock'] = '37.59.174.224 - 37.59.174.239' 
    dic_subdomain['server.nameserver'] = 'ns1.businesscorp.com.br'  
    data = {
                 '@timestamp':hora,
                 'server.address':dic_subdomain['server.address'],
                 'server.domain':dic_subdomain['server.domain'],
                 'server.ip':dic_subdomain['server.ip'],
                 'server.ipblock':dic_subdomain['server.ipblock'],
                 'server.nameserver':dic_subdomain['server.nameserver'],
                 'vulnerability.scanner.vendor':dic_subdomain['vulnerability.scanner.vendor']
    }
    r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
    print (r.text)
    #print(data)

def main():
	parse()
if __name__== '__main__':
    main()
