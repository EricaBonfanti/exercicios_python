#Faça um programa que calcule o fatorial de um número inteiro fornecido
#pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120.

#A saída deve ser conforme o exemplo abaixo:

num = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1

for i in range (num, 0, -1):
    fatorial *= i
    print(f"{i}", end="")

print(f" = {fatorial}")