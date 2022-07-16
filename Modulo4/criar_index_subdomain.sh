curl -XPUT --insecure --user admin:$3 https://$2:9200/$1-subdomain -H "Content-Type: application/json" -d @- <<EOF
{
	"mappings":{
		"properties":{
			"@timestamp":{"type":"date"},
			"server.address": {"type":"keyword"},
			"server.domain": {"type":"keyword"},
			"server.ip": {"type":"ip"},
			"vulnerability.scanner.vendor": {"type":"keyword"}
		}
	}
}
EOF
echo
