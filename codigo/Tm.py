"""Regresión Tm."""
from datos import x_min, min_final
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# No se pudo encontrar facilmente la función que toma la forma de la envolvente
# por ello en este proceso se usó Matlab


def func(x, M, d, p):
    """Funcion que se supone que toma la forma los minimos."""
    return M / (1 + np.exp(p*(-x + d)))

# Se suponen valores proximos a los de la regresión


g = [0.53, 550, 0.05]
# Se calcula los valores reales de los parametros
c, cov = curve_fit(func, x_min, min_final, g)
# Se imprimen estos parametros
print(c)
# se crea el vector que guardará la información de la y que es calculada
# con los x y la función con los parametros calculados siendo la 'y final'
y = []
for j in x_min:
    y.append(func(j, c[0], c[1], c[2]))
# Se comparan ambas y y min_final para encontrar el r^2 de la regresión
print('R^2', r2_score(y, min_final))
# Se grafica la regresión y los datos iniciales
plt.plot(x_min, min_final, 'r.')
plt.plot(x_min, y, 'b-')
plt.savefig('regresionTm.png')
plt.show()
