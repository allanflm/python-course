"""- Calculadora While - """


while True:

    n1 = input("Digite um numero -> ")
    n2 = input("Digite outro numero -> ")
    operador = input("Digite o operador (+ | - | * | /) -> ")

    numeros_validor = None

    n1_float = float(n1)
    n2_float = float(n2)

    try:
        numeros_validor = True

    except:
        numeros_validor = None

    if numeros_validor is None:
        print("Um ou ambos o numeros são invalidor!")
        continue

    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        print("Operador invalido!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue

    print("-- Realizando sua conta...")
    if operador == "+":
        print(f"A soma entre {
            n1_float} + {n2_float} = {n1_float + n2_float}")
    elif operador == "-":
        print(f"A subtração entre {
            n1_float} - {n2_float} = {n1_float - n2_float}")
    elif operador == "*":
        print(f"A multiplicação entre {
            n1_float} * {n2_float} = {n1_float * n2_float}")
    elif operador == "/":
        print(f"A divisão entre {
            n1_float} / {n2_float} = {n1_float / n2_float}")

    sair = input("Quer sair: [S]im -> ").lower().startswith("s")
    if sair is True:
        print("Saindo....")
        break
