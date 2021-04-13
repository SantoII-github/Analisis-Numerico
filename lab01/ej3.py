import math

x = 2.0
i = 1

while not math.isinf(x*2):
    x = x*2
    i = i + 1

print('La mayor potencia de 2 no infinita en python es: ' + str(x))
print('Su exponente es: ' + str(i))

y = 2.0
i = 1
while y/2 != 0:
    y = y/2
    i = i - 1

print('El menor número positivo en punto flotante en python es: ' + str(y))
print('Su exponente es: ' + str(i))