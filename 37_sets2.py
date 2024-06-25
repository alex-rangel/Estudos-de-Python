"""
Funções de teoria de conjuntos com sets.
"""

conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

# Unir conjuntos:
conjunto3 = conjunto1.union(conjunto2)
# Union retorna um novo conjunto, guardamos em conjunto3:
print(conjunto3)
print(conjunto1) # Conjunto1 não sofreu alteraçao.
print(conjunto2) # Conjunto2 também não sofreu alteraçao.
# Obs.: Poderia utilizar a função update, a diferença é que com
# update não seria necessário criar um terceiro conjunto. 
conjunto1.update(conjunto2)
print(conjunto1)

# Intercessão de conjuntos:
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)
print(conjunto1)
print(conjunto2)
# Caso não queira criar um terceiro conjunto, podemos
# utilizar a função intersection_update(), ex.: 
conjunto1.intersection_update(conjunto2)
print(conjunto1)

# Diferença de conjuntos:
# Une os conjuntos e remove a intercessão:
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)
print(conjunto1)
print(conjunto2)
# Caso não queira criar um terceiro conjunto, podemos
# utilizar a função symmetric_difference_update(), ex.: 
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

"""
Implemente um programa em python, utilizando set, que crie
2 conjuntos e armazene dados informados pelo usuário,
o programa deve perguntar ao usuário se deseja inserir
mais dados a cada nova inserção. Ao final deve ser
gerado um relatório exibindo os elementos de cada conjunto,
a união, intercessão e a diferença deles.
"""
# Dica de como criar um conjunto (set) vazio :
d = set()
print(type(d))
print(d)

# Resolução:
print()
print("-->> Sistema de Conjuntos <<--")
print()
conjunto1 = set()
conjunto2 = set()
print("Armazenar dados do conjunto 1:")
while True:
    item = input("Informe o item: ")
    conjunto1.add(item)
    opcao = input("Deseja inserir outro item ao conjunto 1?(S/N)")
    if opcao in "Nn":
        break
print()
print("Armazenar dados do conjunto 2:")
while True:
    item = input("Informe o item: ")
    conjunto2.add(item)
    opcao = input("Deseja inserir outro item ao conjunto 2?(S/N)")
    if opcao in "Nn":
        break
print()
print("-->> Relatório de Conjuntos <<--")
print()
print("--Elementos do conjunto 1:")
for x in conjunto1:
    print(f"Item: {x}")
print()
print("--Elementos do conjunto 2:")
for x in conjunto2:
    print(f"Item: {x}")

print()
conjunto3 = conjunto1.union(conjunto2)
print(f"--União dos conjuntos: {conjunto3}")

print()
conjunto3 = conjunto1.intersection(conjunto2)
print(f"--Intercessão dos conjuntos: {conjunto3}")

print()
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(f"Diferença dos conjuntos: {conjunto3}")
