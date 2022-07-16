echo
echo [+] Delete index SUBDOMAIN TEMP
echo
curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-subdomain-temp
echo
