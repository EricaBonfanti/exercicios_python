#Elabore um programa que leia uma frase, uma palavra antiga e uma palavra nova.
#  O programa deve exibir uma string contendo a frase original e outra com a ocorrência
#  da palavra antiga substituída pela palavra nova.

#Exemplo:
#	Frase: “Quem parte e reparte fica com a maior parte”
#	Palavra antiga: “parte”
 #    	Palavra nova: “parcela”
#	Resultado a ser impresso no programa : “Quem parcela
#		e reparcela fica com a maior parcela”
#Dica: use replace

frase = input("Digite uma frase: \n")
old = input("Digite a palavra antiga: (ela deve estar na frase) \n")
new = input("Digite a palavra nova: \n")

print(f"frase antiga: {frase}")
print(f"frase nova: {frase.replace(old,new)}")

