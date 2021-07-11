"""Determianción de los maximos y minimos de T."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import pandas as pd


# Leer el documento excel
data = pd.read_excel(
    '/home/onixseries/Documentos/pedro' +
    '/Nacho/9 semestre/Tecnicas/Ardila/python/datos.xlsx'
    )

# T  los valores de la transmitancia de la película
T = pd.DataFrame(data, columns=['trnspeli'])
# Numero de datos que revisa para determinar si es o no minimo o maximo local
n = 5

# Funciones para determinar los minimos y maximos locales
T['min'] = T.iloc[argrelextrema(T.trnspeli.values, np.less_equal,
                  order=n)[0]]['trnspeli']
T['max'] = T.iloc[argrelextrema(T.trnspeli.values, np.greater_equal,
                  order=n)[0]]['trnspeli']
max = []
min = []
# Convierto las tablas en listas
for m in T['min']:
    min.append(m)
# Remuevo los Nan de la lista
min_m = [x for x in min if np.isnan(x) == False]

min_final = []
x_min = []
# Se quitan los 0 de la lista anterior y se encuentra su
# correspondiente valor de x
for m in min_m:
    if m > 0:
        min_final.append(m)
        x_min.append(min.index(m) + 300)
# Elimino el ultimo valor de las listas porque termina cortada la grafica
min_final.pop()
x_min.pop()
# Convierto las tablas en listas
for m in T['max']:
    max.append(m)
# Remuevo los Nan de la lista
max_m = [x for x in max if np.isnan(x) == False]

max_final = []
x_max = []
# Se quitan los 0 de la lista anterior y se encuentra su
# correspondiente valor de x
for m in max_m:
    if m > 0:
        max_final.append(m)
        x_max.append(max.index(m) + 300)

Ts = 0.9153317647

s = 1 / Ts + np.sqrt(1/Ts**2 - 1)
print('El valor de s es:', s)
# Finalmente grafico e imprimo los valores de los maximos y minimos
print('λ      minimos')
for i in range(len(x_min)):
    print(f'{x_min[i]}   {min_final[i]}')
print('λ      maximos')
for i in range(len(x_max)):
    print(f'{x_max[i]}   {max_final[i]}')

plt.scatter(x_min, min_final, c='r')
plt.scatter(x_max, max_final, c='g')
plt.plot(T.index + 300, T['trnspeli'])
plt.savefig('minimo_maximo.png')
plt.show()
