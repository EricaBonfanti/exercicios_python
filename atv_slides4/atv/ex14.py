#Construa um programa que tem como dados de entrada dois pontos quaisquer no plano
#cartesiano: P1 e P2. Considere que P1 é definido pelas coordenadas x1 e y1,
#enquanto P2 por x2 e y2 . O programa deve calcular e escrever a distância entre
#os pontos P1 e P2. A fórmula que calcula a distância entre os dois pontos é dada por:

#d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#A função que calcula a raiz quadrada é a sqrt() (square root), veja pow()
import math

p1x = int(input("Digite a coordenada x1 do ponto P1: \n"))
p1y = int(input("Digite a coordenada y1 do ponto P1: \n"))
p2x = int(input("Digite a coordenada x2 do ponto P2: \n"))
p2y = int(input("Digite a coordenada y2 do ponto P2: \n"))

d = math.sqrt((p2x-p1x)**2 + (p2y-p1y)**2)

print(f"A distância entre os pontos P1 e P2 é: {d}")