#Escrevendo programa que recebe 2 valores de x e y. Em seguida, calculando e imprimindo o valor de z:

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

soma = (x * x) + (y * y)
print(soma)
sub =  x - y
print(sub) 
z = soma/sub

print(f"O valor de z é: {z}")