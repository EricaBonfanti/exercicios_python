# Sua tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto. Você deve mostrar:
#	Preço original do produto
#	Valor do desconto em R$ (tipo 'Você ganhou R$ xx,xx de desconto’)
#	Valor do produto com o desconto

preco = float(input("Qual o preço do produto?"))

desconto = preco * 0.20
preco_final = preco - desconto

print(f"O preço final é {preco_final}")