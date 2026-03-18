# Seguindo o exercício acima, exiba da mesma forma, no entanto a entrada será com todos os caracteres maiúsculos.
# Dica: use .lower() e .title()

name = input("Digite seu nome todo em MAIÚSCULO! " + "\n")

#Usando .tittle() para transformar primeira letra em maiúsculo!
name_minusculo_first = name.lower()
name_maiusculo = name_minusculo_first.title()

print(name_maiusculo)