lista = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista.append(nota)

media = sum(lista) / len(lista) # Calcula a média das notas usando a função sum() e len()
print(f"A média das notas é: {media}")
print(f"A maior nota é: {max(lista)}")
print(f"A menor nota é: {min(lista)}")

print("Notas na ordem de entrada:")
print(lista)

