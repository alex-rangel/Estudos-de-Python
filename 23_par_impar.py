"""
Descobrir se o número é par ou ímpar,
solicitando um número ou apenas ENTER para sair.
"""
while True:
    entrada = input("Informe um número ou ENTER para sair.")
    
    if entrada == "":
        print("Fim do programa.")
        break
    else:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
            