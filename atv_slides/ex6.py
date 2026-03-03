print ("REAJUSTE DO SALÁRIO!")
sal_input = input("Digite seu salário: ")
rea_input = input ("Qual a % do seu reajuste? ")

sal = int(sal_input)
rea = int(rea_input)

novo_salario = sal % rea

print (f"Seu novo salário é: {novo_salario}")
