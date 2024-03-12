# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# --- Codigo da aula: ------
# import copy
# d1 = {
#     "c1": 1,
#     "c2": 2,
#     "l1": [0, 1, 2],
# }

# d2 = d1.copy()  # apenas faz uma copia...

# # d2 = copy.deepcopy(d1) -> copia mais profunda
# # d2 = copy.copy(d1) -> copia linkando os valores dentro da lista

# d2["c1"] = 1000
# d2["l1"][1] = 999


# print(d1)
# print(d2)

p1 = {
    "nome": "allan",
    "sobrenome": "felipe"
}

# print(p1["nome"])

# # get() -> se nao exister essa chava o valor retorna como None
# print(p1.get("nome", "nao existe!"))

# pop() -> aparga a chave e guarda em uma variavel o valor da chave apagada!
# nome = p1.pop("nome")
# print(nome)
# print(p1)


# popitem() -> retorna a ultima chave do dicionario
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# update() -> cria uma nova chave, e atualiza o dicionario;
p1.update({
    "nome": "Thais",
    "idade": 21,

})
# outra opcao
p1.update(nome="allan", idade=20)
print(p1)
