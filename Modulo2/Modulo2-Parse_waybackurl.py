import string
import sys

dic_wayback = {}

def parse():
    with open('/home/mbuogo/smart-recon/wayback.txt') as file:
        for line in file:
            dic_wayback['urlfull'] = line.rstrip('\n')
            dic_wayback['protocolo'] = line.rstrip('\n').split(':')[0]
            print(dic_wayback)

def main():
    parse()
    
if __name__== '__main__':
    main()


#waybackurls --> https://github.com/tomnomnom/waybackurls