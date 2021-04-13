import math

# Inciso a:

fact6 = 1
for n in range(1,7):
    fact6 = fact6 * n
    print(f"6! = {fact6}")


# Inciso b:
print(str(math.factorial(6)))

# Inciso c:

def factn(n):
    res = math.factorial(n)
    print('El factorial de n es: ' + str(res))
    return res