def potencia_enesima(x, n):
    return x**n


def main():
    print('Ingrese un real')
    x = float(input())

    for i in range(6):
        print(f"La potencia {i}-ésima de {x} es: {potencia_enesima(x, i)}")

if __name__ == '__main__':
    main()