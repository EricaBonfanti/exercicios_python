#Uma imobiliária paga aos seus corretores um salário base de R$ 1.500,00.
#Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 5% do valor
#de cada venda. Construa um programa que solicite o nome do corretor, a quantidade
#de imóveis vendidos e o valor total de suas vendas. Ao fim, o programa deve calcular
#e escrever o salário final do corretor de imóveis.

name = input("Digite o seu nome: \n")
qtd = int(input("Digite a quantidade de imóveis vendidos: \n"))
valor_total = float(input("Digite o valor total de suas vendas: \n"))

salario_base = 1500
comissao = 200
qtd_total = qtd * comissao
qtd_total += salario_base
valor_total *= 1.05
qtd_total += valor_total

print(f"O salário final do corretor de imóveis {name} é: R$ {qtd_total}")
