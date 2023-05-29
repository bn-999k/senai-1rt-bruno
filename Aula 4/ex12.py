num = int(input("Digite um número inteiro: "))



if num < 0:
    print("Não é possível calcular o número negativo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print("O fatorial de", num, "é", fatorial)