# dir , hasattr e getattr em Python:

string = "Allan"
metodo = "lower"

if hasattr(string, metodo):
    print(f"Exite o metodo: {metodo}")
    print(getattr(string, metodo)())
else:
    print(f"Nao exite o método: {metodo}")
