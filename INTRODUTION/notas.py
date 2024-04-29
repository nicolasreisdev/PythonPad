result = float(input("Nota da primeira prova: "))
result += float(input("Nota da segunda prova: "))
result += float(input("Nota da terceira prova: "))

result /= 3
if result >= 60:
    print("Aprovado!")
    print("Média:", result)
elif result >= 40:
    print("Recuperação!")
    print("Média:", result)
else:
    print("Reprovado!")
    print("Média:", result)