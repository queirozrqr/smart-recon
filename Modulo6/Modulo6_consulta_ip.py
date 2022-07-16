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
lista_index = ['subdomain','portscan','webenum','webvuln','infravuln']
json_parse = ''
dic_ip = {}

def consulta_bases(index):
	data = {"size":10000}
	url = 'https://$2:9200/'+target+'-'+index+'/_search'
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	return(parse_scan)

def mostra_ips():
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			if(x['_source']['server.ip'] not in lista_ips ):
				lista_ips.append(x['_source']['server.ip'])

	os.system('clear')
	print('\n',lista_ips,'\n')

def mostra_portas(op,ip):
	dic_ip = {}
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			if(x['_source']['server.ip'] not in dic_ip and x['_source']['server.ip'] != '0.0.0.0'):
				dic_ip[x['_source']['server.ip']] = []
		try:
			for x in json_parse['hits']['hits']:
				if(x['_source']['server.port'] not in dic_ip[x['_source']['server.ip']]):
					dic_ip[x['_source']['server.ip']].append(x['_source']['server.port'])
		except:
			pass
	os.system('clear')
	if(op == '5'):
		for y in dic_ip:
			if(y == ip):
				print(y,dic_ip[y])
	else:
		print(dic_ip)
def mostra_vuln(op):
	dic_ip = {}
	for index in lista_index:
		json_parse = consulta_bases(index)
		for x in json_parse['hits']['hits']:
			if(x['_source']['server.ip'] not in dic_ip and x['_source']['server.ip'] != '0.0.0.0'):
				dic_ip[x['_source']['server.ip']] = []
			try:
				for x in json_parse['hits']['hits']:
					if(op == '3'):
						if(x['_source']['vulnerability.name'] not in dic_ip[x['_source']['server.ip']]):
							dic_ip[x['_source']['server.ip']].append(x['_source']['vulnerability.name'])
					if(op == '4'):
						if(x['_source']['vulnerability.name'] not in dic_ip[x['_source']['server.ip']] and x['_source']['vulnerability.severity'] == 'high'):
							dic_ip[x['_source']['server.ip']].append(x['_source']['vulnerability.name']+' | Severity: '+x['_source']['vulnerability.severity'])
			except:
				pass
	os.system('clear')
	print(dic_ip)
def main():
	op = 99
	while (int(op) > 0):
		print("\n 1 - Mostrar Enderecos IPs\n")
		print("\n 2 - Mostrar Portas\n")
		print("\n 3 - Mostrar Vulnerabilidades\n")
		print("\n 4 - Mostrar Vulnerabilidades HIGH\n")
		print("\n 5 - Mostrar Portas IP\n")
		print(" 0 - Sair\n")
		op = input(" > Digite um número: ")
		os.system('clear')
		if(op == '1'):
			mostra_ips()
		if(op == '2'):
			ip = '0.0.0.0'
			mostra_portas(op,ip)
		if(op == '3'):
                        mostra_vuln(op)
		if(op == '4'):
                        mostra_vuln(op)
		if(op == '5'):
			ip = input("## Digite o IP: ")
			mostra_portas(op,ip)
		if(op == '0'):
			os.system('clear')
if __name__ == '__main__':
	main()
