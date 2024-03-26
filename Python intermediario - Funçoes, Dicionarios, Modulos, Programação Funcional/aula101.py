# Exercicio - Adiando execução de funções:

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def cria_funcao(funcao, x):
    def funcao_interna(y):
        return funcao(x, y)
    return funcao_interna


soma_cinco = cria_funcao(soma, 5)
multiplica_por_dez = cria_funcao(multiplica, 10)


print(soma_cinco(5))
print(multiplica_por_dez(10))
