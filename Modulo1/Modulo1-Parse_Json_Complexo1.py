import sys
import string
import json

lista_livros = []

def parse():
    with open('/home/mbuogo/smart-recon/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                if('prateleira' in k):
                    for prat in jsondata[i][k]:
                        lista_livros.append(prat['titulo'])

def main():
    parse()
    print(lista_livros)
    
if __name__== '__main__':
    main()