"""Diagrama de Tauc."""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


def func(x, a, b):
    """Regresión lineal."""
    return a*x + b


n2 = [1.24E+08, 3.53E+07, 5.35E+06, 7.56E+05, 1.27E+05, 1.29E+04, 1.57E+03,
      6.76E+02, 5.82E+02, 3.63E+02, 7.45E+01]
# los valores para n = 2
n1 = [105.4784781, 77.08248343, 48.09700144, 29.48409406, 18.88202807,
      10.65626929, 6.290119051, 5.098476259, 4.912178612, 4.364518198,
      2.937437356]
# los valores para n = 1/2
E_p = [2.17, 2.11, 2.03, 1.96, 1.88, 1.80, 1.71, 1.63, 1.54, 1.45, 1.36]
# los valores de la energpia del foton

# Se selecciona las secciones lineales para ambos procesos
y_1 = [105.4784781, 77.08248343, 48.09700144, 29.48409406]
y_2 = [1.24E+08, 3.53E+07, 5.35E+06]
# Se toman las energías correspondientes para ambos procesos
E_p_final_1 = [2.17, 2.11, 2.03, 1.96]
E_p_final_2 = [2.17, 2.11, 2.03]

# se suponen unos posibles valores de los parametros de la función
g = [0.53, 550]
# Se obtenien los verdaderos parametros
c_1, cov_1 = curve_fit(func, E_p_final_1, y_1, g)
print('Valores de la regresión de n =1/2: ', c_1)
c_2, cov_2 = curve_fit(func, E_p_final_2, y_2, g)
print('Valores de la regresión de n =2: ', c_2)

# Se calculan las y_finales que se obtienen de las energías y la función
# con los nuevos parametros
y_1_final = []
y_2_final = []

for j in E_p_final_1:
    y_1_final.append(func(j, c_1[0], c_1[1]))

for jj in E_p_final_2:
    y_2_final.append(func(jj, c_2[0], c_2[1]))

# Se calcula el ancho de banda
Eg_1 = -c_1[1]/c_1[0]
Eg_2 = -c_2[1]/c_2[0]

print(f'Energía de banda para n = 1/2 es: {Eg_1:.4f}')
print(f'Energía de banda para n = 2 es: {Eg_2:.4f}')
# se promedia los valores de energpia de banda
print(f'El promedio de la energia es: {(Eg_1 + Eg_2)/2:.4f}')
# Se imprime el r^2
print(f'R^2 para n = 1/2: {r2_score(y_1, y_1_final):.4f}')
print(f'R^2 para n = 2: {r2_score(y_2, y_2_final):.4f}')
# se grafica cada uno por aparte
fig, ax = plt.subplots()
ax.grid()
ax.plot(E_p, n2, 'r.')
ax.plot(E_p_final_2, y_2_final, 'b-')
ax.legend(['Valores', 'Regresión lineal'])
ax.set(xlabel='Energía del foton [eV]',
       ylabel='(αhv)^(2)[(cm^(-1) eV)^(1/2)]x10^5',
       title='Diagrama de Tauc para n = 2')
fig.savefig("Diagrama de Tauc_2.png")
plt.show()
