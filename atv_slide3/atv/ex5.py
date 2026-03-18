# Elabore um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula.
# No mesmo programa exiba a frase sem espaços em branco. Dica use replace.

frase = input("Escreva uma frase toda em MAÍUSCULO!")
frase_rep = frase.replace(' ', '')
print(frase_rep)