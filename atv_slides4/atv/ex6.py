#Desenvolva um script que solicite dois números quaisquer e mostre o maior entre  eles.

n1 = int(input("Digite um número: \n"))
n2 = int(input("Digite outro número: \n"))

if n1 > n2:
    print (f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")