"""
Exercício 01:
Escreva um programa que leia 5 valores e encontre
o maior e o menor deles. Mostre o resultado.

Exercício 02:
Escreva um programa para calcular as somas:
a)
S = 31/40 + 32/39 + 33/38 + 34/37 + 35/36

b)
S = 480/21 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)

c)
S = 1/21 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)
"""

"""
# Exercício 01:
# Como eu faria em Java:
n = float(input(f"Informe o 1º valor:"))
maior = menor = n

for i in range(4):
    n = float(input(f"Informe o {i+2}º valor:"))

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print(f"Maior: {maior}")
print(f"Menor: {menor}")

# Como eu faria em Python:
maior = float('-inf')
menor = float('inf')

for i in range(5):
    n = float(input(f"Informe o {i+1}º valor:"))

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print(f"Maior: {maior}")
print(f"Menor: {menor}")
"""

# Exercício 02:
# a)
# S = 31/40 + 32/39 + 33/38 + 34/37 + 35/36
"""
soma = 0
numerador = 31
denominador = 40
i = 0

while i < 5:
    print(f"{numerador}/{denominador}")
    soma += numerador/denominador
    numerador += 1
    denominador -= 1
    i += 1

print(f"A soma é : {soma}")
"""

# b)
# S = 480/21 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
"""
soma = 0
numerador = 480
denominador = 21

for i in range(25):
    print(f"{numerador}/{denominador}")
    soma += numerador / denominador
    numerador -= 5
    denominador += 1

print(f"A soma é:{soma}")
"""

# c)
# S = 1/21 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)

soma = 0
numerador = 1
denominador = 21

for i in range(20):
    print(f"{numerador}/{denominador}")
    soma += numerador / denominador
    numerador = numerador * 2 + 1
    denominador += 2

print(f"A soma é: {soma}")
