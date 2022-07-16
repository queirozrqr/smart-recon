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
import telegram
from time import strftime
from pathlib import Path

target = sys.argv[1]
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
url = 'https://$2:9200/'+target+'-subdomain/_search'
url_temp = 'https://$2:9200/'+target+'-subdomain-temp/_search'
url_post = 'https://$2:9200/'+target+'-subdomain/_doc?refresh'
auth=('admin', $3)
hora = strftime("%Y-%m-%dT%H:%M:%S%Z")
scanner = 'monitora_subs'
dic_subdomain = {}
x = str(uuid.uuid1()).split('-')[0]
container_name = target+'-'+x+'-monitora_subs'
list_subs = []
list_subs_novos = []

def consulta_subdomain_base():
	data = {"size":10000}
	get_doc = requests.get(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
	parse_scan = json.loads(get_doc.text)
	for x in parse_scan['hits']['hits']:
		if(str(x['_source']['server.domain']) not in list_subs):
			list_subs.append(str(x['_source']['server.domain']))
def consulta_subdomain_novos():
    data = {"size":10000}
    get_doc = requests.get(url_temp, headers=headers, auth=auth, data=json.dumps(data), verify=False)
    parse_scan = json.loads(get_doc.text)
    for x in parse_scan['hits']['hits']:
        if(str(x['_source']['server.domain']) not in list_subs and x['_source']['server.domain'] not in list_subs_novos):
            list_subs_novos.append(x['_source']['server.domain'])
def rdap_ip(ip):
    try:
        consulta1 = subprocess.check_output('docker run --rm --name '+container_name+' -v /docker/data/'+target+'/temp:/data kali-tools:2.0 /root/go/bin/rdap '+ip+' --json || true', shell=True) 
        json_rdap_ip = json.loads(consulta1)
        blocoip = json_rdap_ip['handle']
        return(blocoip)
    except:
        return('')

def rdap_domain(domain):
    nameserver = ''
    try:
        consulta2 = requests.get('https://rdap.registro.br/domain/'+domain)
        json_rdap = json.loads(consulta2.text)
        for ns in json_rdap['nameservers']:
            nameserver = nameserver+ns['ldhName']+','
        return(nameserver[:-1])
    except:
        return('')

def executa():
    os.system('sh /docker/scripts/delete_index_subdomain_temp.sh '+target)
    os.system('sh /docker/scripts/criar_index_subdomain_temp.sh '+target)
    os.system('sh /docker/scripts/enumerar_subdominios_temp.sh '+target)
def parse():
    for line in list_subs_novos:
        dic_subdomain['server.address'] = line.rstrip('\n')
        dic_subdomain['server.domain'] = line.rstrip('\n')
        try:
            dic_subdomain['server.ip'] = socket.gethostbyname(line.rstrip('\n'))
        except:
            dic_subdomain['server.ip'] = '0.0.0.0'
        dic_subdomain['vulnerability.scanner.vendor'] = scanner
        dic_subdomain['server.ipblock'] = rdap_ip(dic_subdomain['server.ip']) 
        dic_subdomain['server.nameserver'] = rdap_domain(dic_subdomain['server.domain'])
        data = {
                 '@timestamp':hora,
                 'server.address':dic_subdomain['server.address'],
                 'server.domain':dic_subdomain['server.domain'],
                 'server.ip':dic_subdomain['server.ip'],
                 'server.ipblock':dic_subdomain['server.ipblock'],
                 'server.nameserver':dic_subdomain['server.nameserver'],
                 'vulnerability.scanner.vendor':dic_subdomain['vulnerability.scanner.vendor']
        }
        r = requests.post(url_post, headers=headers, auth=auth, data=json.dumps(data), verify=False)
        print (r.text)
        message = "[+] New Subdomain finded - "+dic_subdomain['server.domain']+' - '+dic_subdomain['server.ip']
        bot = telegram.Bot(token='5180853037:AAEAQVVNAil6Y99Gw1Xlnn1SIHOjrJBYXFc')
        bot.send_message(text=message, chat_id=35130497)
        #print(data)

def main():
	executa()
	consulta_subdomain_base()
	consulta_subdomain_novos()
	parse()
if __name__== '__main__':
    main()
