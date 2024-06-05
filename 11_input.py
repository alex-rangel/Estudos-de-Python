"""
Função input() - Função para receber dados
do usuário, entrada de dados.
"""

# 1ª Forma de exibição:
print("Qual é o seu nome?")
nome = input()
print("Olá, "+nome)
# Ou
print("Olá,",nome)

idade = input("Qual sua idade?")
print("Idade:",idade)

# 2ª Forma de exibição:
nome2 = input("Qual é o seu nome?")
idade2 = input("Qual é a sua idade?")
print("Seu nome é: {0} e sua idade é: {1}".format(nome2, idade2))

# 3ª Forma de exibição:
nome3 = input("Qual é o seu nome?")
idade3 = input("Qual é a sua idade?")
print(f"Seu nome é: {nome3} e sua idade é: {idade3}")
