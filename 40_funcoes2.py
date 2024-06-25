def ola_mundo():
    print("Olá mundo!!!")
    # ola_mundo() # Esta chamada de ola_mundo() recursivamente,
                  # causa um loop infinito. Cuidado.

ola_mundo()

# Normalmente, nome de funções possuem verbo.
def executar():
    print("Início de executar.")
    # Posso chamar uma função dentro de outra.
    ola_mundo()
    print("Fim de executar.")

executar()
print("Fim do programa.")
