#8) A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas,
#  10% em outras, nada em outros produtos e até 30% em alguns outros produtos.
#  Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido.
#  Ele deve mostrar a saída igual ao exercício anterior.

print("Quais produtos você quer comprar? Temos opções de: laranja, tlou, camiseta tematica e lápis tematico")
carrinho = 0
#LARANJA 20%
resp = input("Você deseja comprar laranja? S/N ")
if resp == "S":
    laranja = 2.0
    desconto = laranja * 0.20
    final_laranja = laranja - desconto
    print(f"A laranja tem desconto de 20%! o valor dela original é {laranja} e o preço final é {final_laranja}")
    carrinho += final_laranja

# TLOU (30%)
resp = input("Deseja comprar TLOU? S/N: ")
if resp == "S":
    tlou = 200.50
    desconto = tlou * 0.30
    final_tlou = tlou - desconto
    print(f"TLOU: de R$ {tlou} por R$ {final_tlou}")
    carrinho += final_tlou

# CAMISETA (10%)
resp = input("Deseja comprar camiseta? S/N: ")
if resp == "S":
    camiseta = 150.00
    desconto = camiseta * 0.10
    final_camiseta = camiseta - desconto
    print(f"Camiseta: de R$ {camiseta} por R$ {final_camiseta}")
    carrinho += final_camiseta

# LÁPIS (sem desconto)
resp = input("Deseja comprar lápis? S/N: ")
if resp == "S":
    lapis = 5.00
    print(f"Lápis: preço R$ {lapis} (sem desconto)")
    carrinho += lapis

print(f"Compra finalizada! 🛒 R${carrinho}")


    
