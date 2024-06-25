"""
Comandos de controle condicional
if, else e elif(else if)
"""

x = 50
y = 8 

print("if:")
if y > x:
    print("y é maior que x")
    print("Código dentro do bloco condicional.")
print("Código fora do bloco condicional.")

print()
print("if e else")
if y > x:
    print("y é maior que x")
    print("Código dentro do bloco condicional if.")
else:
    print("y é menor ou igual a x")
    print("Código dentro do bloco condicional else.")
print("Código fora do bloco condicional")

print()
print("Não usual em Python:")
print("if else if:")
if y < x:
    print("y é menor que x.")
else:
    print("y é igual a x.")
print("Código fora do bloco condicional.")

x = 200
y = 20

print()
print("if elif else:")

if y > x:
    print("y é maior que x")
    print("Código dentro do bloco condicional if.")
elif y < x:
    print("y é menor que x")
    print("Código dentro do bloco condicioanl elif.")
else:
    print("y é igual a x.")
    print("Código dentro do bloco condicional else")
print("Código fora do bloco condicional.")

# Operador ternário
a = 8
b = 30
c = 2

print()
# Possso colocar o comando ao lado dos dois pontos.
if b > a:print("b é maior que a.")
print("Código fora do bloco condicional.")

# Operador ternário ou Expressões Condicionais:
print("B") if b > a else print("A")
# Código equivalente ao comando acima:

if b > a:
    print("B")
else:
    print("A")

# Alinhamento de IFS

if a > b:
    if a > c:
        print("A é maior que B e que C")
else:
    if a == b:
        print("A é igual a B")