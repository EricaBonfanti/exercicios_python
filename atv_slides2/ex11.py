#9) Você foi contratado para desenvolver um programa que calcule área de uma coroa circular com base 
# em duas medidas de raio fornecido pelo usuário. 
#A=π(R^2−r^2)
import math

print("Vamos calcular a área de uma coroa circular!")

rmaior = float(input("Digite o valor do raio maior! "))
rmenor = float(input("Agora digite o valor do raio menor! "))

area = (math.pi * (rmaior**2 - rmenor**2 ))

print (f"P valor final da área foi: {area}")