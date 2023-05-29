def area(largura, comprimento):
    total = largura * comprimento
    return total

largura = float(input("Qual a largura do terreno: "))
comprimento = float(input("Qual o comprimento do terreno: "))

resultado = area(largura, comprimento)

print("A área do terreno é", resultado, "metros quadrados.")


