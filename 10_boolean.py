"""
Operadores lógicos e o tipo Boolean

Em computação, boolean, ou lógico, é um tipo de dado primitivo
que possui dois valores possíveis, que podem ser considerados
como 0 ou 1, falso ou verdadeiro.

Chamada boolean em homenagem a George Boole
"""

# Tipos Boolean: True e False
ok = True
print(type(ok))
print(ok)

ok = False
print(type(ok))
print(ok)

"""
Operadores lógicos:

and (e)
or (ou)
not (negação)

Tabela verdade
Utilizando o "E" (and):
V e V = V
V e F = F
F e V = F
F e F = F
"""
print("AND:")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()
x = 5
print(x>3 and x<10)
print(x>3 and x>10)
print(x<3 and x<10)
print(x<3 and x>10)

print()
"""
Utilizando o "OU" (or):
V e V = V
V e F = V
F e V = V
F e F = F
"""
print("OR:")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print()
x = 5
print(x > 3 or x < 10)
print(x > 3 or x > 10)
print(x < 3 or x < 10)
print(x < 3 or x > 10)

print()
"""
Utilizando a "Negação" (not):
not True = False
not False = True
"""
print("NOT:")
print(not True)
print(not False)

