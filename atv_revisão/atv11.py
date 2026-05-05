n1 = float(input("Digite sua primeira nota: \n "))
n2 = float(input("Digite sua segunda nota: \n "))
n3 = float(input("Digite sua terceira nota: \n "))

res = (n1+n2+n3)/3

if res == 10:
    print("Parabéns, você é um aluno nota 10!")
elif res >= 7:
    print("Você está aprovado.")
else:
    print("Infelizmente, você está reprovado.")
print(res)