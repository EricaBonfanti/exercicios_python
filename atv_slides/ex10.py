#DESCRIÇÃO NARRATIVA:
#1- Digite o valor da base do retânuglo
#2- Digite o valor da altura do retângulo
#3- faça a conta de multiplicação entre a base e a altura
#4- imprima o resultado

#FLUXOGRAMA '
#  [início]
#      |
#[valor b e h]
#      |
# [res = b*h]
#      |
#    [fim]


#PSEUDOCÓDIGO
#algoritmo "Lado Retângulo"
#var
#   b: inteiro
#   h: inteiro
#   res: real
#inicio
#   escreval("Qual a base do retângulo? ")
#   leia(b)
#   escreval("Qual a altura do retângulo?")
#   leia(h)
#      res <- b * h
#      escreva("A área do retângulo é: " , R)
#fimalgoritmo

#PROGRAMA
b = int(input("Qual a base do retângulo? "))
h = int(input("Qual a altura do retângulo? "))

res = b * h

print(f"A área do retângulo é: {res}")