primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

condicao_1 = primeiro_valor > segundo_valor
condicao_2 = primeiro_valor < segundo_valor

if condicao_1:
    print(f"primeiro valor = {
          primeiro_valor} é maior do que o segundo valor = {segundo_valor}")
elif condicao_2:
    print(f"O segundo valor = {
          segundo_valor} é maior do que o primeiro valor = {primeiro_valor}")
else:
    print("Voce digitou algo incorreto! Por favor tente novamente...")
