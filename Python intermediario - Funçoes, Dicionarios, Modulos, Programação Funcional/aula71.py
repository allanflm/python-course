"""
    args - > argumentos nao nomeados
    *args -> (empacotamento e desempacotamento)
"""


def soma(*args):
    total = 0
    for num in args:
        total += num

    return total


# soma1 = soma(1, 2, 3)
# print(soma1)

numeros = 1, 2, 3, 4, 5, 6, 7, 8
outra_soma = soma(*numeros)

print(outra_soma)
print(sum(numeros))
