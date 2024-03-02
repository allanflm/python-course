# Desenpacotamento em chamadas de métodos e funçoes

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, 4, "Eduarda"]
tupla = "Python", "é", "legal"

salas = [
    # 0         # 1
    ["Allan", "Felipe"],  # -> 0
    ["Matheus"],  # -> 1
    ["Thais", "Milena", "Maria"]  # -> 2
]

p, b, *_, ap, u = lista
# print(p, b, ap)

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep="\n")
