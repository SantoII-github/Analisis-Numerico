import numpy as np
import ej1

def periodo(alpha_rad, theta):
    denominador = np.sqrt(1 - np.sin(alpha_rad / 2)**2 * np.sin(theta)**2)
    return 1 / denominador

def pendulo(l, alpha):
    if alpha < 0 or alpha > 90:
        printf("Alpha debe estar entre 0 y 90")

    alpha_rad = alpha * np.pi/180
    fun_periodo = lambda theta : periodo(alpha_rad, theta)

    integral = ej1.intenumcomp(fun_periodo, 0, np.pi/2, 2**10, "simpson")
    periodo_final = 4 * np.sqrt(l/9.8) * integral

    print(f"El periodo del péndulo es {periodo_final}")
    return periodo_final

# En el caso de alpha = 0, el péndulo está quieto y
# no tiene sentido perdir el período

if __name__ == "__main__":
    pendulo(10, 15)