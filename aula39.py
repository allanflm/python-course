"""
Iterando strings com while:s
"""

nome = "Allan Felipe Malinoski"

index = 0
novo_nome = ""
while index < len(nome):
    letra = nome[index]
    novo_nome += f"*{letra}"
    index += 1

novo_nome += "*"
print(novo_nome)
