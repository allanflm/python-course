# Operadores logicos:
# AND

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Entrando...")
else:
    print("Senha incorreta...")
