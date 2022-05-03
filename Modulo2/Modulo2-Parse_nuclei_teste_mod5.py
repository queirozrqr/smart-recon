import sys
import string
import requests
import json

dic_web = {}
dic_infra = {}
hora = '00000'
target = sys.argv[1]
scanner = 'nuclei'
def parse():
    with open('/home/mbuogo/smart-recon/nuclei_full.json') as jsonfile:
        for linejson in jsonfile:
            jsonline = linejson.rstrip('\n')
            jsondata = json.loads(jsonline)
            for i in jsondata:
                if('http' in jsondata['matched-at'] or 'https' in jsondata['matched-at']):
                    #url = 'https://localhost:9200/'+target+'-webvuln/_doc?refresh'
                    dic_web['vulnerability.name'] = jsondata['info']['name']
                    dic_web['vulnerability.severity'] = jsondata['info']['severity']
                    try:
                        dic_web['vulnerability.description']= jsondata['info']['description']
                    except:
                        dic_web['vulnerability.description'] = jsondata['info']['name']
                    dic_web['url.original'] = jsondata['host']
                    try:
                        dic_web['vulnerability.description'] = dic_web['vulnerability.description']+' '+jsondata['matcher-name']
                    except:
                        pass
                    dic_web['url.full'] = jsondata['matched-at']
                    try:
                        dic_web['server.ip'] = jsondata['ip']
                    except:
                        dic_web['server.ip'] = '0.0.0.0'
                    dic_web['reference'] = jsondata['info']['reference']
                    dic_web['network.protocol'] = jsondata['host'].split(':')[0]
                    dic_web['server.address'] = sys.argv[2]
                    dic_web['server.domain'] = dic_web['server.address']
                    dic_web['server.port'] = sys.argv[3]
                    dic_web['url.path'] = sys.argv[4]
                    dic_web['http.response.status_code'] = '200'

                    data = {
                    '@timestamp':hora,
                    'server.address':dic_web['server.address'],
                    'server.domain':dic_web['server.domain'],
                    'server.ip':dic_web['server.ip'],
                    'server.port':dic_web['server.port'],
                    'network.protocol':dic_web['network.protocol'],
                    'service.name' : 'N/A',
                    'url.path':dic_web['url.path'],
                    'http.response.status_code':dic_web['http.response.status_code'],
                    'vulnerability.description':dic_web['vulnerability.description'],
                    'vulnerability.name':dic_web['vulnerability.name'],
                    'vulnerability.severity':dic_web['vulnerability.severity'],
                    'url.original':dic_web['url.original'],
                    'url.full':dic_web['url.full'],
                    'vulnerability.scanner.vendor':scanner
                    }
                else:
                    #url = 'https://localhost:9200/'+target+'-infravuln/_doc?refresh'
                    dic_infra['server.address'] = sys.argv[2]
                    dic_infra['vulnerability.name'] = jsondata['info']['name']
                    dic_infra['vulnerability.severity'] = jsondata['info']['severity']
                    try:
                       dic_infra['vulnerability.description'] = jsondata['info']['description']
                    except:
                        dic_infra['vulnerability.description']= jsondata['info']['name']
                    try:
                        dic_infra['vulnerability.description'] = dic_infra['vulnerability.description']+' '+jsondata['matcher-name']
                    except:
                        pass
                    try:
                        dic_infra['server.ip'] = jsondata['ip']
                    except:
                        dic_infra['server.ip'] = '0.0.0.0'
                    try:
                        dic_infra['server.port'] = jsondata['matched-at'].split(':')[1]
                    except:
                        dic_infra['server.port'] = sys.argv[3]
                    dic_infra['network.protocol'] = 'N/A'
                    if(dic_infra['server.port'] == '22'):
                        dic_infra['network.protocol'] = 'ssh'
                    if(dic_infra['server.port'] == '21'):
                        dic_infra['network.protocol'] = 'ftp'
                    if(dic_infra['server.port'] == '23'):
                        dic_infra['network.protocol'] = 'telnet'
                    if(dic_infra['server.port'] == '3389'):
                        dic_infra['network.protocol'] = 'rdp'
                    data = {
                    '@timestamp':hora,
                    'server.address':dic_infra['server.address'],
                    'server.ip':dic_infra['server.ip'],
                    'server.port':dic_infra['server.port'],
                    'network.protocol':dic_infra['network.protocol'],
                    'service.name' : 'N/A',
                    'vulnerability.description':dic_infra['vulnerability.description'],
                    'vulnerability.name':dic_infra['vulnerability.name'],
                    'vulnerability.severity':dic_infra['vulnerability.severity'],
                    'vulnerability.scanner.vendor':scanner
                    }
            print(data)
            print('\n')
            #r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
            #print (r.text)
        
def main():
    parse()
if __name__== '__main__':
    main()


#nuclei --> https://github.com/projectdiscovery/nuclei