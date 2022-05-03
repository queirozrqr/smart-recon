import sys
import string
import requests
import json

dic_openrdap = {}
dic_openrdap_ip = {}

def parse():
    r = requests.get('https://rdap.registro.br/domain/businesscorp.com.br')
    retorno_rdap = r.text
    json_rdap = json.loads(retorno_rdap)
    dic_openrdap['domain'] = json_rdap['handle']

    for name in json_rdap['nameservers']:
        dic_openrdap['nameserver'] = name['ldhName']
        dic_openrdap['dono'] = json_rdap['entities'][0]['vcardArray'][1][2][3]
        dic_openrdap['resposavel'] = json_rdap['entities'][1]['vcardArray'][1][2][3]
        print(dic_openrdap)

def parse_tool():
    with open('/home/mbuogo/smart-recon/openrdap.json') as jsonfile:
        json_rdap_ip = json.load(jsonfile)
        dic_openrdap_ip['blocoip'] = json_rdap_ip['handle']
        dic_openrdap_ip['startAddress'] = json_rdap_ip['startAddress']
        dic_openrdap_ip['endAddress'] = json_rdap_ip['endAddress']
        print(dic_openrdap_ip)

def main():
    #parse()
    parse_tool()
if __name__== '__main__':
    main()


#OpenRDAP --> https://github.com/openrdap/rdap