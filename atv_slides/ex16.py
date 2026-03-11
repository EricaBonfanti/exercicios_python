i = float(input("Digite um número mensal: "))
fv = float(input("Digite o valor: "))
n = float(input("Digite o número de meses: "))

pv = ((1+i)**n)/fv

print(f"A resposta final dos seus juros é:"  "%.2f" % pv)