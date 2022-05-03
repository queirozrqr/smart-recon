import string
import xml.etree.ElementTree as ET
import sys

tree = ET.parse('/home/mbuogo/smart-recon/exemplo_complexo.xml')
root = tree.getroot()
dic_livros = {}

def parse_xml():
    for i in root.iter('livros'):
        for y in i:
            dic_livros['id'] = y.attrib['id']
            for x in y:
                if(x.tag == 'titulo'):
                    dic_livros['titulo'] = x.text
                if(x.tag == 'resumo'):
                    dic_livros['resumo'] = x.text
                if(x.tag == 'genero'):
                    dic_livros['genero'] = x.text
                if(x.tag == 'autor'):
                    for a in x:
                        dic_livros['autor'] = a.text
                        print(dic_livros)

def main():
    parse_xml()
    
if __name__== '__main__':
    main()