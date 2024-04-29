#função com tuplas

def soma(*lista): # chamada de função com indeterminados argumentos formando uma tupla (o uso do * é obrigatório para informar a criação da tupla)
    total = 0
    for i in lista: # passagem por cada item na tupla
        total +=i # soma de cada item da tupla no total
    return total

print(soma(1,2,3,4))