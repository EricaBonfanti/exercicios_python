
#qual o custo para tantas copias?
book = float(input("Quantos livros você deseja comprar?"))

#preço capa: R$24,95
capa = 24.95
#desconto 35%
desc = 35
#transporte R$3,00 para primeiro
transp = 3
#75 cent para cada exemplar adiconal
transp_add = 0.75

#SE for apenas 1 livro:
if(book <= 1):
    # 1 livro vezes o valor da capa
    book_capa = book * capa
    # Add 35% de desconto por cima do valor de 1 livro
    book_capa_desc = (book_capa * desc)/100
    # No final, fazer vezes o valor do transporte!
    book_final = book_capa_desc * transp
    print("Seu custo de cópias foi: "  "%.2f" % book_final)
else:
    # 1 livro vezes o valor da capa
    book_capa = 1 * capa
    # Add 35% de desconto por cima do valor de 1 livro
    book_capa_desc = (book_capa * desc)/100
    # No final, fazer vezes o valor do transporte!
    book_final1 = book_capa_desc * transp

    # X livros vezes o valor da capa, menos o valor de 1 livro(book_final1)
    book_capa2 = (book * capa) - 9.48
    # Add 35% de desconto por cima do valor de X livros
    book_capa_desc2 = (book_capa2 * desc)/100
    # No final, fazer vezes o valor do transporte
    book_final2 = book_capa_desc * transp_add
    # Calcular a soma do livro sozinho com transporte de R$3.00 + X livros com transporte de R$0.75
    book_final = book_final1 + book_final2
    print("Seu custo de cópias foi: "  "%.2f" % book_final)
