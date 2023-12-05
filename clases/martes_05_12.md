# CLASE MARTES 05 DICIEMBRE ASTROINFORMÁTICA

método directo para calcular fuerzas: particle-particle (PP) integration

2 alternativas:
1. **Tree method**: sistemas de N cuerpos, subunidades para calcular fuerza a otra partícula que esté lejana, mejora la eficiencia, gracias a este método se corren eagle, auriga, millenium

tenemos un sisetma de particulas en 2 dimensiones, (usado cuando no se puede usar PP porque hay muchas partículas), se toma un grupo como una unidad y se calcula la fuerza, la estructura interna no es tan relevante.
    - divide la caja en 4, quedan 4 subcajas, (en 2D, en 3D sería octaltree, como un cubo de rubik), lo divido en 4 pedazos más, luego en 4 pedazos más, hasta estar segura de tener 1 punto en cada cuadradito, solo subdivide donde hay puntos pq el algoritmo es inteligente. Ahora con esta estructura se genera un árbol, comenzando por lo más grande (la caja entera) y el código calcula la masa total y el centro de masa de la caja entera, ahora voy girando en dirección horario (o antihorario), calculando cuántos "puntos" hay en cada rama "cada cuadro".
    - luego el centro de masa de cada cajita hasta llegar a donde hay solo 1 partícula en 1 cuadrado, en c/u de las "hojas" hay una partícula.
    - mido la fuerza entre ellas dos pero considerando el centro de masa
    - **parámetro de apertura**(opening angle lo define una), si es muy grande es muy cerca, tengo que profundizar a lo largo de mi árbol
    - aproximar un grupo de partículas como una sola partícula por centro de masa
    - si lo que veo es más grande , considerar estructuras de menor tamaño
    si theta es 0 sería Particle-Particle
    superparticle=centrodemasa.

son siempre cuadrados , L el largo, D la distancia al centro de masa, también se toma una distancia mínim, para saber si está por encima o por debajo de mi opening angle, ese es fijo, lo que cambio es con qué lo comparo (L/D)

no se hace en cada snapshot, sino que en cada interacción ???? pasos
se usa en GADGET, en vdd en la gran mayoría

muchisimo + eficiente que el método PP

* utilizar centros de masas y no considerar distribución errores, pero es + rápido
* para mejorar suelen usar expansión multipolar de la distribución de masa dentro de cada celda evaluada, (calcular fuerza basada en el cuadrupolo??!?!?!?!)
* típicamente considerar cuadrupolo está ok
** el árbol no debe ser calculado en cada integración

árbol jerárquico evoluciona porque partículas van cambiando de lugar, se calcula distancia mínima donde sea necesario recalcular, se hace cada N pasos de integración.

tratamos de resolver pozo potencial, Poisson

2. **Particle Mesh (PM)**: asumir que partículas no interactúan directamente entre sí, sino que con un campo medio que genera esa densidad, este método suaviza las interacciones (como el softening len?), en vez de dividir en múltiples casos, calculamos grillas que dividen todo mi espacio y calcular la densidad asociada a cada uno de los puntos de la grilla (que la grilla es fija), y ver la masa qué potencial genera en cada grilla.

La gracia es que la grilla tiene una periodicidad

> _Expansiones multipolares_ para evaluar mejor la masa dentro de la celda
- Metodo para calcular fuerzas: Particle Mesh (PM)
    El potencial gravitacional se contruye por 'mesh' usando la ecuacion de poisson:
        $\nabla^2 \Phi = 4\piG\rho $ se pasa a espacio de fourier para poder resolverla de manera mas inmediata usando la transformada como solucion a la integral
    Las grillas son fijas, pero se pueden superponer 
    Las grillas se pueden usar 
    * Gadget: smooth particle hydrodinamics.
    * Arepo: cambia el sistema hydrodinamico.

