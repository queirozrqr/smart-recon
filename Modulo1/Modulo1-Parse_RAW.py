import string
import sys

dic_raw = {}

def parse_raw():
    with open('/home/mbuogo/smart-recon/raw.txt') as file:
        for i in file:
            dic_raw['subdomain'] = i.rstrip('\n').split(' ')[0]
            dic_raw['ip'] = i.rstrip('\n').split(' ')[1]
            print(dic_raw)

def main():
    parse_raw()
    
if __name__== '__main__':
    main()