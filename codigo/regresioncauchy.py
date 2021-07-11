"""Regresión para la longitud de onda y n2."""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


def func(x, a, c):
    """Funcion de cauchy."""
    return a/(x**2) + c


L = [571, 588, 611, 633, 660, 690, 723, 761, 804, 853,
     910, 975, 1055]
# Los valores de la longitud de onda
n = [2.9674, 2.9595, 2.9445, 2.9256, 2.8989, 2.8807, 2.8628,
     2.8444, 2.8276, 2.8135, 2.8015, 2.7890, 2.7686]
# Los valores de n2

# Se ponen parametros cercanos a lo que se espera
g = [100000, 3]
# Se calculan los verdaderos parametros
c, cov = curve_fit(func, L, n, g)
# Se imprimen los parametros encontrados
print(c)
# se crea el vector que guardará la información de la y que es calculada
# con los x y la función con los parametros calculados siendo la 'y final'
y = []
for j in L:
    y.append(func(j, c[0], c[1]))
# Se comparan ambas y y n para encontrar el r^2 de la regresión
print('R^2', r2_score(y, n))
# Se crea un nuevo vector con los los valores de lamdba que faltan
x = [540, 549]
# Se crea el vector que guardará los n2 faltantes
y_final = []
for ii in x:
    y_final.append(func(ii, c[0], c[1]))

# se imprimen los valores faltantes
print('λ     n2')
for i in range(len(x)):
    print(f'{x[i]}   {y_final[i]:.4f}')
# Se grafica
fig, ax = plt.subplots()

ax.plot(L, n, 'r.')
ax.plot(L, y, 'b-')

ax.set(xlabel='longitud de onda (nm)', ylabel='Índice de refracción',
       title='Regresión de la función de Cauchy, λ vs n2')
plt.legend(['Valores obtenidos', 'Regresión de Cauchy'])
ax.grid()

fig.savefig("regresioncauchy.png")
plt.show()
