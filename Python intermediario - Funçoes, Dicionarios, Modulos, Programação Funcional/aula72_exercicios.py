# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def mult(*args):
    total = 1
    for i in args:
        total *= i

    return total


multiplicao = mult(1, 2, 3, 4)
print(multiplicao)
print(1 * 2 * 3 * 4)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(x):
    if x % 2 == 0:
        return "PAR"

    return "IMPAR"


num = par_impar(1)
print(num)
