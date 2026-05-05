lista_vazia = []

for i in range(5): 
   valor = int(input(f"Digite o {i+1}º valor inteiro: "))
   lista_vazia.append(valor)

print("valores na ordem de entrada")
print(lista_vazia)

print("valores na ordem inversa")
print(lista_vazia[::-1])