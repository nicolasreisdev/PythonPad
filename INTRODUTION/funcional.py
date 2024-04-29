matriz = []



def main(): # Função principal do programa
    print("Inicializando o programa de manipulação de matrizes!")
    m = int(input("Digite o número de linhas da matriz: "))
    n = int(input("Digite o número de colunas da matriz: "))
    buildMatrix(m,n,matriz)
    print(matriz)
    opcao = int(input("Oque você deseja?\n 1 - Trocar elementos da matriz\n 2 - Imprimir a matriz\n 3 - Sair do Programa\n"))
    while opcao != 3:
        if opcao == 1:
            pos1 = int(input("Digite a posição do primeiro elemento a ser trocado: "))
            pos2 = int(input("Digite a posição do segundo elemento a ser trocado: " ))
            trocaElemento(pos1,pos2,matriz)
            print(matriz)
            
        if opcao == 2:
            for i in range(0,m):
                for j in range(0,n):
                    print(matriz[i][j], end = " ") # end = " " para não pular linha
                print() # pula uma linha
                
        opcao = int(input("Oque você deseja?\n 1 - Trocar elementos da matriz\n 2 - Imprimir a matriz\n 3 - Sair do Programa\n"))
        
        
    
        

def buildMatrix(m,n, matriz): # Função para construir a matriz
    
    for i in range(1,m+1):
        linha = []
        for j in range(1,n+1):
            x = int(input("Digite o número da coluna %i%i da matriz:" %(i,j)))
            linha.append(x)
        matriz.append(linha)
        
def trocaElemento(pos1, pos2, matriz): # Função para trocar elementos da matriz
    elemento1 = matriz[pos1[0]][pos1[1]]
    elemento2 = matriz[pos2[0]][pos2[1]]
    matriz[pos1[0]][pos1[1]] = elemento2
    matriz[pos2[0]][pos2[1]] = elemento1
        
        
main()
            
