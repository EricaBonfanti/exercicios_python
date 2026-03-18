# Elabore um programa que leia o nome do usuário e mostre o nome de traz para frente, 
# utilizando somente letras maiúsculas.

name = input("What's your name? \n")
name_invert = name[::-1]
name_up = name_invert.upper()

print(name_up)
