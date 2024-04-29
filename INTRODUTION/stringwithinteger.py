n = int(input())
soma = 0
for result in range(1, n+1):
    if result > 99:
        soma=(soma*1000)+result
    elif result > 9:
        soma = (soma*100)+result
    else:
        soma = (soma*10)+result
    
print(soma)