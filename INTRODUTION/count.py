vector = []
x = int(input())
while x != -1: 
    vector.append(x)
    x = int(input())

print("Digite o elemento a ser buscado: ")
elemento = int(input())
print("O elemento %d aparece %d vezes no vetor" % (elemento, vector.count(elemento))) 
#o metodo count() retorna a quantidade de vezes que o elemento aparece no vetor