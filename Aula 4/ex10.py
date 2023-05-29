while True:
    num = int(input("Insira um numero ( - 1 para finalizar) > "))
    if num == 1:
        break
result = 1
cont = 1
while cont <= num:
    result *= cont
    cont += 1
    print ("{}! = {}.".format(num,result))
