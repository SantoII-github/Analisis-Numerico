import math

def imprimir_menor(num1, num2):
    if num1 < num2:
        print(f"El número más chico es: {num1}")
    elif num1 > num2:
        print(f"El número más chico es: {num2}")
    elif num1 == num2:
        print('Los números son iguales')
    else:
        print('No sé como llegaste a este mensaje de error.')

def main():
    print('Ingrese dos números reales')
    x = float(input())
    y = float(input())

    imprimir_menor(x, y)

if __name__ == '__main__':
    main()