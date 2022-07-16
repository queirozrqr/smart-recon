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
auth=('admin', $3)
lista_ips = []
lista_sis = []
lista_index = ['subdomain','portscan','webenum','webvuln','infravuln']
json_parse = ''
dic_sis = {}

def consulta_bases(index):
	data = {"size":10000}
	url = 'https://$2:9200/'+target+'-'+index+'/_search'
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	return(parse_scan)

def mostra_sistemas():
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			try:
				if(x['_source']['url.original'] not in lista_sis):
					lista_sis.append(x['_source']['url.original'])
			except:
				pass
	os.system('clear')
	print('\n',lista_sis,'\n')

def mostra_diretorios():
	list_sis = []
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			try:
				if(x['_source']['url.full'] not in list_sis and x['_source']['vulnerability.scanner.vendor'] == 'gobuster'):
					list_sis.append(x['_source']['url.full'])
					with open ('/docker/data/'+target+'/diretorios.txt','a') as file:
						file.write(x['_source']['url.full']+'\n')
			except:
				pass
	print(list_sis)
def mostra_vuln(op):
	dic_sis = {}
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			try:
				if(x['_source']['url.original'] not in dic_sis):
					dic_sis[x['_source']['url.original']] = []
				try:
					for x in json_parse['hits']['hits']:
						if(op == '3'):
							if(x['_source']['vulnerability.name'] not in dic_sis[x['_source']['url.original']]):
								dic_sis[x['_source']['url.original']].append(x['_source']['vulnerability.name'])
						if(op == '4'):
							if(x['_source']['vulnerability.name'] not in dic_sis[x['_source']['url.original']] and x['_source']['vulnerability.severity'] == 'high'):
								dic_sis[x['_source']['url.original']].append(x['_source']['vulnerability.name'])
				except:
					pass
			except:
				pass
	os.system('clear')
	print(dic_sis)
def main():
	op = 99
	while (int(op) > 0):
		print("\n 1 - Mostrar Sistemas\n")
		print("\n 2 - Mostrar Diretorios\n")
		print("\n 3 - Mostrar Vulnerabilidades\n")
		print("\n 4 - Mostrar Vulnerabilidades HIGH\n")
		print(" 0 - Sair\n")
		op = input(" > Digite um número: ")
		os.system('clear')
		if(op == '1'):
			mostra_sistemas()
		if(op == '2'):
			mostra_diretorios()
		if(op == '3'):
                        mostra_vuln(op)
		if(op == '4'):
                        mostra_vuln(op)
		if(op == '0'):
			os.system('clear')
if __name__ == '__main__':
	main()
