import random

def SonReciprocos(x, y):
    if x * y == 1:
        return True
    else:
        return False

def main():
    for _ in range(100):
        x = 1 + random.random(1, 100)
        y = 1/x
        if not SonReciprocos(x,y):
            print(x)
            print(y)

if __name__ == "__main__":
    main()

# Algunos números se consideran no recíprocos porque se pierden números significativos que no se pueden guardar, y al multiplicar el resultado queda muy cerca del 1.
# Debería agregar una tolerancia para que no ocurra este error. 