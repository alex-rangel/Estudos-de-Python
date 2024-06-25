"""
Listas: Coleções ordenadas, mutáveis e que permite valores duplicados.
Tuplas: Coleções ordenadas, imutáveis e que peremite valores duplicados.
Dicionários: Coleções não ordenadas, mutáveis e que não permite valores duplicados (para chaves).
Sets: Coeções não ordenadas, mutável e que não permite valores duplicados.
"""
# Os sets também são conhecidos como conjuntos.

# Assim como dicionários, sets também usam chaves para definir seus itens,
# a diferença é que os sets não usam chave-valor, apenas os itens,
# as chaves são os próprios valores.  
conjunto = {"item1", "item2", "item3"}
print(type(conjunto))
print(conjunto) # A ordem de exibição é aleatória, pode ser a mesma ou não.
print(len(conjunto))

# Não permite valores duplicados:
conjunto = {"item1", "item2", "item3", "item1", "item2", "item3"}
print(conjunto) # Continua imprimindo apenas 3 itens.
print(len(conjunto)) # O tamanho continua com 3 itens.

# Também permite tipos diferentes dedados:
conjunto = {"item1", 3, True, 4.7, "Rio de Janeiro"}
print(conjunto)
print(len(conjunto))

# Também possui construtor:
tupla = (3, 7, 9, 5)
print(tupla)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))
# Posso passar valores em vez de uma variável para o set(),
# atenção aos parênteses:
conjunto = set((3, 7, 9, 5))
print(conjunto)
print(type(conjunto))

conjunto = {3, 7, 9, 5}
# print(conjunto[0]) # Dá erro, sets não possuem índice.
# print(conjunto["item1"]) # Dá erro pois sets não possuem chave-valor.
# conjunto[0] = 4 # Também da erro, pois como dito acima, sets não possuem índice.

# Como acessar os ítens de sets?
conj = {"item1", "item2", "item3", "item4", "item5"}
for x in conj:
    print(x)

# Verificar se um ítem pertence ao conjunto:
conjunto = {4, 6, 8, 9, 1, "item"}
print(6 in conjunto)
print(11 in conjunto)
print("item" in conjunto)
print("item2" in conjunto)

conj = {2, 4, 7, 8}
print(dir(conj))

# Adicionar com a função add:
set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item4")
print(set1)
set1.add(8)
set1.add(True)
print(set1)

# Adicionar com a função update:
set1 = {4, 5, 7, 8, 9, 1}
set2 = {"item3", "item5", "item1"}
set1.update(set2)
print(set1)
# Ou (atenção as chaves):
set1 = {4, 5, 7, 8, 9, 1}
set1.update({"item1","item2","item3"})
print(set1)

# Posso passar uma LISTA para a função update:
set1 = {4, 5, 7, 8, 9, 1}
set1.update([3, 4, 5, 7, 8, 9, 1, "item3","item5","item1"])
# Perceba que só foram adicionados os itens que não existiam no conjunto.
print(set1)

# Posso passar uma TUPLA para a função update:
set1 = {4, 5, 7, 8, 9, 1}
set1.update((3, 4, 5, 7, 8, 9, 1, "item3", "item5", "item1"))
# Perceba que só foram adicionados os itens que não existiam no conjunto.
print(set1)

# Removendo elementos de um conjunto (set):
set1 = {3, 4, 5, 7, 8, 9, 1, "item3", "item5", "item1"}
print(set1)

# Função remove:
set1.remove("item5") # Remover um ítem específico.
print(set1)

# Função discard:
set1.discard("item3") # Também remove um ítem específico.
print(set1)

# A diferença entre o remove e o discard é que ao tentar 
# remover um item que não exista, a função remove retorna
# erro, já a função discard não:
# set1.remove("item9")
# print(set1)
# set1.discard("item9")
# print(set1)

# Apaga todos os itens do set:
set1.clear()
print(set1)

# "Desdeclara" a variável set1:
del set1
# print(set1) # Dá erro pois a variável set1 não existe mais.
