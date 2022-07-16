#!/usr/bin/env python3

import sys
import socket
import string
import sys
import datetime
import requests
import subprocess
import os
import shutil
import uuid
import json
import time
from time import strftime
from pathlib import Path

target = sys.argv[1]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://$2:9200/'+target+'-subdomain/_search'
auth=('admin', $3)
dic_ip = {}

def consulta_subdomain():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(str(x['_source']['server.domain']) not in dic_ip and str(x['_source']['server.ip'] != '0.0.0.0')):
			dic_ip[(str(x['_source']['server.domain']))] = str(x['_source']['server.ip'])
def parallel():
    os.system('rm -rf /docker/data/teste/temp/httpx_parallel.log')
    with open ('/docker/data/'+target+'/temp/httpx_parallel.log','a') as file:
        for sub in dic_ip:
            file.write('python3 /docker/scripts/Modulo5_parse_httpx.py '+target+' '+sub+' ' +dic_ip[sub]+'\n')
    print("[+] PROCESSANDO HTTPX \n")
    os.system('cat /docker/data/'+target+'/temp/httpx_parallel.log | parallel -u')
def main():
   consulta_subdomain()
   parallel() 
if __name__ == '__main__':
    main()
