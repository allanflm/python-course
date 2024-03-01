"""
Operação Ternaria (condicao de uma linha só)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 11
variavel = "Valor" if condicao else "outro valor"
print(variavel)

digito = 10
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print("valor" if False else "outro valor" if False else "FIM!")
