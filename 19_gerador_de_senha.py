"""
O usuário irá incerir uma chave e
o programa irá gerar uma senha.
Ex.:
Chave: Security
Senha: 5ecur1ty
"""

chave = input("Digite a base da sua senha:")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "1"
    elif letra in "Bb":
        senha = senha + "@"
    elif letra in "Cc":
        senha = senha + "2"
    elif letra in "Dd":
        senha = senha + "3"
    elif letra in "Ee":
        senha = senha + "4"
    elif letra in "Ff":
        senha = senha + "5"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    else:
        senha = senha + letra
        
print(f"Senha gerada: {senha}")