Definir como asignar la masa a c/u de estas celdas
ventajas: fácil de implementar y suele ser más rápido que tree method (si la masa llena el volumen)
desventajas: al ser cuadradas las rejillas pierde la isotropía de la distribución de las fuerzas, errores sistemáticos que se van a propagar. La aproximación de la fuerza es anisotrópica en la rejilla (una partícula q debería producir una fuerza esféricamente simétrica se verá afectada por errores que selecciones direcciones alineadas con la rejilla)

a mi masa le asigno un peso y si lo distribuyo en 1 solo lugar o desparramada, lo más tonto es buscar el punto más cercano XD

* _nearest-grid-pointing_, el único punto con masa será el cercano

* _cloud-in-cell_ (CIC) puedo elegir un peso que tenga el tamaño de la cajita, entonces esa masa la divido en la cajita

* _triangular-shaped-cloud_ nube triangular que el peso va en forma de triángulo, dependiendo de la altura, pone más masa en el nearest point, no es uniforme, voy a distribuir en 2 o 3 pero no en solo 1

saber cuánta masa le corresponde a cuál cuadro: CIC

_métodos híbridos_: puedo usar combinaciones de todas las técnicas

ya teniendo el potencial debemos calcular la evolución temporal, con EDO, para sist. N cuerpos
**método para integración de órbitas** discretizar el tiempo con pasos de integración, esos pasos son `h`, esto debe ser consistente, es decir que a medida que pasa el tiempo la solución numérica tiene a la solución exacta cuando h = 0, que $\eta = y(x)$

_error local_: error de mi código en algún paso de integración, se asocia a Taylor por ejemplo, el error sería del orden del siguiente factor
_error global_: terminar donde se debe, delta final, es ideal que sea lo más pequeño posible, es como comparar el mejor método posible con el actual, es decir la resta entre la solución numérica y la solución exacta, en valor absoluto

para integrar:
- integradores de alto orden (4to orden), considerar pasos pequeños
- métodos simplécticos: conservar la forma, conservar el volumen en el espacio de fase, en fn de esto sabemos que la energía se está conservando.
- el más clásico: euler integration simplest integracion method, posición y velocidad, si lo comparamos con expansión de Taylor, el error es O($h^2$) first-order accurate
el más simple pero el más malo 

otros: si mi velocidad no es cte. a primer orden: vel y pos inicial, sería muy grande el error al considerar velocidad cte. (first-order)
otro: *MIDPOINT* que hacen un paso intermedio, es más costoso pero mejora la calidad, el truco es calcular primero con Eular el desplazamiento hasta la mitad de mi paso de integración, calculo posición y nuevas pendientes que yo me daría con la velocidad en ese lugar, después con esas nuevas pendientes las uso para calcular el crecimiento, ahora la pendiente me da otro salto y provoca que el error local cambie mucho !!! (second order), es como calcular 2 veces el método de Euler pero cambiamos el punto de velocidad.

*Leapfrog integration*: salto de rana jaja lol
primero calculo velocidad punto medio, salto de 0 a 1 pero también de 0.5 a 1.5, van desfasadas por 2, (drift y kick)

conserva momento angular, es reversible en tiempo, preserva phase-space density (symplectic)

_Runge-Kutta_ preciso hasta h a las 5, es más complejo pero se usa mucho, toma la posición inicial + saltos que consideran pendientes en 4 distintos (por eso error es el 5), es el promedio de esas 4 posiciones, esa es la posición con la cual me quedaré (posición final)
puede ser hasta orden infinito !!!! es el más preciso
pero no son simplécticos buuu, no conservan energía, errores se propagan, puede ser peor 

leapfrog es mejor porque se mantiene constante, y con menor error que Euler, sin embargo R-K parte con menor error pero se propagan tanto al no conservar la energía que se puede ir hasta Euler en cuanto al error

hoy vimos como calcular potencial y teniendo esto vimos como calcular órbitas
ahora podemos evolucionarlo en el tiempo 1313
