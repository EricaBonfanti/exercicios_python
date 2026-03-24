#Crie um programa em Python para calcular a média de três notas inseridas
#pelo usuário e dar feedback baseado na média calculada.

#Peça ao usuário para inserir as notas de três avaliações.
#Calcule a média das notas e arredonde-a para duas casas decimais.
#Exiba a média na tela.
#Dê um dos seguintes feedbacks de acordo com a média:
#Média maior ou igual a 7.0: "Parabéns! Sua média é alta."
#Média maior ou igual a 5.0: "Sua média é razoável."
#Média abaixo de 5.0: "Sua média é baixa. É uma boa oportunidade para melhorar.".

n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))
n3 = float(input("Digite a terceira nota: \n"))
media = (n1 + n2 + n3) / 3
# O round(valor, 2) arredonda para duas casas decimais
media_arredondada = round(media, 2)

if media_arredondada >= 7.0:
    print(f"Parabéns! Sua média é alta: {media_arredondada}")
elif media_arredondada >= 5.0: 
    print(f"Sua média é mediana: {media_arredondada}")
else:
    print(f"Sua média é baixa: {media_arredondada}. É uma boa oportunidade para melhorar.")