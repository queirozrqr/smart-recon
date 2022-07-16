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
url = 'https://$2:9200/'+target+'-webenum/_search'
auth=('admin', $3)
list_sistemas = []

def consulta():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(str(x['_source']['url.original']) not in list_sistemas):
			list_sistemas.append(x['_source']['url.original'])
def parallel():
    os.system('rm -rf /docker/data/teste/temp/nikto_parallel.log')
    with open ('/docker/data/'+target+'/temp/nikto_parallel.log','a') as file:
        for sis in list_sistemas:
            file.write('python3 /docker/scripts/Modulo5_parse_nikto.py '+target+' '+sis+'\n')
    print("[+] PROCESSANDO NIKTO \n")
    os.system('cat /docker/data/'+target+'/temp/nikto_parallel.log | parallel -u')
def main():
   consulta()
   parallel() 
if __name__ == '__main__':
    main()
