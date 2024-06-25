lista = ["a","b","c"]
lista2 = [1, 4, 6]

# Concatenando listas (já visto):
lista3 = lista + lista2
print(lista3)
# Ou:
lista.extend(lista2)
print(lista)
# Ou, de forma lógica:
for x in lista2:
    lista.append(x)
print(lista)

# Copiar uma lista para outra lista:
lista_letras = ["a","b","c"]
print(lista_letras)
# Aqui faço uma cópia da referência e não da lista
lista_letras2 = lista_letras
print(lista_letras2)
lista_letras2.append("d")
print(lista_letras2)
print(lista_letras)
lista_letras.append("e")
print(lista_letras)
print(lista_letras2)

# Aqui faço cópia da lista e não da referência:
lista_letras_copia = []
for x in lista_letras:
   lista_letras_copia.append(x)
# Ou
# lista_letras_copia.extend(lista_letras)
print("Lista_letras:")
print(lista_letras)
print("Lista_letras_copia:")
print(lista_letras_copia)
lista_letras_copia.append("z")
print("Lista_letras:")
print(lista_letras)
print("Lista_letras_copia:")
print(lista_letras_copia)

# Existe uma função própria para copiar uma lista:
# Para fazer uma cópia dos itens e não copiar a referência:
lista_letras_copia = lista_letras.copy()
lista_letras_copia.append("f")
lista_letras.append("g")
print(lista_letras)
print(lista_letras_copia)

"""
Implemente um programa de cadastro de funcionários que guarde
os nomes e salários dos funcionários em listas. A matrícula do
funcionário será seu índice da lista +1.
Ao final, deverá apresentar um relatório das matrículas, nomes
e salários como também qual o maior e menor salário e a méria
salarial dos funcionários.
"""

print()
nomes = []
salarios = []
while True:
    print("Cadastro de funcionários:")
    nome = input("Informe o nome:")
    salario = float(input("Informe o salário:"))
    nomes.append(nome)
    salarios.append(salario)
    opcao = input("Deseja cadastrar outro funcionário?(S/N)")
    if opcao in "Nn":
        break
print()
print("--Relatório de funcionários--")
for x in range(len(nomes)):
    print(f"Matricula: {x+1}")
    print(f"Nome: {nomes[x]}")
    print(f"Salário: {salarios[x]}")
    print()
print("--Dados estatísticos--")
print(f"Maior salário: {max(salarios)}")
for x in range(len(salarios)):
    if max(salarios) == salarios[x]:
        print(f"---Funcionário: {nomes[x]}")
print(f"Menor salário: {min(salarios)}")
for x in range(len(salarios)):
    if min(salarios) == salarios[x]:
        print(f"---Funcionário: {nomes[x]}")
print(f"Média salarial: {sum(salarios) / len(salarios)}")
