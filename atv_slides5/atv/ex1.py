#Para construir o programa a seguir, considere que os usuários só informarão
#  números inteiros positivos. Crie um programa que receba 5 números digitados
#  e, ao final, exiba a quantidade de números pares.

#1) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 à 10. O usuário deve informar de qual número ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo

i = 1
num = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1