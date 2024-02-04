# Operados logicos:
# OR
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.

# entrada = input("[E]ntrar ou [S]air: ")
# senha_digitada = input("Senha: ")
# senha_permitida = "1234"


# if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
#     print("Entrando..")
# else:
#     print("Saindo...")

# Avaliacao de curto circuito
senha = input("Senha: ") or "nenhuma senha digitada..."
print(senha)
