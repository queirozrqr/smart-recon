import sys
import string
import requests
import json

dic_openrdap = {}

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


def main():
    parse()
    
if __name__== '__main__':
    main()


#OpenRDAP --> https://github.com/openrdap/rdap