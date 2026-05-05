 #Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: 

#• adição (opção 1) 
#• subtração (opção 2) 
#• multiplicação (opção 3) 
#• divisão (opção 4)
#• saída (opção 5) 

#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta
#  ao menu de opções. O programa somente termina quando for escolhida a opção de saída (opção 5).

for i in range (0, 1):
    print("MENU")   
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opc = int(input("Escolha sua opção para a conta:"))
    if opc == 5:
        print("Saindo...")
        break
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if opc == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opc == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opc == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opc == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Opção inválida")