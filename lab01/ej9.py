# coeficientes = [1, 2, 3] ---> x^2 + 2x + 3
def horn(valor, coeficientes):
    n = len(coeficientes)
    b = coeficientes[0]

    for i in range (1, n):
        b = coeficientes[i] + b * valor
    
    return b

def main():
    coeficientes = [1, 2, 3]
    res = horn(1, coeficientes)
    print(str(res))

if __name__ == '__main__':
    main()