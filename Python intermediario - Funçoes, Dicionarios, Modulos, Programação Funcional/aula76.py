# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    "nome": "Allan",
    "sobrenome": "Felipe",
    "idade": 20,
    "peso": 1.89,
    "endereços": [
        {"rua": "Tal tal", "numero": 123},
        {"rua": "Tal 2 tal 2", "numero": 123}]
}

print(pessoa)

print(pessoa["nome"])
print("--------")
for chave in pessoa:
    print(f"{chave} -> {pessoa[chave]}")
