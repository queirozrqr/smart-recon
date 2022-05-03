import sys
import string
import json

with open('/home/mbuogo/smart-recon/json_Object.json') as json_file:
    jsondata = json.load(json_file)
    for i in jsondata:
        for k in jsondata[i]:
            print("chave externa: "+i+" - chave:"+k+" value:"+jsondata[i][k])