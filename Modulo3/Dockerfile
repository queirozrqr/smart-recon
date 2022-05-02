FROM kalilinux/kali-rolling:latest

WORKDIR /scripts

WORKDIR /data

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get dist-upgrade -y

RUN apt-get install locate -y

RUN apt-get install wget -y

RUN apt-get install git -y

RUN apt-get install vim -y

RUN apt-get install golang -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip3 install uuid

RUN GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
RUN mv /root/go/bin/subfinder /usr/bin/

RUN apt-get install sublist3r -y

RUN apt-get install nmap -y

RUN apt-get install nikto -y

RUN apt-get install hydra -y

RUN go get -u github.com/tomnomnom/assetfinder
RUN mv /root/go/bin/assetfinder /usr/bin/

RUN go get -u github.com/openrdap/rdap/cmd/rdap
RUN mv /root/go/bin/rdap /usr/bin/

RUN GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx
RUN mv /root/go/bin/httpx /usr/bin/

RUN go get github.com/tomnomnom/waybackurls
RUN mv /root/go/bin/waybackurls /usr/bin/

RUN GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
RUN mv /root/go/bin/nuclei /usr/bin/
RUN nuclei -update-templates
