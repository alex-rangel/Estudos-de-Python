"""
Parâmetros de uma função.
"""

def minha_funcao():
    return "Essa é minha função"

retorno = minha_funcao()

print(f"Retorno da minha função: {retorno}")

def minha_funcao2():
    variavel = "Maria"
    return variavel

retorno2 = minha_funcao2()
print(f"Retorno da minha função 2: {retorno2}")
print(f"Retorno diretamente para o print: {minha_funcao2()}")

# A variável "variavel" nada tem a ver com a va variável "variavel"
# que está dentro da função "minha_funcao2()".
variavel = "Ana"
print(variavel)

# Função que lê do teclado e imprime na tela.
def imprime_nome_teclado():
    nome = input("Qual seu nome?")
    print(f"Olá {nome}.")

imprime_nome_teclado()


def nome_da_funcao(parametro): 
    # Parâmetro é o nome dado aos valores utilizados na 
    # definição de uma função.
    # Corpo da função.
    print(f"Olá {parametro}")


# Argmento é o nome dado aos valores utilizados na
# chamada de uma função. 
nome_da_funcao("Juliana")
nome_da_funcao("Pedro")
nome = input("Qual seu nome? ")
nome_da_funcao(nome)


# Reformulando os nomes da função e do parâmetro:
def imprime_nome(nome):
    print(f"Olá {nome}.")

print()
nome = input("Qual seu nome? ")
imprime_nome(nome)

print()
imprime_nome(input("Qual seu nome? "))

print()
# imprime_nome() Dá erro pois preciso passar o mesmo
# número de argumentos definidos pela função.
 

def imprime_nome(nome, sobre_nome):
    print(f"Olá {nome} {sobre_nome}")


imprime_nome("Ana", "Clara")
# imprime_nome("Ana", "Clara", 25) # Aqui também da erro
# por causa da quantidade de argumentos.

imprime_nome("Clara", "Ana")













