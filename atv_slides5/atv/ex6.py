print("1 - TENSÃO (V)")
print("3 - RESISTÊNCIA (R)")
print("2 - CORRENTE (I)")
opc = 0

for i in range (0, 1):
    opc = int(input("Digite qual das opções você deseja: (1, 2 ou 3)"))
    if opc == 1:
        r = float(input("Informe o valor da resistência (R): "))
        i = float(input("Informe o valor da corrente (I): "))
        v = r * i
        print(f"A tensão (V) é: {v}")
    elif opc == 2:
        v = float(input("Informe o valor da tensão (V): "))
        r = float(input("Informe o valor da corrente (I): "))
        r = v / i
        print(f"A corrente (I) é: {i}")
    elif opc == 3:
        v = float(input("Informe o valor da tensão (V): "))
        i = float(input("Informe o valor da corrente (I): "))
        r = v / r
        print(f"A resistência (R) é: {r}")
    else:
        print("Opção inválida")