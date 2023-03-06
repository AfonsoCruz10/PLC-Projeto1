import re
from auxi import *
from Cria import *

# Abrir o ficheiro com modo leitura e converter para string
file = open("emd1.csv", mode='r')
string = file.read()
file.close()
# Iterar pelas linhas do ficheiro 
lines = re.split(r'\n', string)
# Estrutura que irá ter todas as linhas numa lista sendo que cada elemento faz parte de uma coluna
lst = []

for i in lines:
    o = re.split(r',(?!\d+})',i)
    lst.append(o)


lst_dics = []
for linha in lst[1:]:
    dics = {}
    i = 0
    for parte in lst[0]:
        if parte == "":
            continue
        elif re.search(r'(\w+{[0-9]+,[0-9]+}|\w+{[0-9]+})(::sum|::media)?', parte) == None:
            dics[parte] = linha[i]
            i += 1
        else:
            nome = nome_correto(parte)
            nums = re.findall(r'[0-9]+', parte)
            tamanho_inf = int(nums[0])
            limite = numero(nums)
            lista = []
            while limite > 0:
                lista.append(linha[i])
                limite -= 1
                i +=1
            lista_final = forma_correta_lista(lista)    
            if len(lista_final) >= tamanho_inf:    
                dics[nome] = funcao_agregacao(nome,lista_final)
            else:
                dics[nome] = "Tamanho incorreto"    
    lst_dics.append(dics)

escreve_file(lst_dics)
