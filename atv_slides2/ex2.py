fv = float(input("Qual seu objetivo? "))
n = int(input("Em quantos meses você quer ter este valor? "))
i_por = float(input("Qual a rentabilidade mensal esperada (em %)? "))

i = i_por / 100

pv = fv / (1 + i)**n

print(f"Para atingir R${fv:,.2f} em {n} meses com taxa de {i_por}% ao mês,")
print(f"você deve investir inicialmente: R$ {pv:,.2f}")