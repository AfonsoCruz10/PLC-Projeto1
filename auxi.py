import re
 
def numero(lista):
    if len(lista) == 1:
        return int(lista[0])
    else:
        return int(lista[1])

def forma_correta_lista(lista):
    nova_lista = []
    for i in lista:
        if i == '':
            continue
        elif re.search(r'[0-9]+', i) != None:
            nova_lista.append(int(i))
        else:
            nova_lista.append(i)
    return nova_lista

def nome_correto(parte):
    nome = ""
    lista = re.split(r'{\d+,\d+}|{\d+}',parte)
    if lista[1] != "":
        nome = lista[0] + "_" + re.search(r'\w+', lista[1]).group()
    else:
        nome = lista[0]
    return nome


def funcao_agregacao(nome,lista):
    x = 0
    if re.search(r'sum',nome) != None:
        for i in lista:
            x += i
        resultado = x
    elif re.search(r'media',nome) != None:
        for i in lista:
            x += i
        resultado = int(x/len(lista))
    else:
        resultado = lista    
    return resultado        

