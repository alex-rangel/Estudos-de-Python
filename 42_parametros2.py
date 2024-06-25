"""
Argumentos nomeados.
"""

def imprimir_nome(nome, sobre_nome, idade):
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobre_nome}")
    print(f"Idade: {idade}")

imprimir_nome("Maria", "Silva", 20)
# Aqui imprime os valores todos trocados por causa da ordem
# em que os argumentos estão sendo passados para a função.
imprimir_nome("Silva", 20, "Maria")
# Podemos resolver isso chamando os nomes dos parâmetros e
# atribuindo valores. Desta forma os valores sendo passados
# fora da ordem, serão passados para seus respectivos
# par?âmetros corretamente. Ex.:
imprimir_nome(sobre_nome="Silva", idade=20, nome="Maria")
# Ou
sobre_nome = "Silva"
idade = 30
nome = "João"
imprimir_nome(sobre_nome=sobre_nome, idade=idade, nome=nome)
