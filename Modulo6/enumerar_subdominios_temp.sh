#!/bin/bash

TGT=$1

rm -rf /docker/data/$TGT/temp/*

echo "[+] Enumeracao de Subdominios"
echo
for domain in $(cat /docker/data/$TGT/domains.txt);do
	python3 /docker/scripts/subdomain_temp_parallel.py $TGT $domain
done
echo

