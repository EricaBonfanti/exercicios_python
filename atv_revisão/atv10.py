quantos_hora = int(input("Olá, quantos você recebe por hora?"))

horas_mes = int(input("Quantas horas você trabalha por mês?"))

salario = quantos_hora * horas_mes
print(f"Você recebe um salário de {salario} por mês.")

# valor salario conforme o desconto do ir, inss, sindicato
ir_desc = salario - (salario * 11 / 100)
inss_desc = salario - ( salario * 8 / 100)
sindicato_desc = salario - (salario * 5 /100)

# quanto será descontado por cada desconto.
ir = (salario * 11 / 100)
inss = ( salario * 8 / 100)
sindicato = (salario * 5 /100)

salario_desc = ir + inss + sindicato
salario_final = salario - salario_desc

print(f"seu salário bruto é: {salario: .2f}")
print(f"Seu salário final é: {salario_final: .2f}")