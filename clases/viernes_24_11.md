# CLASE VIERNES 24 NOVIEMBRE ASTROINFORMÁTICA

### CADENAS DE MARKOV
clima: sol, nublado, lloviendo

representan procesos estocásticos a tiempo discreto donde la probabilidad de cada estado futuro depende únicamente del estado actual, no de estados pasados.

representación de los cambios posibles que puede tomar un sistema, incluye todas las probabilidades de salto de un estado a otro incluyendo a sí mismo

estados categóricos: early o late type ejemplo

_estado de Markov_

tiene que tener predeterminado el camino futuro de todos modos ... categorizado
ej: un juego de ajedrez

cambio dominado por una transición, la idea es saber esta transición

**matriz de transiciones**
**diagramas de estado**: saber hacer primero una predicción exacta de qué estado tomará, proyectar, en N pasos + cuál es la probabilidad de que esté en A, B o C -> álgebra de probabilidades, o árboles de decisión, puedo usar cuántos estados quiero pero idealmente que sean finitos
ej: el de la ciudad, los diferentes estados corresponden a las diferentes posiciones? y las transiciones los caminos? o al revés?

machine learning con bach !!!!!!!!! se puede usar para cadencias !!!! armonias !!!

**estados que sabes que se pueden describir**

### CADENAS DE MARKOV CON MONTECARLO

2 estrategias combinadas ! y diferentes !
son un conjunto de algoritmos utilizados para **muestrear una distribución de probabilidad** que no puedo muestrearla analíticamente
no puedo analíticamente porque: mucho costo computacional, o + empírica, o que no tiene solución analítica

_determinar de forma empírica cuál es una distribución de probabilidad_

esto sólo funciona si la **propiedad de MARKOV se cumple** !!
la probabilidad de ...(cambiar de punto a punto? calcular distribución prob del otro punto?)... depende sólo de en qué estado estoy ahora, no de los estados anteriores de la cadena

no depende de cambios anteriores.

_inferencia bayesiana_: resultados empíricos para distribuciones de probabilidad
esto es todo lo contrario ???
> ver link que puso profe !!!
c/u de los puntos es entendido como el estado de una cadena, no son estados discretos como Markov, sino que c/cadena va construyendo su propio estado, cadenas extensibles, con parámetros quizás en un plano contínuo

### METODOLOGÍA
- MCMC genera una **serie de muestras** (estados de la cadena de Markov) para representar una distribución desconocida
- Comienza desde un **estado inicial**, y luego realiza **transiciones** a nuevos estados basándose en ciertas _reglas probabilísticas_, es: qué tan probable es que yo pueda samplear mi distribución, elegir el punto inicial NO es trivial !! si los pongo en diferentes posiciones tendré diferentes caminos, transición: ¿dónde pongo mi punto 2?, insertar una distribución de probabilidad asociada a método MonteCarlo
- Con **sufientes iteraciones** la distribución de las muestras tiende a la distribución objetivo (la que se desea estimar)
- **quemar la cadena**, se pueden descartar las primeras muestras para asegurar que la cadena ha alcanzado su estado estacionario

**Metropolis-Hastings**: establece criterios para elegir cada cosa, el salto por ejemplo, o cuántos saltos voy a hacer
- cada vez que tenga un punto, el siguiente va a estar determinado por una probabilidad relativa a la muestra actual.

Suponer que el modelo me permite representar el modelo 
Decisión: 
1. Se calcula la razón de aceptación comparando la densidad de probabilidad de la nueva muestra con la actual
2. Si la nueva muestra es más probable, se acepta; si es menos probable, se acepta con una probabilidad igual a la razón de aceptación

$dfrac{P(X_1)}{P(X_1|X_2)}$

### procedimiento
**en cada iteración t**
Generar candidato x' para la sgte muestra seleccionándolo de la distribución g(x'|x_t)

**aceptación o rechazo**
si mi numero es menor q alfa lo acepto ($x_{t+1} = x'$), sino empiezo denuevo, este procedimiento me da que x cada punto elegido. (rechazo: alfa menor : ($x_{t+1} = x_t$))
más lejos del centro es menor que más cerca del centro, la probabilidad de que el punto más lejos sea aceptado es más baja que la que esté cerca del centro.

sirve para: ajustar parámetros de un modelo
falla cuando tienes muchos máximos, o cuando no eliges bien la fn de distribución de probabilidad.
sigma grande: mapeo ineficiente, sigma pequeño: cadena que nunca converger, no mapeo todo porque voy con pasitos pekeños

sirve para modelos ...con restricciones
para ajustar funciones

todos los modelos semianalíticos lo usan para ajustar ~15 parámetros que usan, cada iteración tarda 15 min, sirve si kero explorar parámetros en espacio multidimensional.

PSO: cadenas que se comuniquen entre sí

hormigas se pueden representar con cadenas de Markov !!!

_repasar probabilidad !!!_
