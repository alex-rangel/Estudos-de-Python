"""
Estruturas de Repetição - loops

while
for
do while*
"""

s = "pernambuco"

for x in s:
    print(x)

# Em python posso multiplicar um número
# por uma string para repetir a string.
print(15 * "-")

#range(6) significa que começamos do 0
#até termos 6 números destintos, ou seja,
#de 0 a 5, o 0 também conta.
for x in range(6):
    print(x)

print(15 * "-")

#range (inicio, fim), o 15 não entra.
for x in range(3, 15):
    print(x)

print(15 * "-")

#range(inicio, fim, passo) 0 10 não entra.
for x in range(2,10, 2):
    print(x)
print(f"Variavel x: {x}")

print(15 * "-")

#for com else
for x in range(6):
    print(x)
else:
    #x, no exemplo, termina com valor 5,
    #else não passa para 6.
    print(f"Chegamos ao fim:{x}")

print(15 * "-")