import sys
import string
import requests
import json

dic_nuclei = {}

def parse():
    with open('/home/mbuogo/smart-recon/nuclei_full.json') as jsonfile:
        for linejson in jsonfile:
            jsonline = linejson.rstrip('\n')
            jsondata = json.loads(jsonline)
            for i in jsondata:
                dic_nuclei['name'] = jsondata['info']['name']
                dic_nuclei['severity'] = jsondata['info']['severity']
                try:
                    dic_nuclei['description'] = jsondata['info']['description']
                except:
                    dic_nuclei['description'] = jsondata['info']['name']
                dic_nuclei['host'] = jsondata['host']
                try:
                    dic_nuclei['matcher-name'] = jsondata['matcher-name']
                except:
                    dic_nuclei['matcher-name'] = 'N/A'
                dic_nuclei['matched'] = jsondata['matched-at']
                try:
                    dic_nuclei['ip'] = jsondata['ip']
                except:
                    dic_nuclei['ip'] = '0.0.0.0'
                dic_nuclei['reference'] = jsondata['info']['reference']
                print(dic_nuclei)
        
def main():
    parse()
if __name__== '__main__':
    main()


#nuclei --> https://github.com/projectdiscovery/nuclei