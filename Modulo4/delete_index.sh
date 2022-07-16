curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-subdomain
echo
curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-portscan
echo
curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-webenum
echo
curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-webvuln
echo
curl -XDELETE --insecure --user admin:$3 https://$2:9200/$1-infravuln
