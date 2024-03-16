a, b = 1, 2
a, b = a, b

# print(a, b)

pessoa = {
    "nome": "Allan",
    "sobrenome": "Felipe",
}

dados_pessoa = {
    "idade": 20,
    "altura": 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# args e kwargs
# kwargs -> keywords arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print("NAO NOMEADOS:", args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome="Allan", qlt=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracos = {
    "arg1": 1,
    "arg2": 2,
    "arg3": 3,
    "arg4": 4,
}
mostro_argumentos_nomeados(**configuracos)
