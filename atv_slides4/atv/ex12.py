#Neste exercício, você vai criar um programa em Python que verifica se um
#componente elétrico está obedecendo à Lei de Ohm. A Lei de Ohm relaciona
#a tensão (V), a corrente (I) e a resistência (R) de um componente elétrico
#através da fórmula 
#V = I * R.

#Peça ao usuário para inserir o valor da tensão (V) em volts.
#Peça ao usuário para inserir o valor da corrente (I) em amperes.
#Peça ao usuário para inserir o valor da resistência (R) em ohms.
#Calcule a tensão esperada usando a fórmula V = I * R.
#Compare a tensão calculada com o valor inserido de tensão (V).
#Se não houver diferença entre a tensão calculada e o valor de tensão inserido, exiba: "O componente obedece à Lei de Ohm." Caso contrário, exiba: "O componente não obedece à Lei de Ohm."

v = float(input("Digite o valor da tensão em volts: \n"))
i = float(input("Digite o valor da corrente em amperes: \n"))
r = float(input("Digite o valor da resistência em ohms: \n"))

tensao_calculada = i * r

if tensao_calculada == v:
    print("O componente obedece à Lei de Ohm.")
else:
    print("O componente não obedece à Lei de Ohm.")


