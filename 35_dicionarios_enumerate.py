"""
Listas: Coleções ordenadas, mutável e que permite valores duplicados.
Tuplas: Coleções ordenadas, imutável, e que permite valores duplicados.
Dicionários: Coleções não ordenadas, mutável e que não permite valores duplicados.
"""
# Relembrando:
# index     0       1       2  Aceita valores repetidos pq utiliza indices:
lista = ["item2","item3","item2"]
tupla = ("item2","item3","item2")

# Os itens de um dicionário são compostos pela dupla chave-valor:
dicio = {"chave1":"Gabriel", "chave2":1993, "chave3":True}
print(dicio)
dicio = {"nome":"Gabriel", "ano_nascimento":1993, "habilitado":True}
print(dicio)

# Posso declarar um dicionário com quebra de linha:
dicionario = {
    "nome":"Bruna",
    "idade":27,
    "nacionalidade":"brasileira"
    # "idade":35 # Não posso ter chaves repetidas,
                 # Se tiver ele mantem o valor da última.
}
print(dicionario)

# Acessando os itens do dicionário:
print(dicionario["nome"])
print(dicionario["idade"])
print(dicionario["nacionalidade"])
# Ou através da função get:
print(dicionario.get("nome"))
print(dicionario.get("idade"))
print(dicionario.get("nacionalidade"))

print(dir(dicionario)) # Para ver os métodos disponíveis para dicionários.
print()
print(dicionario.keys()) # Retorna todas as chaves do dicionário.
print()
print(len(dicionario)) # Retorna o tamanho do dicionário.
print()
print(dicionario.values()) # Retorna todos os valores do dicionário.

# Verificar se uma chave existe no dicionário:
if "idade" in dicionario:
    print(f"A chave idade existe: {dicionario["idade"]}")
else:
    print("A chave idade não existe.")

if "salario" in dicionario:
    print(f"A chave salário existe: {dicionario["salario"]}")
else:
    print("A chave salário não existe.")

# Retorna uma lista de tuplas, com cada item do dicionário
# em forma de tupla.
print(dicionario.items())
lista = dicionario.items()
print(lista)
# Desempacotando a lista de tuplas:
(x, y, z) = lista
print(x)
print(y)
print(z)
# Desempacotando as tuplas com cada par chave / valor:
(chave, valor) = x
print(chave)
print(valor)
(chave, valor) = y
print(chave)
print(valor)
(chave, valor) = z
print(chave)
print(valor)

# Modificar valores do dicionário:
dicio = {"nome":"Gabriel", "ano":1993, "valor_logico": True}
print(dicio)
dicio["nome"] = "Pedro"
print(dicio)
# Ou
dicio.update({"nome": "Ana"})
print(dicio)

# Criar uma nova chave:
# Passo uma chave que ainda não existe, ele cria esta nova chave:
dicio["idade"] = 32
print(dicio)
# Ou
# Também passo uma chave que não existe:
dicio.update({"estado":"Rio de Janeiro"})
print(dicio)

# Remover uma chave (item):
# Obs sobre o popitem: A função elimina o último item da versão 3.7 e acima,
# nas outras versões (abaixo de 3.7) essa função elimina um item aleatório.
dicio.popitem() # Remove o último item.
print(dicio)

dicio.pop("nome") # Remove um item específico.
print(dicio)

del dicio["ano"] # Também remove um item específico.
print(dicio)

# del dicio
# print(dicio) # Dá erro pois como visto anteriormente,
               # a variável foi "desdeclarada".

dicio.clear() # Remove todos os itens do dicionário.
print(dicio)

dados = {"nome":"Gabriel","ano":1993,"valor_logico":True,"estado":"Rio de Janeiro"}
print(dados)

# Loop com dicionário:
# Imprime somente as chaves:
for x in dados:
    print(x)
# Ou
print()
for x in dados.keys():
    print(x)

print()
# Imprime somente os valores:
for x in dados.keys():
    print(dados[x])
# Ou
print()
for x in dados:
    print(dados[x])
# Ou
print()
for x in dados.values():
    print(x)

