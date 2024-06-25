"""
Uma string é um conjunto de caracteres indexados,
o primeiro caracter possui indice zero.
"""

nome = "Chicago"

print(nome)
print(nome[0]) # imprime o C
print(nome[2]) # imprime o i
print(nome[5])

# Range crescente e decrescente:
print("Range crescente:")
for x in range(1, 11, 1):
    print(x)

print("Range descrescente:")
for x in range(10, 0, -1):
    print(x)

nome = "Chicago"
nome2 = "Queens"

# Imprime pulando uma linha:
print(nome)
print(nome2)

# Imprime sem pular linha, eu escolho o que terá
# no final do comando.
print(nome, end=" ")
print(nome2)

nome = "Chicago"
for x in nome:
    print(x, end="")
print()

