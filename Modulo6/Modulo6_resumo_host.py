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
sistema = sys.argv[2]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
lista_ips = []
lista_index = ['subdomain','portscan','webenum','webvuln','infravuln']
json_parse = ''
dic_ip = {}
list_vulns = []

def consulta_bases(index):
	data = {"size":10000}
	url = 'https://localhost:9200/'+target+'-'+index+'/_search'
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	return(parse_scan)

def consulta_diretorios(sistema):
	with open ('/docker/data/'+target+'/vulns.txt','a') as file:
		file.write('\n\n[+]DIRETORIOS\n\n')

	list_sis = []
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			try:
				if(x['_source']['url.original'] == sistema):
					if(x['_source']['url.full'] not in list_sis and x['_source']['vulnerability.scanner.vendor'] == 'gobuster'):
					#if(x['_source']['url.full'] not in list_sis):
						list_sis.append(x['_source']['url.full'])
						with open ('/docker/data/'+target+'/vulns.txt','a') as file:
							file.write(x['_source']['url.full']+'\n')
			except:
				pass

def consulta_ip(ip):
	with open ('/docker/data/'+target+'/vulns.txt','a') as file:
		file.write('\n\n[+]PORTAS\n\n')
	dic_ip[ip] = []
	for index in lista_index:
		json_parse = consulta_bases(index)
		try:
			for x in json_parse['hits']['hits']:
				if(x['_source']['server.ip'] == ip):
					if(x['_source']['server.port'] not in dic_ip[ip]):
						dic_ip[ip].append(x['_source']['server.port'])
						with open ('/docker/data/'+target+'/vulns.txt','a') as file:
								file.write(str(ip)+' '+str(x['_source']['server.port'])+'\n')
		except:
			pass
	consulta_diretorios(sistema)
def consulta_vuln():
	list_vulns = []
	with open ('/docker/data/'+target+'/vulns.txt','a') as file:
		file.write('\n[+]LISTA DE VULNERABILIDADES\n\n')
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			try:
				for x in json_parse['hits']['hits']:
					if(x['_source']['url.original'] == sistema):
						if(x['_source']['server.ip'] != '0.0.0.0'):
							ip = x['_source']['server.ip']
						if(x['_source']['vulnerability.name'] not in list_vulns):
							list_vulns.append(x['_source']['vulnerability.name'])
							with open ('/docker/data/'+target+'/vulns.txt','a') as file:
								file.write(x['_source']['vulnerability.name']+'\n')
			except:
				pass
	consulta_ip(ip)

def main():
	os.system('rm -rf /docker/data/'+target+'/vulns.txt')
	consulta_vuln()

if __name__ == '__main__':
	main()

