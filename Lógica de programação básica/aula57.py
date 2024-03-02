"""
Lista de listas e seus indices:
"""

salas = [
    # 0         # 1
    ["Allan", "Felipe"],  # -> 0
    ["Matheus"],  # -> 1
    ["Thais", "Milena", "Maria"]  # -> 2
]

print(salas[1][0])
print(salas[0][0])
print(salas[2][0])

for sala in salas:
    print(f"A sala é {sala}")
    for aluno in sala:
        print(aluno)
