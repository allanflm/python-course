"""
Introducao ao try/except:
    try -> tenta executar o codigo
    except -> ocorreu algun erro ao executar o codigo.
"""

numero_str = input("Vou dobrar o numero que voce digitar: ")


try:
    print(f"STR {numero_str}")
    numero_float = float(numero_str)
    print(f"FLOAT: {numero_float}")
    print(f"O dobro do numero {numero_str} é {numero_float * 2}")
except:
    print("Voce nao digitou um numero!")


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"O dobro do numero {numero_str} é {numero_float * 2}")
# else:
#     print("Voce digitou algo incorreto!....")
