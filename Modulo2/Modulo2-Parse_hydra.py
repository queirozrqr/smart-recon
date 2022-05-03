import string
import sys
import json

dic_hydra = {}

def parse():
    with open('/home/mbuogo/smart-recon/hydra.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata['results']:
            dic_hydra['porta'] = i['port']
            dic_hydra['servico'] = i['service']
            dic_hydra['ip'] = i['host']
            dic_hydra['usuario'] = i['login']
            dic_hydra['senha'] = i['password']
            print(dic_hydra)
           

def main():
    parse()
    
if __name__== '__main__':
    main()


#apt-get install hydra