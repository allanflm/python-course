# Dictionaty Comprehension e Set comprehension:


produto = {
    "nome": "Caneta Azul",
    "preco": 2.4,
    "categoria": "Escritorio",
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != "categoria"
}
# print(dc)

lista = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]

dc = {
    chave: valor
    for chave, valor in lista
}
# print(dc)

# set
s1 = {2 ** i for i in range(10)}
print(s1)
