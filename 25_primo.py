"""
Descobrir se um número é primo.
"""
numero = int(input("Informe um número:"))

# Com for:
if numero > 1:
    for x in range(2, numero):
        if numero % x == 0:
            print("Esse número NÃO é primo.")
            break
    else:
        print("Esse número É primo.")
else:
    print("Esse número não é primo, número menor ou igual a 1.")

# Com while:
if numero > 1:
    i = 2
    while i<numero:
        if numero % i == 0:
            print("Esse número NÃO é primo.")
            break
        i = i + 1
    else:
        print("Esse número É primo.")
else:
    print("Esse número não é primo, número menor ou igual a 1.")