# Imprime chave-valor do dicionário:
print(dados.items())
# Desta forma percorremos o dicionário e obtemos cada um de sues
# itens em forma de tupla: 
for x in dados.items():
    print(x)
    print(type(x))

print()
# Desta forma recebemos cada item do dicionário em forma de tupla,
# desempacotamos cada tupla e obtemos as chaves e os valores diretamente. 
# A variável x recebe a chave e a variável y recebe o valor:
for x,y in dados.items():
    print(f"Chave: {x} - Valor: {y}")

# Criar uma cópia de dicionário, copiar os conteúdos para outro
# dicionário, não copiar a referência.
dicio = dados.copy()
print(dicio) 
# Ou
dicio2 = dict(dados)
print(dicio2)

print()
dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)


# Função fromkeys:
# index     0        1        2
tupla = ("item1", "item2", "item3")

# dicio = dict(tupla) # Dá erro pois tupla não possui chave-valor.
# Como fazer então?
# Usando fromkeys. Ele cria o dicionário utilizando os ítens da tupla
# como chave e os valores são preenchidos com nulo (None).
# Obs.: Nome em python é nulo.
dicio = dict.fromkeys(tupla)
print(dicio)

# Posso criar uma variável e passar como parâmetro ao fromkeys, para
# preencher todos os valores.
x = 0
dicio = dict.fromkeys(tupla, x)
print(dicio)

# Posso passar como parâmeto uma outra tupla para preencher todos os valores,
# cada valor receberá a mesma tupla completa. 
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)

# Alinhamento de dicionários.
# Posso ter dicionários dentro de outros dicionários.

#Dicionário comum:
dados = {
    "nome":"Gabriel",
    "ano":1993,
    "valor_logico":True
}

# Dicionário dom outros dicionários como chave-valor:
dicio = {
    "dicio1":{
        "nome":"Ana",
        "idade":25
    },
    "dicio2":{
        "nome":"Pedro",
        "idade":38,
        "dicio3":{
            "nome":"Ana Julia",
            "idade":5
        }
    }
}
print(dicio)

"""
Enumerate:
"""
"""
print()
print("-->>Enumerate:")
frutas = ["maçã", "banana", "cereja", "damasco"]

# Enumerate retorna uma tupla contendo 2 itens, são eles o índie to item 
# e o valor do item:
for x in enumerate(frutas):
    print(type(x))
    print(x)

# Desempacotando cada tupla retornada pelo enumerate:
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice} - Fruta: {fruta}")
print()

# Posso especificar um índice inicial para o enumerate começar
# a contagem dos índices, em vez do zero:
for indice, fruta in enumerate(frutas, start=1):
    print(f"Índice: {indice} - Fruta: {fruta}")

# Exemplo com uma lista de tuplas:
pessoas = [("Alice",25), ("Luiz", 30), ("Maria", 10)]

print()
# Usanto enumerate e desempacotando os índices, os nomes e as idades:
for indice, (nome, idade) in enumerate(pessoas):
    print(f"Índice: {indice} - Nome: {nome} - Idade: {idade}")

# Enumerate com dicionários:
print()
dados = {"nome":"Gabriel","ano":1993,"valor_logico":True,"estado":"Rio de Janeiro"}

# Imprimindo índices e chaves do dicionário:
for indice, chave in enumerate(dados):
    print(f"Índice: {indice} - Chave: {chave}")
# Ou
for indice, chave in enumerate(dados.keys()):
    print(f"Índice: {indice} - Chave: {chave}")

print()
# Imprimindo índices e valores do dicionário:
for indice, valor in enumerate(dados.values()):
    print(f"Índice: {indice} - Valor: {valor}")

print()
# Imprimindo índices, chaves e valores:
for indice, (chave, valor) in enumerate(dados.items()):
    print(f"Índice: {indice} - Chave: {chave} - Valor: {valor}")

print()
# Imprimindo índices, chaves e valores e definindo 1 como valor inicial::
for indice, (chave, valor) in enumerate(dados.items(), start=1):
    print(f"Índice: {indice} - Chave: {chave} - Valor: {valor}")
"""
"""
Fim do enumerate.
"""
