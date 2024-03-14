def executa(funcao, *args):
    return funcao(*args)


# Lambdas:
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))


print(executa(lambda x, y: x + y,
              1, 2))

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5))

# Funçoes:
# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica
