# CLASE MARTES 21 NOVIEMBRE ASTROINFORMÁTICA 

leer individualmente sobre sckit
_mariposa de Maxwell_

### INTRODUCCIÓN A LOS MÉTODOS NUMÉRICOS

problema en cuadratura : problema complejo que puedo expresar en ecuaciones

¿qué son los métodos numéricos?
- nos permite modelar y resolver problemas matemáticos usando computación
- variedad de disciplinas, física, biología, etc. no tienen solución analítica (de física de fluidos para adelante)
- podemos abordar: interpolación y aproximación, técticas de diferenciación e integración y optimización

chi cuadrado: 


### SciPy
incorpora conjunto de soluciones, implementa un gran número de algoritmos de alto nivel, algoritmos asociados a métodos y cada método tiene limitación
- 

**Interpolación y aproximación**
- interpolación: proceso que necesita de una función que pase por un conjunto de datos, es "rellenar" vacíos entre los datos conocidos, puede ser con recta o con curva (polinomio), aumentar orden puede sobreajustar !!!!!
- aproximación: función que se aproxima a los datos pero no necesariamente pasa por los datos, comportamientos más coherentes a la realidad de la física ??? ej: regresión lineal, cómo aproximar los datos ?? : ajustar una línea XDD según la tendencia de los datos, modelo nuevo que represente estadística ??? 

interpolación más usada en imágenes para rellenar con color

**Ajuste de curvas** : es un modelo más adecuado que las aproximaciones, porque puedo ajustar cualquier curva

RMS suma de los cuadrados y dividido por los datos ???

funcional : S(P) ? 
caso ideal vale 0 
le saco las derivadas y tengo un problema en cuadratura

minimizar funcional 
método analítico ; método numérico
analítico si la matriz es invertible: se puede diagonalizar, si no es invertible no se puede diagonalizar pero se puede triangulizar, pero ahí ya es mejor numérico?
analítico es caro, mejor numérico

problema: mínimos locales vs mínimos globales

mínimo de una función y recorrer fn de forma númerica, no hay cómo saber si el mínimo es realmente el que tengo que encontrar

funcional al ser tan libre, puede ser el problema

agrega un ruido

ruido poisson ??? nada tiene que seguir poisson realmente ??? 

si la paso una serie de pd tiene q devolverme lo mismo, o si entro un array tiene q devolverme lo mismo

siempre parto con una suposición ...
esos errores aparecen en chi cuadrado

si ajusto fn que tiene 7 parámetros libres, la ajusto con 7 parámetros, el primer parámetro debe ser el dato, el eje x independiente

matriz de covarianza: correlación entre los diferentes parámetros

modelos degenerados
marginalización: fijo otros parámetros en los valores obtenidos por el mejor ajuste y se ve como se comporta el ajuste moviendo solo el parámetro que quiero estudiar 

no puedo correlaciones modelos degenerados
chi cuadrado sin estadística no es nada  a a aa a a

ojito con ajustes si es logarítmico owowo