name = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2 

print(f"{name}, sua média aritmética das notas é: {media}")

if (media >= 6):
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
