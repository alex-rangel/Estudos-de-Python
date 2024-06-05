# int - Forçar a conversão para inteiro

x = 2
y = 2.8
z = '2'

print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

x = int(2)
y = int(2.8) # Aqui perdeu a casa decimal, perdeu a precisão.
z = int('2')

print(x, y, z)
print(type(x))
print(type(y))
print(type(z))

# float - Forçar conversão para float
a = float(2.3)
b = float(2)
c = float('2.3')
d = float('2')
print(a, b, c, d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# str - Forçar a conversão para string
t = 's1'
r = 2
z = 2.3
print(type(t))
print(type(r))
print(type(z))

t = str('s1')
r = str(2)
z = str(2.3)
print(t, r, z)
print(type(t))
print(type(r))
print(type(z))