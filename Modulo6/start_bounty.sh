#!/bin/bash

TGT=$1

rm -rf /docker/data/$TGT/temp/*

echo "[+] INICIO DO BOUNTY - Enumeracao de Subdominios"
echo
for domain in $(cat /docker/data/$TGT/domains.txt);do
	python3 /docker/scripts/subdomain_parallel.py $TGT $domain
done
echo

echo "[+] Enumeracao de Sistemas"
echo
python3 /docker/scripts/httpx_parallel.py $TGT
echo

echo "[+] Enumeracao de Diretorios Web"
echo
python3 /docker/scripts/gobuster_parallel.py $TGT
echo

echo "[+] Enumeracao de URLs"
echo
python3 /docker/scripts/wayback_parallel.py $TGT
echo

echo "[+] Port Scanning"
echo
python3 /docker/scripts/nmap_parallel.py $TGT
echo

echo "[+] Scan Vulnerabilidades Web"
echo
python3 /docker/scripts/nikto_parallel.py $TGT
python3 /docker/scripts/nuclei_parallel.py $TGT
echo

echo "[+] Scan Vulnerabilidades Infra"
echo
python3 /docker/scripts/hydra_parallel.py $TGT
echo

echo "[+] FINAL DO BOUNTY"
