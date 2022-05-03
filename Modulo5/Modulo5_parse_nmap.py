#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import datetime
import socket
import requests
import subprocess
import os
import uuid
import shutil
import json
import time
from time import strftime
from pathlib import Path

target = sys.argv[1]
domain = sys.argv[2]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://localhost:9200/'+target+'-subdomain/_doc?refresh'
auth=('admin', '83d875fc-8789-11ec-9757-00505642c2bf')
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'nmap'
dic_ports = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-nmap'
saida = 'nmap-'+x+'.xml'
ip = '37.59.174.225'

def executa():
    subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data kali-tools:2.0 nmap -sSV -Pn '+ip+' -oX /data/temp/'+saida+' || true', shell=True)

def parse():
    tree = ET.parse('/docker/data/'+target+'/temp/'+x)
    root = tree.getroot()
    for i in root.iter('nmaprun'):
        for nmaprun in i:
            if(nmaprun.tag == 'host'):
                for host in nmaprun:
                    if(host.tag == 'address'):
                        if(':' not in host.attrib['addr']):
                            dic_ports['ip_v4'] = host.attrib['addr']
                            dic_ports['addrtype'] = host.attrib['addrtype']
                    if(host.tag == 'ports'):
                        for port in host:
                            if(port.tag == 'port'):
                                dic_ports['protocol'] = port.attrib['protocol']
                                dic_ports['portid'] = port.attrib['portid']
                                for itens in port:
                                    if(itens.tag == 'state'):
                                        dic_ports['state'] = itens.attrib['state']
                                    if(itens.tag == 'service'):
                                        try:
                                            dic_ports['name'] = itens.attrib['name']
                                        except:
                                            dic_ports['name'] = ''
                                        try:
                                            dic_ports['version'] = itens.attrib['version']
                                        except:
                                            dic_ports['version'] = ''
                                        try:
                                            dic_ports['product'] = itens.attrib['product']
                                        except:
                                            dic_ports['product'] = ''
                                        try:
                                            dic_ports['cpe'] = itens.attrib['cpe']
                                        except:
                                            dic_ports['cpe'] = ''
                                        print(dic_ports)
def main():
    executa()
    parse()
    
if __name__== '__main__':
    main()
