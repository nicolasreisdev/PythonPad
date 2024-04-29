def soma(y):
    global x # informa que a variável x é global e pode ser usada fora do escopo da função
    x += y
    return x

x = 10
print(x) # valor de x antes da chamada da função
print(soma(10)) # chamada da função soma
print(x) # valor de x após a chamada da função