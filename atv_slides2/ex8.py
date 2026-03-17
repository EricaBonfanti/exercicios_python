#) Um novo modelo de carro, super econômico foi lançado. Ele faz 20 km com 1 litro de combustível. Cada litro de combustível custa R$ 4,95.
# Faça um programa que pergunte ao usuário quanto de dinheiro ele pretende usar e em seguida o programa informa quantos litros de combustível
#  ele pode comprar e quantos quilômetros o carro consegue rodar com esta quantidade de combustível.

comb = 4.95
consumo = 20  # km por litro

qtd_comb = float(input("Quantos reais você quer colocar? "))

litros = qtd_comb / comb
km = litros * consumo

print(f"Litros: {litros:.2f}L")
print(f"Você pode rodar aproximadamente: {km:.2f} km")

