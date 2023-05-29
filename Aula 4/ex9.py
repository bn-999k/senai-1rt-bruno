while True:
    n = int(input("Digite um número (digite um valor negativo para sair): "))
    
    if n < 0:
        print("Fim da linha pra você amigo!")
        break
    
    if n % 2 == 0:
        print("O número", n, "é par.")
    else:
        print("O número", n, "é ímpar.")
