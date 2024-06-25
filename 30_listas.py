"""
Listas:
São utilizadas como vetores, são iteráveis como strings,
possuem índice começando do zero.
"""

lista = ["Chicago", "Queens", "Salvador", "Pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

# Concatenar listas:
lista2 = lista2 + lista3
print(lista2)

lista4 = [True, False]
print(lista4)

lista5 = [True, "Chicago", 2.5, False, 4]
print(lista5)

print(type(lista5))

print(lista5[1])
print(lista5[-1]) # Imprime o último elemento.
print(lista5[-2])
print(lista5[-3])
print(lista5[-4])
print(lista5[-5])
# Estes 2 comandos dão erro pois tenta ler um
# elemento fora do range da lista, inexistente.
# Dá erro -> IndexError: list index out of range
#print(lista5[-6])
#print(lista5[5])

# Técnica de Slicing:
print("Slicing:")
print(lista5[::]) # Imprime tudo.
print(lista5[1:]) # Imprime do índice 1 até o fim.
print(lista5[2:]) # Imprime do índice 2 até o fim.
print(lista5[:3]) # Imprime do começo até o índice 3-1.
print(lista5[:4]) # Imprime do começo até o índice 4-1.
print(lista5[1:4]) # Imprime do índice 1 até o índice 4-1.
print(lista5[1:5:2]) # Imprime do índice 1 até o índice 5-1, de 2 em 2.

# Slicing também funciona com strings.
nome = "Terra"
print(nome[::])
print(nome[2:4])

# Tamanho de listas:
lista1 = [2.0, 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

# index      0       1       2
lista3 = ["Nome", "Nome2", "Nome"]

# Comando len retorna a quantidade de elementos de uma lista.
print(len(lista1))
print(len(lista2))
print(len(lista3))

# Funções que só podem ser utilizadas com
# tipos de dados numéricos:
print(sum(lista1)) # Soma os elementos da lista.
print(max(lista1)) # Retorna o maior elemento da lista.
print(min(lista1)) # Retorna o menor elemento da lista.

# Converter uma string e um range em lista:
nome = "Curso de Python"
valor = range(10)
print(nome)
print(valor)

lista6 = list(range(10))
print(lista6)

lista7 = list("Curso de Python")
print(lista7)

elemento = 8
if elemento in lista6:
    print("Este elemento está na lista.")

# Mudando ítens da lista:
# index     0         1          2         3         4          5
lista8 = ["Gato", "Cachorro", "Peixe", "Cavalo", "Tubarão", "Girafa"]
print(lista8)

print(type(lista8))
print(lista8[1])

lista8[1] = "Cavalo"
print(lista8)

# Mudando itens com Slicing:
lista8[1:4] = ["Águia", "Morcego", "Elefante"]
print(lista8)

# O que acontece se passarmos mais valores
# do que foi definido no intervalo de Slicing?
lista8[1:2] = ["Vaca", "Rato"]
print(lista8)
# Definimos 1 item no intervalo e passamos 2 itens.
# O primeiro item é adicionado na posição definida pelo intervalo.
# O segundo item, é adicionado na próxima posição,
# empurrando todos os outros itens da lista para trás.

print(lista8[1])
print(lista8[2])
print(lista8[3])

# O que acontece se passarmos menos valores
# do que foi definido no intervalo de Slicing?
lista8[1:5] = ["Esquilo"]
print(lista8)
# Definimos 4 itens no intervalo e passamos 1 item.
# O item é adinionado na primeira posição definida pelo intervalo de Slicing.
# Todas as outra posições do intervalo são removidas,
# empurrando todos os outros itens da lista para frente.
# Ele faz uma substituição.
