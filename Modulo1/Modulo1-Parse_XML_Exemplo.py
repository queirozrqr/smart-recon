import string
import xml.etree.ElementTree as ET
import sys

tree = ET.parse('/home/mbuogo/smart-recon/exemplo.xml')
root = tree.getroot()

def parse_xml():
    for i in root.iter('teste'):
        for y in i:
            print(y.attrib)

def main():
    parse_xml()
    
if __name__== '__main__':
    main()