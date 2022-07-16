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
url = 'https://$2:9200/'+target+'-webvuln/_search'
auth=('admin', $3)

def consulta():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(x['_source']['url.original'] == 'http://businesscorp.com.br' and x['_source']['vulnerability.severity'] == 'info'):
			print(x['_source']['vulnerability.name'],x['_source']['vulnerability.severity'],x['_source']['vulnerability.scanner.vendor'])
def main():
	consulta()
if __name__ == '__main__':
	main()
