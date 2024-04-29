def exp(n):
    def eleva(x):
         n**x
         
    return eleva

def main():
    y = int(input("Digite a base: "))
    f = exp(y)
    x = int(input("Digite o expoente: "))
    print(y,"elevado a",x, "=",  f(x))
    
main()

    