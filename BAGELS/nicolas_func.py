import random

def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida
    False --> Entrada Inválida
    """
    if 1000 < num < 10000:
        return True
    else:
        return False

def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    """
    numeros = list(range(10)) #Lista com os números de 0 a 9
    secretNum = 0 

    while numeros[0] == 0: #Garante que o primeiro número não seja 0
        random.shuffle(numeros) #Embaralha a lista
    
    for i in range(4):
        dig = numeros[i] #pega o número na posição i
        secretNum += dig*(10**(3-i)) #multiplica o número por 10 elevado a 3-i e soma a secretNum (2*10³ + 3*10² + 4*10 + 5*1 = 2345)

    return secretNum, numeros[:4] #retorna o número secreto e a lista com os 4 primeiros números da lista
                

def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o número escolhido e o número secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Código
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi

    Retorna uma lista vazia caso os dois números sejam iguais
    """

    if num == secretNum: #se os números forem iguais
        return [] #retorna uma lista vazia (o usuário acertou o número e venceu o jogo)

    dica = []

    for i in range(4):
        dig = num % 10 #pega o último dígito do número
        if dig == secretNumList[3-i]: #se o dígito for igual ao dígito na mesma posição do número secreto
            dica.append(2) #Fermi
        elif dig in secretNumList: #se o dígito estiver na lista do número secreto
            dica.append(1) #Pico
        num //= 10 #remove o último dígito do número

    if len(dica) == 0: #se a lista estiver vazia
        dica.append(0) #Bagels

    dica.sort() #ordena a lista

    return dica

        
