velocidade = float (input("Qual a distância da viagem em km? ") )

if velocidade <= 200:
    novavelocidade = velocidade * 0.50
else:
    novavelocidade = velocidade * 0.45
    
print("O preço da viagem é: ", novavelocidade)