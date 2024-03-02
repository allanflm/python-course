"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def imprimir(a):
#     print(a)


# imprimir("teste")


# def Print(a, b, c):
#     print(a, b, c)


# Print(1, 2, 3)
# Print(4, 5, 6)

nome = input("Digite seu nome: ")


def mostar_nome(nome="Sem nome"):
    print(f"Seja bem vindo {nome}!")


mostar_nome(nome)
