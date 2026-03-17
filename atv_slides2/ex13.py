# Você foi contratado para desenvolver um programa que calcule o Índice de Massa Corporal (IMC)
# com base nos dados de altura e peso fornecidos pelo usuário. O IMC é uma medida que relaciona
# o peso e a altura de uma pessoa para avaliar se ela está abaixo do peso, com peso normal, com sobrepeso ou obesa.
# A fórmula para calcular o IMC é: IMC = peso / (altura^2), onde o peso é em quilogramas e a altura é em metros

print("Vamos calcular a massa coproral?")

alt = float(input("Digite sua altura"))
pes = float(input("Digite seu peso"))

imc = pes / (alt**2)

if imc <= 18.5:
 print("Você está com o imc de {imc} abaixo do peso!")
elif  18.5 < imc <= 24.9:
 print ("Você está com o imc de {imc} na media do peso!")
elif 25 < imc <= 29.9:
 print("Você está com o imc de {imc} com sobrepeso!")
else:
 print("Você está com o imc de {imc} com obesidade!")
