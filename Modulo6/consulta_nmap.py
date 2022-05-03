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

def consulta_subdomain():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(x['_source']['server.port'] == '21' or x['_source']['server.port'] == '22' or x['_source']['server.port'] == '23'):
			print(x['_source']['server.ip'],x['_source']['server.port'])
def main():
	consulta_subdomain()
if __name__ == '__main__':
	main()
