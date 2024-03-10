"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(mgs, nome):
    return f"{mgs}, {nome}"


def executa(funcao, *args):
    return (funcao(*args))


print(executa(saudacao, "Bom dia ", "Allan"))
