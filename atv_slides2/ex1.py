
i = float(input("Digite a rentabilidade: "))
pv = float(input("Digite o valor do investimento: "))
n = float(input("Digite o número de meses: "))

fv = ((1+i)*pv)**n

print(f"A resposta final da sua aplicação é:"  "%.2f" % fv)