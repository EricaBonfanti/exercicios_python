#Elabore um código fonte que calcule a hipotenusa de um triângulo retângulo,
#cujos catetos serão fornecidos pelo usuário

import math

cateto1 = int(input("Digite o cateto 1: \n"))
cateto2 = int(input("Digite o cateto 2: \n"))

h = (cateto1**2) + (cateto2**2)

resultado = math.sqrt(h)

print(f"A hipotenusa é: {resultado}")