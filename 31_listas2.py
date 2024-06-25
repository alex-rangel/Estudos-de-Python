# index     0       1       2
lista = ["carro","barco","avião"]
print(lista)

for x in lista:
    print(x)

print(len(lista))

# Exibe os índices e os itens:
for x in range(len(lista)):
    print(f"Índice: {x} - Item: {lista[x]}")

texto = "carro,avião"
# Cada caracter passa a ser um elemento da lista:
lista2 = list(texto)
print(lista2)

print(type(texto))
# Split(char): Divide a string ao encontrar o caracter passado
# por parâmetro, retorna uma lista com essa string dividida,
# cada pedaço da string vira um elemento da lista.
texto = texto.split(',')
print(type(texto)) # Texto que era string passa a ser um lista.
print(texto)

texto = "meulogin@gmail.com"
texto = texto.split('@')
print(texto)

nome = "José Silva Santos"
nome = nome.split(" ")
print(nome)

print(f"Nome: {nome[0]}")
print(f"Sobrenome:", end=" ")
for x in range(1,len(nome)):
    print(f"{nome[x]}", end=" ")
print()


# Adicionar elementos no final da lista:
print(nome)
# Ao tentar fazer desta forma abaixo dá erro pois
# estou tentando acessar uma posição inválida da lista
# esta posição não existe.
#nome[3] = "Lima"

# A maneira correta de inserir no final da lista
# é usando a função append:
nome.append("Lima")
print(nome)

lista.append("moto") # Append só aceita um parâmetro.
print(lista)
# Posso passar uma lista, só que o item inserido será uma lista,
# teremos uma lista dentro de outra. Pode não ser este o objetivo.
lista.append(["bicicleta", "navio"])
print(lista)
# A forma correta de inserir mais de um item de uma vez
# é usando a função extend, passando uma lista com os itens
#  a serem inseridos:
nova_lista = ["bicicleta","navio"]
lista.extend(nova_lista)
print(lista)

# Adiciona elemento por índice na lista:
# Ele adiciona, não substitui.
# Não sendo na última posição, ele "empurra"
# todos os outro elementos para trás.
lista.insert(1,"caminhão")
print(lista)

# Remover o último elemento da lista:
lista.pop()
print(lista)

# Remover um elemento da lista pelo indice:
lista.pop(0)
print(lista)
# ou
del lista[0]
print(lista)

# Apaga a lista e a varíável, é como se a variável
# fosse "desdeclarada", podendo gerar erros. 
# del lista
# print(lista) # Dá erro.

# Remover um elemento específico da lista:
lista.remove(["bicicleta", "navio"]) # Removi aquela lista que estava dentro da nossa lista.
print(lista)

lista.remove("barco")
print(lista)

# Ordenar uma lista de forma crescente:
lista.sort()
print(lista)

# Sort também funciona com números:
lista_numeros = [1, 50, 23, 100, 67]
lista_numeros.sort()
print(lista_numeros)

# Sort ordenando de forma decrescente:
lista_numeros.sort(reverse = True)
print(lista_numeros)

# Ainda sobre sort:
lista_nomes = ["Ana","Pedro","Marta","Clarice","beatriz","ana clara"]
print(lista_nomes)
# "beatriz" e "ana clara" são ordenados de forma separada por
# começarem com letra minúscula. 
lista_nomes.sort()
print(lista_nomes)
# Para resolver isso, passamos um parâmetro para o sort:
lista_nomes.sort(key=str.lower) # Converte para minusculo apenas
# para ordenar, não muda o conteúdo das strings.
print(lista_nomes)

# Inverte os elementos da lista,
# independente de ordenação: 
print(lista)
lista.reverse()
print(lista)

# Apagar todos os itens de uma lista:
lista.clear()
print(lista)

# Preencher uma lista com dados:
nomes = []
while True:
    nome = input("Informe um nome:")
    nomes.append(nome)
    opcao = input("Deseja inserir outro nome?(S/N)")
    if opcao in "Nn":
        break
print(nomes)
