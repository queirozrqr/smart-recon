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
url = 'https://localhost:9200/'+target+'-subdomain/_search'
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
list_ip = []

def consulta():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(str(x['_source']['server.ip']) not in list_ip):
			list_ip.append(str(x['_source']['server.ip']))
def parallel():
	os.system('rm -rf /docker/data/'+target+'/temp/nmap_parallel.log')
	for ip in list_ip:
		with open ('/docker/data/'+target+'/temp/nmap_parallel.log','a') as file:
			file.write('python3 /docker/scripts/Modulo5_parse_nmap.py '+target+' '+ip+'\n')
	print("[+] PROCESSANDO NMAP \n")
	os.system('cat /docker/data/'+target+'/temp/nmap_parallel.log | parallel -u')
def main():
	consulta()
	parallel()
if __name__ == '__main__':
    main()
