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

cliente = sys.argv[1]
dominio = sys.argv[2]

def monta_lista_atual(cli):
    data = {"size":10000}
    url_get = ('https://10.255.51.63:9200/'+cli+'-url-crawler/_search')
    get_doc = requests.get(url_get, headers=headers, auth=auth_get, data=json.dumps(data), verify=False)
    parse_scan = json.loads(get_doc.text)
    for x in parse_scan['hits']['hits']:
        if (x['_source']['url.full'] not in list_urls):
            list_urls.append(x['_source']['url.full'])
    print(len(list_urls))

def monta_parallel_nuclei():
    for i in list_urls:
        x = cliente+'-'+str(uuid.uuid1()).split('-')[0]+'-nuclei'
        with open ('nuclei.log','a') as file:
            file.write('docker run --rm --name '+x+' kali-tools:1.0 nuclei -t /root/nuclei-templates/ -u '+i+' --silent >> /home/hunt/bounty/nuclei.txt\n')
    print("\n[+] NUCLEI")
    os.system('cat /home/hunt/bounty/nuclei.log | parallel -u')

def monta_parallel_jaeles():
    for i in list_urls:
        x = cliente+'-'+str(uuid.uuid1()).split('-')[0]+'-nuclei'
        with open ('jaeles.log','a') as file:
            file.write('docker run --rm --name '+x+' kali-tools:1.0 /roo/go/bin/jaeles scan -u '+i+' >> /home/hunt/bounty/jaeles.txt\n')
    print("\n[+] JAELES")
    os.system('cat /home/hunt/bounty/jaeles.log | parallel -u')

def main():
    monta_lista_atual(cliente)
    monta_parallel_nuclei()
    monta_parallel_jaeles()
if __name__ == '__main__':
    main()
