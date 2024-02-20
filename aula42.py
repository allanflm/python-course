frase = 'O Python é uma linguagem de programação' \
        ' Multiparadgima' \
        "Python foi criado por ..."


i = 0
qtd_vezes = 0
letra_mais_vezes = ""
while i < len(frase):
    letra = frase[i]

    if letra == " ":
        i += 1
        continue

    qtd_letra_atual = frase.count(letra)

    if qtd_vezes < qtd_letra_atual:
        qtd_vezes = qtd_letra_atual
        letra_mais_vezes = letra
    i += 1

print(f"A letra que apareceu mais vezes foi: {
      letra_mais_vezes}.\nQuantidade de vezes: {qtd_vezes}x")
