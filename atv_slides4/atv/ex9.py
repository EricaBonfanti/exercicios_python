#Escreva um programa que verifique se uma letra digitada é vogal ou consoante.
#Ou ainda se não está nestes grupos.

letra = input("Digite uma letra: \n")
if letra in "aeiouAEIOU":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")