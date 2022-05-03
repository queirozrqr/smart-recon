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
url = 'https://localhost:9200/'+target+'-webenum/_search'
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
dic_sistemas = {}

def consulta():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(str(x['_source']['url.original']) not in dic_sistemas):
			dic_sistemas[x['_source']['url.original']] = [x['_source']['server.domain'],x['_source']['server.ip']]
def parallel():
    os.system('rm -rf /docker/data/teste/temp/wayback_parallel.log')
    with open ('/docker/data/'+target+'/temp/wayback_parallel.log','a') as file:
        for sis in dic_sistemas:
            file.write('python3 /docker/scripts/Modulo5_parse_wayback.py '+target+' '+sis+' ' +dic_sistemas[sis][0]+' '+dic_sistemas[sis][1]+'\n')
    print("[+] PROCESSANDO wayback \n")
    os.system('cat /docker/data/'+target+'/temp/wayback_parallel.log | parallel -u')
def main():
   consulta()
   parallel() 
if __name__ == '__main__':
    main()
