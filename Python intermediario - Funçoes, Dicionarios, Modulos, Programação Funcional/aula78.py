# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set:
# -> set(iteravel) ou {1,2,3}
s1 = set("Allan")
s1 = set()  # vazio
s1 = {"Allan", 1, 2, 3}  # com dados
print(s1)
print("------")
# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(l1)
s1 = {1, 2, 3}
print(3 not in s1)
for num in s1:
    print(num)

print("------")

# Métodos uteis:
# add, update, clear, discard

s1 = set()
s1.add("Allan")
s1.add(1)
s1.update(("Ola mundo", 1, 2, 3, 4))
# s1.clear()
print(s1)
s1.discard("Ola mundo")
print(s1)

print("------")

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2  # une
print(s3)
s3 = s1 & s2  # tem nos dois
print(s3)
s3 = s1 - s2  # itens diferentes(só o da esquerda ex: s1)
print(s3)
s3 = s1 ^ s2  # nao tem igual
print(s3)
