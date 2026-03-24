#Um posto de abastecimento está comercializando combustíveis com a seguinte
#tabela de descontos:

#Álcool: 		até 20 litros, desconto de 2% por litro;
#	       	acima de 20 litros, desconto de 5% por litro;

#Gasolina: 	até 20 litros, desconto de 4% por litro;
#	       	acima de 20 litros, desconto de 6% por litro;

#Desenvolva um programa em Python que leia o número de litros vendidos e o tipo de 
#combustível (codificado com A – Álcool e G – Gasolina), calcule e imprima o valor a 
#ser pago pelo cliente, sabendo que o litro da gasolina está em R$ 5,57 e do álcool R$ 4,98.

alcool = 4.98
gasolina = 5.5


litros = input("Digite qual combustível deseja abastecer (A - Álcool ou G - Gasolina): \n")

if litros in "Aa":
    qtd = int(input("Digite quantos litros você deseja por no seu carro: \n"))
    if qtd <= 20:
        res = alcool * qtd 
        res_alcool = 0.02 * res
        res -= res_alcool
        print(f"O valor a ser pago é: R$ {res}")
    else:
        res = alcool * qtd 
        res_alcool = 0.05 * res
        res -= res_alcool
        print(f"O valor a ser pago é: R$ {res}")

elif litros in "Gg":
    qtd = int(input("Digite quantos litros você deseja por no seu carro: \n"))
    if qtd <= 20:
        res = gasolina * qtd
        res_gasolina = 0.04 * res
        res -= res_gasolina
        print(f"O valor a ser pago é: R$ {res}")
    else:
        res = gasolina * qtd
        res_gasolina = 0.06 * res
        res -= res_gasolina
        print(f"O valor a ser pago é: R$ {res}")
