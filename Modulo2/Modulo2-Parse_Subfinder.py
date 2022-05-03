import sys
import string
import json

dic_subfinder = {}

def parse():
    with open('/home/mbuogo/smart-recon/subfinder-json.json') as json_file:
        for line in json_file:
            json_line = line.rstrip('\n')
            jsondata = json.loads(json_line)
            dic_subfinder['subdomain'] = jsondata['host']
            dic_subfinder['source'] = jsondata['source']
            print(dic_subfinder)


def main():
    parse()
    
if __name__== '__main__':
    main()


#Subfinder --> https://github.com/projectdiscovery/subfinder