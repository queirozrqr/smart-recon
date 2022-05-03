#!/usr/bin/env python3

import sys
import socket
import string
import sys
import datetime
import requests
import subprocess
import os
import shutil
import uuid
import json
import time
from time import strftime
from pathlib import Path

target = sys.argv[1]
domain = sys.argv[2]

def parallel():
    os.system('rm -rf /docker/data/'+target+'/temp/subdomain_parallel_temp.log')
    with open ('/docker/data/'+target+'/temp/subdomain_parallel_temp.log','a') as file:
        file.write('python3 /docker/scripts/Modulo6_parse_assetfinder_temp.py '+target+' '+domain+'\n')
        file.write('python3 /docker/scripts/Modulo6_parse_subfinder_temp.py '+target+' '+domain+'\n')
        file.write('python3 /docker/scripts/Modulo6_parse_sublist3r_temp.py '+target+' '+domain+'\n')
    print("[+] PROCESSANDO SUBDOMAIN \n")
    os.system('cat /docker/data/'+target+'/temp/subdomain_parallel_temp.log | parallel -u')
def main():
   parallel() 
if __name__ == '__main__':
    main()
