"""Escopo de variáveis"""

"""
Variáveis globais - declaradas fora de qualquer bloco de funções.

Variáveis locais - declaradas dentro de algum bloco de funções,
só existem enquanto a função estiver executando.
"""

x = 5

def funcao():
    x = 3
    print("Valor da variável local: ",x)

funcao()
print("Valor da variável global: ",x)

# Prática ruim para nomes de variáveis:
y = 'Gabriel'
z = 1.74
t = "111.222.333-44"
l = 23

# Boa prática para nomes de variáveis:
nome = 'Gabriel'
altura = 1.74
cpf = "111.222.333-44"
idade = 23
