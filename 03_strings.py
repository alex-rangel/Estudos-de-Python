print("Olá")
print('Olá')

w = "Curso de Python3"
print(w)

"""comentário""" #Este bloco não é executado pois essa String
# não está guardada em memória.

# Mas, posso utilizar em blocos, posso guardar um
# uma variável guardando a quebra de linha.
a = """Olá,
este é o curso de Python,
espero que goste."""

print(a)

#Métodos de Strings

b = " Olá Mundo "
print(b)
print(b.strip()) #Strip ignora os espaços de antes ee depois
print(b.lower()) #Minúsculo
print(b.upper()) #Maiúsculo

e = "Olá"
f = "Mundo"
g = e + " " + f # Concatenação de Strings
print(g)

"""
Crie um código com todass as variáveis necesárias para
imprimir utilizando a função print("Lembre-se que deve
ser possível trocar nomes, preços e dados apenas alterando
 os valores das variáveis"):

 Situação 1:
 Gabriel é o cliente de uma livraria online que acaba de 
 comprar 01 livro com título Lógica de Programação por R$79,30
 o vendedor MArcos recebeu uma comissão de R$30,00 pela venda.

 "Olá, (Gabriel) sua compra de (01) qtd do livro
 (Lógica de Programação) por R$(79,30) foi efetuada
 com sucesso!".

 "Olá, (Marcus) você acaba de receber uma comissão de R$(30,00)
 pela compra realizada pelo(a) cliente (Gabriel)".

 Situação 2:
 A autora (Beatriz) publicou um post em um blog sobre
 (redes neurais) e obteve (32) compartilhamentos.

 "Seu post com título (Redes Neurais) gerou (32)
 compartilhamentos".

"""


print("Resolução da situação 1:")
cliente = "Gabriel"
quantidade = "01"
titulo_livro = "Lógica de Programação"
valor = "79,30"

print("Olá, "+cliente+" sua compra de "+quantidade+" qtd do livro "
      +titulo_livro+" por R$ "+valor+" foi efetuada com sucesso!")

vendedor = "Marcus"
comissao = "30,00"

print("Olá, "+vendedor+" você acaba de receber uma comissão de R$ "
      +comissao+" pela compra realizada pelo(a) cliente "+cliente+".")

print()
print("Resolução da situação 2:")
autora = "Beatriz"
titulo = "Redes Neurais"
quant_compart = "32"

print("A autora "+autora+" publicou um post em um blog sobre "
      +titulo+" e obteve "+quant_compart+" compartilhamentos.")

print("Seu post com título "+titulo+" gerou "+quant_compart+" compartilhamentos.")