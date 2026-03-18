# Desenvolva um programa que leia uma frase e um caractere. Em seguida, exiba ambos e o número
# de ocorrências do caractere na frase

frase = input("Escreva uma frase! \n ")
carac = input("Digite um caractere que você deseja tirar da frase: \n")

frase_sem_carac = frase.replace(carac,'')
print(frase_sem_carac)