"""
Exercício - Verificar se um número
é positivo, negativo ou nulo.
Ao encontrar o valor nulo (0), sai do programa.

Escolha qual laço deseja usar (while ou for).
"""

numero = 1

while numero != 0:
    numero = int(input("Informe um número:"))
    if numero > 0:
        print(f"{numero} é positivo.")
    elif numero < 0:
        print(f"{numero} é negativo")
    else:
        print(f"{numero} é nulo.")
print("Fim do programa.")