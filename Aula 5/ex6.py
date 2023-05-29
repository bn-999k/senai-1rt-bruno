def sm(a, b):
    return a + b

def mtp(a, b):
    return a * b

def maior(a, b):
    return max(a, b)

def menor(a, b):
    return min(a, b)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

opcao = input("Escolha uma opção:\n"
              "1. Somar\n"
              "2. Multiplicar\n"
              "3. Maior número\n"
              "4. Menor número\n"
              "Escolha uma opção: ")

if opcao == "1":
    resultado = sm(v1, v2)
    print("Resultado da soma:", resultado)
elif opcao == "2":
    resultado = mtp(v1, v2)
    print("Resultado da multiplicação:", resultado)
elif opcao == "3":
    resultado = maior(v1, v2)
    print("Maior número:", resultado)
elif opcao == "4":
    resultado = menor(v1, v2)
    print("Menor número:", resultado)
else:
    print("Opção inválida.")