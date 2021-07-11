"""Obtener los valores de los maximos y minimos para x y graficar."""

import Tm
import TM
import matplotlib.pyplot as plt
import datos

# Se crea una lista con los valores de la longitud de onda
x = list(range(300, 1150, 1))
# se crea la lista que tendra los valores de la envolvente inferior
y_min = []
for i in x:
    y_min.append(Tm.func(i, Tm.c[0],
                 Tm.c[1], Tm.c[2]))
# se crea la lista que tendra los valores de la envolvente superior
y_max = []
for i in x:
    y_max.append(TM.func(i, TM.c[0],
                 TM.c[1], TM.c[2]))
# Se crea la lista donde estaran unicamente donde estan las longitudes de onda
# maximas y minimas
x_final = []
x_final = Tm.x_min + TM.x_max
x_final.sort()
# Se crea la lista donde se guardan los valores minimos y maximos de x_final
y_min_final = []
y_max_final = []
for j in x_final:
    y_min_final.append(Tm.func(j, Tm.c[0],
                       Tm.c[1], Tm.c[2]))
    y_max_final.append(TM.func(j, TM.c[0],
                       TM.c[1], TM.c[2]))

# Se imprimen los valores encontrados para x_final
print("λ  \t minimo  maximo")
for ii in range(len(x_final)):
    print(f"{x_final[ii]}\t{y_min_final[ii]:.6f} {y_max_final[ii]:.6f}")
# Se grafica las envolventes
plt.plot(x, y_max, 'r-')
plt.plot(x, y_min, 'b-')
plt.plot(datos.T.index + 300, datos.T['trnspeli'], 'g-')
plt.savefig('envolventes.png')
plt.xlabel("Longitud de onda")
plt.ylabel("Transmitancia")
plt.legend(['TM', 'Tm', 'T'])
plt.show()
