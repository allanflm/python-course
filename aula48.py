"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# string = "ABCD"

# lista = [123, True, "Allan", 1.2, []]

# print(lista[2], type(lista[2]))
# print(lista[2].upper(), type(lista[2]))

# # -----------------------------------
# print(lista[-3])
# lista[-3] = "Felipe"
# print(lista[-3])


lista = [10, 20, 30, 40]
print(lista)

# # - adicionado
# lista.append(50)
# print(lista)

# # removendo o ultimo valor
# print(f"ultimo valor removido -> {lista.pop()}")

# deletar por indice
del lista[-1]
print(lista)

# limpar lista
# lista.clear()
# print(lista)

# adicionando um valor por indice
lista.insert(0, "numeros")
print(lista)
