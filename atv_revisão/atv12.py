n1 = input("Digite o primeiro numero: \n ")
n2 = input("Digite o segundo numero: \n ")
n3 = input("Digite o terceiro numero: \n ")

print("Qual o menor número entre eles?")
if n1 < n2 and n1 < n3:
    print(n1)       
elif n2 < n1 and n2 < n3:
    print(n2)
else: 
    print(n3)

print("Qual o maior número entre eles?")
if n1 > n2 and n1 > n3:
    print(n1)       
elif n2 > n1 and n2 > n3:
    print(n2)
else: 
    print(n3)