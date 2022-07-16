executa(sistema)
with open('/docker/data/'+target+'/temp/'+saida) as jsonfile:
        for linejson in jsonfile:
            jsonline = linejson.rstrip('\n')
            jsondata = json.loads(jsonline)
            for i in jsondata:
                if('http' in jsondata['matched-at'] or 'https' in jsondata['matched-at']):
                    url = 'https://$2:9200/'+target+'-webvuln/_doc?refresh'
                    dic_web['vulnerability.name'] = jsondata['info']['name']
                    dic_web['vulnerability.severity'],= jsondata['info']['severity']
                    dic_web['server.port'] = sys.argv[6]
                    try:
                        dic_web['description'] = jsondata['info']['description']
                    except:
                        dic_web['description'] = jsondata['info']['name']
                    dic_web['url.original'] = jsondata['host']
                    try:
                        dic_web['description'] = dic_web['description']+' '+jsondata['matcher-name']
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
                    'url.path':dic_web['url.path'],
                    'http.response.status_code':dic_web['http.response.status_code'],
                    'vulnerability.description':dic_web['vulnerability.description'],
                    'vulnerability.name':dic_web['vulnerability.name'],
                    'vulnerability.severity':dic_web['vulnerability.severity'],
                    'url.original':dic_web['url.original'],
                    'url.full':dic_web['url.full'],
                    'vulnerability.scanner.vendor':scanner
                    }
                    print(data)
                    #r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
                    #print (r.text)
                else:
                    url = 'https://$2:9200/'+target+'-infravuln/_doc?refresh'
                    dic_infra['server.address'] = sys.argv[2]
                    try:
                        dic_infra['server.ip'] = jsondata['ip']
                    except:
                        dic_infra['server.ip'] = '0.0.0.0'
                    try:
                        dic_infra['server.port'] = jsondata['matched-at'].split(':')[1]
                    except:
                        dic_infra['server.port'] = sys.argv[6]
                    data = {
                    '@timestamp':hora,
                    'server.address':dic_web['server.address'],
                    'server.domain':dic_web['server.domain'],
                    'server.ip':dic_web['server.ip'],
                    'server.port':dic_web['server.port'],
                    'network.protocol':dic_web['network.protocol'],
                    'url.path':dic_web['url.path'],
                    'http.response.status_code':dic_web['http.response.status_code'],
                    'vulnerability.description':dic_web['vulnerability.description'],
                    'vulnerability.name':dic_web['vulnerability.name'],
                    'vulnerability.severity':dic_web['vulnerability.severity'],
                    'url.original':dic_web['url.original'],
                    'url.full':dic_web['url.full'],
                    'vulnerability.scanner.vendor':scanner
                    }
                    print(data)
                    #r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
                    #print (r.text)









for i in root.iter('scandetails'):
    dic_web['server.ip'] = i.attrib['targetip']
    dic_web['server.address'] = i.attrib['targethostname']
    dic_web['server.domain'] = i.attrib['targethostname']
    dic_web['server.port'] = i.attrib['targetport']
    dic_web['network.protocol'] = i.attrib['sitename'].split(':')[0]
    dic_web['service.name'] = i.attrib['sitename'].split(':')[0]
    dic_web['http.response.status_code'] = '200'
    dic_web['url.original'] = sistema
    for scan in i:
        if(scan.tag == 'item'):
            for item in scan:
                if(item.tag == 'description'):
                    dic_web['vulnerability.description'] = item.text.replace('\n ','').replace(' \n','')
                    dic_web['vulnerability.name'] = item.text.replace('\n ','').replace(' \n','')
                    dic_web['vulnerability.severity'] = 'N/A'
                if(item.tag == 'uri'):
                    dic_web['url.path'] = item.text.replace('\n ','').replace(' \n','')
                if(item.tag == 'namelink'):
                    dic_web['url.full'] = item.text.replace('\n ','').replace(' \n','')
            data = {
                    '@timestamp':hora,
                    'server.address':dic_web['server.address'],
                    'server.domain':dic_web['server.domain'],
                    'server.ip':dic_web['server.ip'],
                    'server.port':dic_web['server.port'],
                    'network.protocol':dic_web['network.protocol'],
                    'url.path':dic_web['url.path'],
                    'http.response.status_code':dic_web['http.response.status_code'],
                    'vulnerability.description':dic_web['vulnerability.description'],
                    'vulnerability.name':dic_web['vulnerability.name'],
                    'vulnerability.severity':dic_web['vulnerability.severity'],
                    'url.original':dic_web['url.original'],
                    'url.full':dic_web['url.full'],
                    'vulnerability.scanner.vendor':scanner
            }
            #print(data)
            r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data), verify=False)
            print (r.text)