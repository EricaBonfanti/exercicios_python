#O que é preciso fazer no programa anterior para que o programa
#  ao finalizar os cálculos, solicite novamente um novo cálculo
#  e só encerre quando solicitado?

while True:
    print("\n--- CALCULADORA LEI DE OHM ---")
    print("1 - TENSÃO (V)")
    print("2 - RESISTÊNCIA (R)")
    print("3 - CORRENTE (I)")
    print("4 - SAIR")

    opc = int(input("\nDigite qual das opções você deseja (1, 2, 3 ou 4): "))

    if opc == 1:
        r = float(input("Informe o valor da resistência (R): "))
        i = float(input("Informe o valor da corrente (I): "))
        v = r * i
        print(f"-> A tensão (V) é: {v}V\n\n\n")

    elif opc == 2:
        v = float(input("Informe o valor da tensão (V): "))
        i = float(input("Informe o valor da corrente (I): "))
        r = v / i
        print(f"-> A resistência (R) é: {r}Ω\n\n\n")

    elif opc == 3:
        v = float(input("Informe o valor da tensão (V): "))
        r = float(input("Informe o valor da resistência (R): "))
        i = v / r
        print(f"-> A corrente (I) é: {i}A\n\n\n")

    elif opc == 4:
        print("Encerrando o programa... Até logo!\n\n\n")
        break  # Este comando sai do laço while imediatamente

    else:
        print("Opção inválida! Tente novamente.")