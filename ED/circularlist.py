

n = int(input("Digite o tamanho da lista: "))
list = [0]*n
beg = end = 0
while True:
    print("1 - Adicionar elemento")
    print("2 - Remover elemento")
    print("3 - Mostrar")
    print("4 - Sair")
    op = int(input("Digite a opção: "))
    if op == 1:
        element = int(input("Digite o elemento: "))
        list[end] = element
        end = (end+1)%n # Circular
    elif op == 2:
        if beg == end:
            print("Lista vazia")
        else:
            print("Elemento removido:", list[beg])
            beg = (beg+1)%n
    elif op == 3:
        print(list)
    elif op == 4:
        break
    else:
        print("Opção inválida")