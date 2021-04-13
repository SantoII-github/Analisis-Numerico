def SonOrtogonales(x, y):
    if x[0] * y[0] + x[1] * y[1] == 0:
        return True
    else:
        return False

def main():
    x = [1, 1.1024074512658109]
    y = [-1, 1/x[1]]
    if not SonOrtogonales(x,y):
        print("Algo salió mal...")

if __name__ == '__main__':
    main()

# Hay un error de redondeo al calcular 1/x[1], ya que no se pueden almacenar todos los dígitos en memoria. Por tanto, debería agregar una tolerancia para tener en cuenta estos casos.