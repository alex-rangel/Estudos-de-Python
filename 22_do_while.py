"""
do while - não vem imbutido no Python.

Código para adivinhar um número.
"""

palpite = 0
numero = 9

while palpite != numero:
    palpite = int(input("Qual o número correto?"))
print("Parabéns, você acertou.")

# Melhorando o código:
palpite = 0
numero = 9

# Para criar um loop que se comporte como o DO WHILE,
# devemos utilizar um "while ture" em conjunto com um
# "if break".
while True:
    palpite = int(input("Qual o número correto?"))
    if palpite == numero:
        print("Parabéns, você acertou.")
        break
    else:
        print("Você errou.")


# Outra maneira de fazer, se digitar zero ele sai do loop:

# Em python existe um método chamado bool()
# que retorna o resultado de uma sentença lógica.
# Retorna verdadeiro para qq valor não vazio
# e/ou não zero.
# Retorna falso para 0 e/ou vazio.
print(bool(3 > 0))
print(bool(3 < 0))
print(bool(3))
print(bool(0))
print(bool(""))
print(bool())
print(bool("abc"))
print(bool(99))

palpite = 1
numero = 9

while bool(palpite):
    palpite = int(input("Qual o número correto ou ZERO para sair?"))
    if palpite == numero:
        print("Parabéns, você acertou.")
        break
    else:
        print("Você errou.")
              
