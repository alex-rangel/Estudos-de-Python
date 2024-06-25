"""
Jogo Pedra, Papel e Tesoura
"""

# import random # Desta forma, importa todo o módulo random, desnecessariamente.
from random import choice # Assim, importa apenas a função choice de random.

jogador_vitorias = 0
maq_vitorias = 0

def opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador = esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida. Tente novamente.")
        return opcao_jogador() # Recursividade

def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina
    
while True:
    print("--"*15)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("--"*15)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
    or (esc_jogador == "papel") and (esc_maquina == "pedra") \
    or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        # Jogador ganha
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu"
              f" {esc_maquina}. Resultado: Você ganhou!")
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        # Empate
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu"
              f" {esc_maquina}. Resultado: Empate.")
    else:
        # Máquina ganha
        print(f"Jogador escolheu {esc_jogador} e a máquina escolheu"
              f" {esc_maquina}. Resultado: Você perdeu!")
        maq_vitorias += 1
    print("--"*15)
    print(f"Vitórias do jogador: {jogador_vitorias}")
    print(f"Vitórias da máquina: {maq_vitorias}")
    print("--"*15)
    esc_jogador = input("Deseja jogar novamente?")
    esc_jogador = esc_jogador.lower()
    if esc_jogador in ["sim", "s"]:
        pass
    elif esc_jogador in ["não", "n"]:
        break
    else:
        break
