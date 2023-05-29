from time import sleep
def contagem_regressiva(numero):
    if numero < 0:
        print("O número deve ser positivo.")
        return

    while numero > 0:
        numero = numero - 1
        print(numero)
        sleep(1)

nm = int(input("Digite um número inteiro positivo: "))

contagem_regressiva(nm)


#sleep = vai diminuindo (nesse caso de 1 em 1)