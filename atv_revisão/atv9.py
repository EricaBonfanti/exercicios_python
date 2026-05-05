peso = float(input("Qual o peso do peixe?"))

if peso >= 50:
    multa =  4.00 * peso
    print(f"O peso é acima do regulamento. pague esta multa:")
else: 
    print("O peso do seu peixe está conforme o regulamento!")