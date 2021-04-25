import ej1
import ej2
import ej3
import ej4

# Este archivo ejecuta las funciones correspondientes al ejercicio 3 y 4.
# Como el ejercicio 1 y 2 solamente piden escribir la función y no requieren
# usarlas, para corregir esos es mejor leer ej1.py y ej2.py individualmente.
# Los .py de cada ejercicio tienen algunos comentarios que pueden ser útiles.

if __name__ == "__main__":
    print("-- Leer comentarios en el código para más detalles --\n")
    print("* Para puntos iniciales x0 = 10, x1 = -10 *\n")
    ej2.busqueda_ceros(ej3.polinomio, 10.0, -10.0, 1e-6, 15)
    print("\n")
    print("* Para puntos iniciales x0 = -2, x1 = 4 *\n")
    ej4.graficar()
    