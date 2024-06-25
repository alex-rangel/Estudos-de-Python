"""
Função é um bloco de comandos criado com o intuito de 
realizar uma tarefa específica e muito bem definida.
"""
# Bloco externo
nome = "Gabriel" # Variável global


def minha_funcao():
    # Bloco interno da função,
    # também conhecida como corpo da função.
    nome = "Ana"
    print(nome)
    tupla = 2, 5, 6, 7, 9
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if.")
    for x in tupla:
        print(x)


minha_funcao()
print(nome)
minha_funcao()

# Retorno de uma funçao:
lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop() # Pop remove e retorna o último item da lista.
print(lista)
print(f"Retorno da função pop: {retorno}")

var1 = print("Olá mundo!!!")
print(var1) # A função print retorna None, ou seja, nada, nulo.

def ola_mundo():
    return "Olá mundo!!!"

retorno = ola_mundo()
print(retorno)
# Ou
print(ola_mundo())

# Não posso ter uma função sem nada, dá erro, ex.:
# def teste():
# Como resolver?
# Usando o pass:
def teste():
    pass


def par_impar():
    numero = 4
    if (numero % 2) == 0:
        return "Número par"
    return "Número ímpar" # Esta linha só é executada se o
                          # return da linha anterior não
                          # for executado.

print(par_impar())

x = 0
if x == 0:
    print("Entrei no if.")
print("Seguindo o fluxo.") # Aqui é executado pois não possui
                           # return nem é uma função.

print("Olá mundo")
print(par_impar())
print("Olá mundo novamente")
