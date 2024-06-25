# Concatenando tuplas:
tupla = ("item1",)
tupla2 = ("a", "b")

tupla3 = tupla + tupla2
print(tupla3)

tupla3 = tupla * 3
print(tupla3)

# Percorrendo uma tupla:
tupla = ("item1", "item2", "item3")
print(tupla)
for x in tupla:
    print(x)

# Exibindo os índices com seus respectivos itens:
for x in range(len(tupla)):
    print(f"{x} - {tupla[x]}")

# Empacotar é atribuir itens a uma tupla ou lista.
tupla = ("item1", "item2", "item3")

# Desempacotando itens de uma tupla:
# Desempacotar é obter os itens da tupla ou lista.
# Desta forma, tenho que saber a quantidade de itens:
(x, y, z) = tupla
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Desta forma, x recebe o primeiro item,
# y recebe todos os restantes em forma de lista.
(x, *y) = tupla # ("item1", "item2", "item3")
print(f"x: {x}")
print(f"y: {y}")

tupla = ("item1","item2","item3","item4","item5")
# Desta forma x recebe o primeiro item, z recebe o último
# e y todos os restantes em forma de lista.
(x, *y, z) = tupla
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# Desta forma x recebe o primeiro item, a recebe o último,
# z recebe o penúltimo e y todos os restantes em forma de lista.
(x, *y, z, a) = tupla
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
print(f"a: {a}")

# Desta forma a recebe o último, z recebe o penúltimo 
# e y todos os restantes em forma de lista.
(*y, z, a) = tupla
print(f"y: {y}")
print(f"z: {z}")
print(f"a: {a}")

# Tudo isso também vale para listas:
lista = ["itemLista1", "itemLista2", "itemLista3", "itemLista4", "itemLista5"]
(x, *y, z) = lista
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
