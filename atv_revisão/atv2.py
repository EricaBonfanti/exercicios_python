# Para cada problema a seguir, elabore um script em linguagem Python.
# a. Dado um número real qualquer, informe qual é o seu dobro.
# b. Dadas as medidas de uma sala em metros (comprimento e largura),
# informe a sua área em metros quadrados.
# c. Dados o valor da compra e o percentual de desconto, calcule
# o valor a ser pago. Considere que o percentual de desconto é um
# número real entre 0 e 1.

num = float(input("Digite um número real: \n"))
if num > 0:
    print(f"O dobro de {num} é {num * 2}.")

comp = float(input("Digite o comprimeiro de uma sala em metros: \n"))
larg = float(input("Digite a largura de uma sala em metros: \n"))
area = comp * larg
print(f"A área da sala é {area} metros quadrados.")

compr = float(input("Digite o valor da sua compra:"))
desc = float(input("Digite o porcentual do seu desconto entre 0 e 1:"))
if desc < 0 or desc > 1:
    print("Valor de desconto inválido. Por favor, insira um valor entre 0 e 1.")
else:
    valor_desconto = compr * desc
    valor_final = compr - valor_desconto
    print(f"O valor a ser pago é {valor_final:.2f}.")