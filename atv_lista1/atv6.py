print ("Área do Trapézio")

b1_input = input("Qual o primeiro valor da base? ")
b2_input = input("Qual o segundo número da base? ")
h_input = input("Qual a altura do trapézio? ")

b1 = int(b1_input)
b2 = int(b2_input)
h = int(h_input)

res = ((b1+b2) * h) / 2

print (f"A área do trapézio é: {res}")
