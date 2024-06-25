"""
continue: Utilizado em loops para encerar uma única
iteração do laço. Ele não encerra o laço. 
"""
print("For:")
for x in range(10):
    if x == 3:
        continue
    print(x)
print(f"Valor de x após sair do for: {x}")

print("While:")
i = -1
while i<9:
    i = i + 1
    if i == 3:
        continue
    print(i)

print("While 2:")# Não muito eficiente pois repete linha de código.
i = 0
while i<10:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1

"""
Pass: Usado em estruturas,
quando a estrutura não tem nenhuma linha de código,
ocorre em python, erro de identação, então usa-se
o pass para retirar o erro.
Muito cuidado ao usar o pass.
"""
if x != 9:
    pass  
else:
    print("Caiu no else!!!")
print("Fim do programa.")