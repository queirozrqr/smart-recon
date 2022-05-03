import sys
import string
import json

def parse():
    with open('/home/mbuogo/smart-recon/json_Array.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                for t in k:
                    print(i+" - "+t+" - "+k[t])

def main():
    parse()

if __name__== '__main__':
    main()