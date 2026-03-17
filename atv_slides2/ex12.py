# Você está desenvolvendo um programa para calcular a vazão de um fluido em um tubo com base no diâmetro
# interno do tubo e na velocidade do fluxo. A fórmula para calcular a vazão deve ser pesquisada. 
# Os dados de entrada devem ser alimentados em metros e m/s.

import math

# Entrada de dados
d = float(input("Digite o diâmetro do tudo (em metros): "))
v = float(input("Digite a velocidade do fluido (em m/s)"))

# Cálculo vazão
q = (math.pi * d**2 / 4)

#Saída
print(f"A vazão do fluido é: {q:.4f} m/s")
