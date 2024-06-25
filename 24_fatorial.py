"""
Encontrar o fatorial de um número.
Pode ser feito com while ou for.
"""

# Com while:
fatorial = 1
i = 1
numero = int(input("Informe um número:"))

while numero >= i:
    fatorial = fatorial * i
    i = i + 1
print(f"Com while: {numero}! = {fatorial}")

# Com for:
fatorial = 1
if numero < 0:
    print("Não existe fatorial de números negativos.")
elif numero == 0:
    print(f"O fatorial de {numero} é 1.")
else:
    for x in range(1, numero+1):
        fatorial = fatorial * x
    print(f"Com for: {numero}! = {fatorial}")