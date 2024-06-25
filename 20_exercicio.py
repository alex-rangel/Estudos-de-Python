"""
Exercício - Trocar variáveis

x e y
O que está em x, vai para Y,
e o que está em y, vai para x.
"""

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

aux = x
x = y
y = aux

print(f"Valor de x depois da troca: {x}")
print(f"Valor de y depois da troca: {y}")

"""
Ou:
"""
y, x = x, y
print(f"Valor original de x: {x}")
print(f"Valor original de y: {y}")