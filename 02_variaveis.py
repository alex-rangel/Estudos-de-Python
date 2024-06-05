# Não preciso declarar o tipo de variáveis para usar
# pois Python tem tipagem dinâmica.

x = 5
y = 3.5
z = 1+2j

w = "Ana"
w = 'Ana'

#Variáveis devem começar com letra ou _, não pode começar
#com número
# De A-z, _, de 0-9
# altura, Altura e ALTURA são diferentes

h, j, l = 1, 3, 5
print(h)
print(j)
print(l)

a = b = c = " faz o curso de Python3"
print(a)
print(b)
print(c)

h = w + a # "+" concatena
print(h)

l = x + j
print(l)

l = w + x
print(l) #dá erro, não posso concatenar texto com número em python,
# pois python tem tipagem forte.
#Python é tipagem dinâmica e forte.
#Tipagem dinâmica pois as variáveis mudam de tipo conforme
# são usadas, podem mmudar seu tipo.
#Tipagem forte pois não fazx a conversão de tipo,
# como por exemplo, para concatenar.
