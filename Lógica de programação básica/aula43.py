#  Introdução ao for / in - estrutura de repetição para coisas finitas

texto = "Python"
new_char = ""
for letra in texto:
    new_char += f"-{letra}"
    print(letra)

print(new_char + "!")
