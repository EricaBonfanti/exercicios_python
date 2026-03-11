
a = int(input('Digite um numero QUALQUER: '))
b = int(input('Digite um numero DIFERENTE de 0 (Zero): '))

try:
    print(a / b)
except ZeroDivisionError:
    print ("Divisão por zero - invalida!")
