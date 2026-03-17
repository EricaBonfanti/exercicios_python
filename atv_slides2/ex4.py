#) Construa um programa que receba do usuário a variação do deslocamento 
# de um objeto (em metros) e a variação do tempo percorrido (em segundo).
#  Ao fim, o programa deve calcular a velocidade média, em m/s, do objeto. 
# Mostrar os dados fornecidos e o valor calculado.

deslocamento = float(input("Digite a variação do deslocamento: "))
tempo = float(input("Digite a variação do tempo: "))


if (tempo <= 0):
    print("ERROR! Digite velocidade maior que zero.")
else:
    res = deslocamento/tempo
    print(f"A velocidade média é: {res} m/s")