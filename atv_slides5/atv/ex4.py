#Para construir o programa a seguir, considere que os usuários só
#informarão números inteiros positivos. Crie um programa que receba
#5 números digitados e, ao final, exiba a quantidade de números pares.

conta = 0

for i in range(0, 5):
    nmero = int(input("Informe um número: "))
    i+=1
    if nmero % 2 == 0: 
        conta+=1
print(conta)





