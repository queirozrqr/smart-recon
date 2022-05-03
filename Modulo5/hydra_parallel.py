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
url = 'https://localhost:9200/'+target+'-portscan/_search'
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
list_ip = []
list_serv = []
dic_ip = {}
servicos = ['ftp','ssh','pop3','telnet','imap','mysql']

def consulta():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(x['_source']['server.ip'] not in list_ip):
			list_ip.append(x['_source']['server.ip'])
	for i in list_ip:
		list_serv = []
		for x in parse_scan['hits']['hits']:
			if(x['_source']['server.ip'] == i):
				if(x['_source']['server.port'] not in list_serv):
					list_serv.append(x['_source']['server.port'])	
					if(x['_source']['network.protocol'] in servicos):
						with open ('/docker/data/'+target+'/temp/hydra_parallel.log','a') as file:
            						file.write('python3 /docker/scripts/Modulo5_parse_hydra.py '+target+' '+i+' '+x['_source']['server.port']+' '+x['_source']['network.protocol']+'\n')

def parallel():
	print("[+] PROCESSANDO HYDRA \n")
	os.system('cat /docker/data/'+target+'/temp/hydra_parallel.log | parallel -u')
def main():
	os.system('rm -rf /docker/data/teste/temp/hydra_parallel.log')
	consulta()
	parallel() 
if __name__ == '__main__':
    main()
