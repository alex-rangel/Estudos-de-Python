idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("MENOR")
elif idade >= 16 and idade < 18:
    print("EMANCIPADO")
elif idade >= 18 and idade < 65:
    print("ADUTO")
else:
    print("IDOSO")