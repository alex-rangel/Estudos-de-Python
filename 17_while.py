"""
Estruturas de Repetição - loops

while
for
do while - obs.: Não existe em Python, usaremos uma estratégia.
"""
a = 0

while a <= 5:
    print(a)
    a = a + 1
print(f"Resultado final de 'a' após sair de while: {a}")

#Ultilizando o break:
print()
a = 0
while a <= 5:
    print(a)
    if a == 3:
        break
    a = a + 1
print(f"Resultado final de 'a' após sair de while: {a}")

#Ultilizando o else
#O else só é executado se a condição do loop
#se tornar falsa e sair do laço.

print()
a = 0
while a <= 5:
    print(a)
    a = a + 1
else:
    print(f"Resultado final de 'a' após sair de while: {a}")