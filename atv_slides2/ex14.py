#Você está desenvolvendo um programa para calcular a área de um hexágono regular com base no raio fornecido pelo usuário.
#  Um hexágono regular tem seis lados de igual comprimento e seis ângulos internos de 120 graus.
#  Assim, para determinar a área desse hexágono, basta determinar a área de um dos triângulos e,
#  em seguida, multiplicar o resultado por 6.
import math

print("Vamos calcular a área de um hexágono regular!")

raio = float(input("Digite o valor do raio"))

area_triangulo = (math.sqrt(3) / 4) * (raio**2)
area_hexagono = 6 * area_triangulo

print(f"Área do hexágono: {area_hexagono:.2f}")