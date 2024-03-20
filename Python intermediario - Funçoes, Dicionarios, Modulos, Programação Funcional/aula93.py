# try e except para tratar execeções:
# a = 18
# b = 0
# c = a / b
try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print("linha 2")

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print("b nao esta definido!")
except (TypeError, IndexError) as erro:
    print("TypeErro + IndexErro")
    print("MSG: ", erro)
    print("Nome: ", erro.__class__.__name__)
except Exception:
    print("Erro desconhecido!")

print("CONTINUA!")
