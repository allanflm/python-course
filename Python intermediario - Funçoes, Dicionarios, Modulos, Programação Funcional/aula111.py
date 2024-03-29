from functools import partial
from types import GeneratorType


def print_iter(iterador):
    print(*list(iterador), sep="\n")
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_porcentagem = partial(
    aumentar_porcentagem,
    porcentagem=1.1,
)


def mudar_preco_de_produtos(produto):
    return {
        **produto,
        "preco": aumentar_porcentagem(
            produto["preco"]
        )
    }


novos_produtos = list(map(mudar_preco_de_produtos, produtos))

print_iter(produtos)
print_iter(novos_produtos)


print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
