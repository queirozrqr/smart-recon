import sys
import string
import json

lista_livros = []
dic_livros = {}

def monta_lista():
    with open('/home/mbuogo/smart-recon/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                if('prateleira' in k):
                    for prat in jsondata[i][k]:
                        lista_livros.append(prat['titulo'])

def dicionario_livros():
    with open('/home/mbuogo/smart-recon/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                if('prateleira' in k):
                    for prat in jsondata[i][k]:
                        dic_livros['prateleira'] = k
                        dic_livros['livro'] = prat['titulo']
                        print(dic_livros)
                        
def mostra_lista():
    print(lista_livros)

def listar_ativos():
    with open('/home/mbuogo/smart-recon/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            if(i == 'clientes'):
                for k in jsondata[i]:
                    print(k,jsondata[i][k]['emprestimo'])

def main():
    #monta_lista()
    #mostra_lista()
    #dicionario_livros()
    listar_ativos()
    
if __name__== '__main__':
    main()