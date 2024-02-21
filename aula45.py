"""
 -> Iteravel - str, range etc (__iter__)
 -> Iterador - que entrage um valor por vez
 -> Next - me entregue o proximo valor.
 -> Iter - me entregue seu iterador.
"""

texto = "Allan"

# iterador = iter(texto) -> iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break


for letra in texto:
    print(letra)
