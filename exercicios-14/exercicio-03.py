v = input("Informe o valor do produto: ")
preco = int(v)
d = input("Informe o valor do desconto que o produto terá: ")
desconto = float(d)

valor_final = preco - ((preco*desconto)/100)

print(f"O valor do produto com o desconsto de {desconto}% será de: R${valor_final}")