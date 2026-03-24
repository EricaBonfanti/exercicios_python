#Crie um programa que peça um valor e imprima na tela se o valor é positivo,
#negativo ou ainda igual a zero.


n1 = int(input("Difite um número: \n"))

if n1 == 0:
    print("O número é igual a zero")
elif n1 > 0:
    print("O número é positivo")
else:
    print("O número é negativo")