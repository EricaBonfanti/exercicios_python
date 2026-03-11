n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if(n1>=n2):
    res = n1/n2
    print(f"A resposta da divisão é: {res}")
else:
    res = n2/n1
    print(f"A resposta da divisão é: {res}")
