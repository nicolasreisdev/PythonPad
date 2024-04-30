
a = False
while(a == False): # Enquanto a for falso
    try: # Tente fazer isso
        x = input('Digite um número: ')
        if x.isnumeric(): # Verifica se é um número
            a = True # Se for, a = True
    except: # Se não conseguir fazer, faça isso
        print('Você não digitou um número')
    