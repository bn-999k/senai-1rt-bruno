salário = float (input("Informe seu salário: ") )

if salário > 8250:
    novosalario = salário + (salário * 0.10)
else:
    novosalario = salário + (salário * 0.15)

print("Seu novo salário é de: ", novosalario)
