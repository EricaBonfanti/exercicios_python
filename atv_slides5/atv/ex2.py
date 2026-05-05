#Desenvolva um script Python que lê vários números positivos via teclado.
#Quando o número lido for -1, o script deve parar e exibir a soma de todos
#os números positivos inseridos, a média desses números, o menor e o maior número digitado.

num = int(input("Digite número:"))
soma = 0
cont = 0
maior = float('-inf')
menor = float('inf')


while num != -1:
    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("Digite número:"))
    if num >= 0:
        continue    
    
    elif num < -1:
        print("Negative Error")
        break
   
    
    
media = soma / cont
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
        
  
