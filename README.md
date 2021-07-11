# Constantes opticas de peliculas delgadas

Este repositorio fue creado para guardar los codigos realizados en python para el desarrollo del informe 
"Estudio de constantes ópticas en películas delgadas". Existen dos partes:

## En la carpeta codigos se encuentran 6 codigos python que se usaron para el procedimiento de los datos.


1.1  datos.py En este programa se toman los datos que fueron dados por el profesor y se encuentran los maximos 
y minimos relativos de la transmitancias.

1.2 TM.py Se encarga de realizar un ajuste sigmoidal de los valores maximos encontrados, aunque este ajuste es excelente
se decidio no tomarlo para el informe por su tendencia constante al final.

1.3 Tm.py Se encarga de realizar un ajuste sigmoidal de los valores minimos encontrados, aunque este ajuste es excelente
se decidio no tomarlo para el informe por su tendencia constante al final.

1.4 Envolentes.py  se juntan las longitudes de onda de maximos y minimos y se calcula segun las regresiones
encontradas anteriormente

1.5  regresioncauchy.py  Se realiza la regresión según la función de cauchy entre los n y las longitudes de onda

1.6 Tauc.py se usa para calcular la energía de banda por el método de diagrama de Tauc



## En Imagenes se encuentran las imagenes que se desarrrllaron por medio de los programas contenidos 
en codigos.
