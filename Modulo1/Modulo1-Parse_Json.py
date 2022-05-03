import sys
import string
import json

with open('/home/mbuogo/smart-recon/json_basico.json') as json_file:
    jsondata = json.load(json_file)
    for i in jsondata:
        print(i)