def adiciona_cliente(nome, lista =None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_cliente("Allan")
adiciona_cliente("Felipe",cliente1)
adiciona_cliente("Matheus", cliente1)

cliente1.append("Thais")

cliente2 = adiciona_cliente("Maria")
adiciona_cliente("Janete",cliente2)

cliente3 = adiciona_cliente("Ana")
adiciona_cliente("Luiza", cliente3)


print(cliente1)
print(cliente2)
print(cliente3)