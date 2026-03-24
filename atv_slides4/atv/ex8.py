#Elabore um programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M – Masculino ou Sexo Inválido

letra = input("Digite uma letra: \n")
if letra == "f" or letra == "F":
    print("F - Feminino")
elif letra == "m" or letra == "M":
    print("M - Masculino")
else:
    print("Digite F ou M")