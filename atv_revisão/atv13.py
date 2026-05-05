lado1 = float(input("Digite o valor do lado 1 do triângulo: \n"))
lado2 = float(input("Digite o valor do lado 2 do triângulo: \n"))
lado3 = float(input("Digite o valor do lado 3 do triângulo: \n"))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            print("O triângulo é equilátero.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("O triângulo é isósceles.")
        else:
            print("O triângulo é escaleno.")