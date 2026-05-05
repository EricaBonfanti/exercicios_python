velocidade_rad = float(input("Digite a velocidade que você está dirigindo no momento: \n"))
velocidade_max = 80
multa1 = 85.13
multa2 = 127.69
multa3 = 574.62
leve = 3
media = 5
gravissima = 7

if velocidade_rad < velocidade_max:
    print("Você não foi multado!")
elif velocidade_rad > velocidade_max and velocidade_rad <= 90:
    print(f"Você foi multado em R${multa1} por dirigir a {velocidade_rad} km/h, causanto uma infração leve de {leve} pontos.")
elif velocidade_rad > 90 and velocidade_rad <= 130:
    print(f"Você foi multado em R${multa2} por dirigir a {velocidade_rad} km/h, causanto uma infração média de {media} pontos.")
elif velocidade_rad > 130:
    print(f"Você foi multado em R${multa3} por dirigir a {velocidade_rad} km/h, causanto uma infração gravissima de {gravissima} pontos.")
