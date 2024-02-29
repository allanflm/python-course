"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

decimal_1 = decimal.Decimal(0.1)
decimal_2 = decimal.Decimal(0.7)

soma = decimal_1 + decimal_2
print(soma)
print(f"{soma:.2f}")
print(round(soma, 3))
