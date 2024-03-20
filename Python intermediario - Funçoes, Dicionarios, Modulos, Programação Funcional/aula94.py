# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print("ABriu o arquivo")
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print("DIVIDIU POR ZERO")
except IndexError as erro:
    print("IndexError")
except (NameError, ImportError):
    print("NameError, ImportError")
else:
    print("Nao deu erro!")
finally:  # sempre será executado com o try
    print("FECHAR ARQUIVO")
