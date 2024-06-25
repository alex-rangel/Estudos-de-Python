# Listas são criadas com colchetes
# index     0        1        2
lista = ["item1", "item2", "item3"]
print(lista)
print(len(lista))
print(type(lista))

print("---" * 15)

# Tupla
# index     0       1       2       3       4
tupla = ("item1","item2","item3","item1","item1")
print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])
print(tupla.count("item1")) # Conta a q2uantidade de ocorrências de um item.

# Tupla é imutavel enquanto a lista é mutavel.
# A lista possuimais funções que uma tupla.
# A tupla não possui funções de inserção e remoção pois é imutável.
print(dir(tupla))
print(dir(lista))

lista.append("item4")
print(lista)
# tupla.append("item4") # Dá erro pois tupla não possui este método.

lista[1] = "item5"
print(lista)
print(tupla[1])
# tupla[1] = "item5" # Também dá erro pois tupla é imutável.

# Tupla é como se fosse uma constante.
# Posso reescrever uma pupla.
# Não posso alterar seu conteúdo, mas posso reescrever, como
# se faz com qualquer variável.
# Ex.:
print(tupla)
tupla = ("item6", "item7", "item8")
print(tupla)

# Mas pq uma tupla é imutável?
# Ex.: Temos a situação de uma lista em que foi inserido
# uma UF que não existe, indevidamente.
# Se fosse uma tupla, as UFs seriam cadastradas e não
# seria possivel alterar mais nada, evitando erros.
uf = ["SP", "DF", "GO", "AA"]
uf.append("rj")
print(type(uf))
print(uf)

uf = ("SP", "DF", "GO", "RJ")
print(type(uf))
print(uf)

# Tuplas também podem guardar diferentes tipos dedados:
tupla = (3, 5.8, True, "item")
print(tupla)

# Se tentarmos criar uma tupla com apenas 1 item,
# ela não é definida como uma tupla.
tupla = ("item")
print(type(tupla)) # Aparece definido como string.
# Como fazer então?
tupla = ("item",) # Agora aparece definido como tupla.
# Então na verdade o que define uma tupla é a vírgula e não os
# parênteses. Os parênteses são usados por uma questão de organização,
# de formatação.
print(type(tupla))

# Podemos declarar sem os parênteses, apenas com a vírgula.
tupla = "item",
print(type(tupla))

tupla = "item1", "item2", "item3", "item4"
print(type(tupla))
print(tupla)

# Caso queira realmente alterar os itens de uma tupla,
# como seria? Tem uma forma estratégica!!!
# Converter a tupla em lista, alterar a lista e depois
# criar a tupla novamente.
tupla = "item1", "item2", "item3", "item4"
lista = list(tupla)
print(tupla)
print(lista)
lista.append("item5")
print(lista)
tupla = tuple(lista)
print(tupla)
# Para remover seria a mesma coisa,
# mas poderia usar a função pop da lista.
lista = list(tupla)
lista.pop()
tupla = tuple(lista)
print(tupla)

# Posso apagar uma tupla, assim como em lista
# posso deletar ra tupla, e a variável sera
# "desdeclarada" utlizando o comando del:
del tupla
# print(tupla) # Dá erro pois a variável tupla não existe mais.
