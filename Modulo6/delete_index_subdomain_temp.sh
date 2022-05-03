echo
echo [+] Delete index SUBDOMAIN TEMP
echo
curl -XDELETE --insecure --user admin:'83d875fc-8789-11ec-9757-00505642c2bf' https://localhost:9200/$1-subdomain-temp
echo
