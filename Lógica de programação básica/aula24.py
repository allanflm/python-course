# Operadores in e not in
# String são iteraveis
#  0 1 2 3 4
#  A l l a n

# nome = "allan"
# print(nome[0])
# print(nome[-1])

# print('all' in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} esta em {nome}")
else:
    print(f"{encontrar} nao esta em {nome}")
