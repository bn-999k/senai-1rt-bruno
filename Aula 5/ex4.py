def maior(n1, n2, n3):
    num = (n1, n2, n3)
    return max(num)

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

resultado = maior(valor1, valor2, valor3)

print("O maior valor é:", resultado)