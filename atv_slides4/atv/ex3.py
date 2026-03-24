idade = int(input("Digite sua idade: \n "))

if (idade<18): 
    print("Você é menor de idade! Não pode dirigir.")
elif ((idade>=18) and (idade<=95)):
    print("Pode acelerar...")
else:
    print("Cuidado, o senhor já está com uma certa idade.")

print("Verificação de idade concluída!!")