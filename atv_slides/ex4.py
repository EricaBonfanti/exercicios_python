print("Olá, seja bem-vindo ao formulário")

name = str(input("Qual o seu nome? "))
city = str(input("Qual cidade você mora? "))
state = str(input("Qual estado você mora? "))
date = str(input("Qual sua data de nascimento? separe com: xx/xx/xxxx "))

print("Ok, obrigada pelas informações.")
print(f"{name}, você mora no estado: {state}. Você mora na cidade de {city}, e também nasceu no dia: {date}")
