# CLASE JUEVES 07 DICIEMBRE ASTROINFORMÁTICA

un halo es un halo y una galaxia es una galaxia... no tenen por qué ser lo mismo 
*estrellas: evolución estelar, enriquecimiento químico, procesos de feedback, gravedad.
*DM: gravedad.
*gas: hidrodinámica, fisica del medio intergaláctico, formación estelar, gravedad.
si modifico 1 modifico todo lo demás, es NO lineal

ecuaciones de Euler
todo fluido está representado por un número de campos:
1. densidad : escalar
2. presión : escalar
3. campo de velocidad : vectorial
4. potencial gravitatorio : escalar

diferencia entre un campo escalar y un campo vectorial: el output del campo, para cada posición tengo una densidad con un valor único: escalar, en cambio vectorial: en c/pto del espacio tengo un vector velocidad

cómo tenemos esta evolución temporal y espacial? EULER
- (1) ec de continuidad: dice q si yo agarro una caja y mi densidad local% varía en el tiempo, si hay un decrecimiento entonces la masa, si la densidad está cayendo, toda variación en el tiempo de la densidad : varía flujo en mi cajita, flujo negativo si se va, flujo positivo si acreta, la suma me tiene q dar 0 pq la masa se conserva
- (2) ec de movimiento: variaciones en la velocidad con el tiempo asociadas a las fuerzas q el fluido siente (gravitatoria, presión)
- potencial gravitatorio (lo de la clase pasada)
- (3) conservación de la energía

* fluido se puede explicar con euleriana: veo pasar el agua, o uno que viaja con el fluido y ve las propiedades: lagrange 

### dinámica del gas
en el tren o en las estaciones donde me tengo que parar

- Eulerian formulation: estaciones del tren, derivadas parciales

- Lagranian formulation: en el tren, derivadas totales

¡ conclusiones son las mismas !, se llega a lo mismo, sólo cambia el referent frame

### enfoque lagrangiano
una forma es utilizar _smooth particle hydrodynamics_ (SPH)
pq suavizadas? cuando uno discretiza un fluido, el fluido no es un punto, sino que se va interponiendo una partícula sobre otra y así
dividiendo en conjuntos móviles discretos ? 
imagino que mi fluido está descrito por un volumen + grande q interactúa con su entorno, y mi elemento de fluido interactuando estará descrito por una función llamada **kernel**

el punto es el realidad el centro de la gaussiana, de mi volumen de fluido
por ej: la temperatura no será la del punto central, sino de todo el volumen del fluido, con una función integral

### SPH
ventajas :  - es ilimitado en espacio por lo que no se pierde materia, la conserva
            - no se pierde tiempo moedelando espacios vacíos, only evoluciona en regiones con densidad $!= 0$
            - resolución adaptativa, si quiero cambiar el tamaño del kernel o cambiar la resolución de masa, (no hay que cambiar la grilla entera)
            - historia de evolución del fluido es intrínsecamente fácil de rastrear, (con los semilagran o lagrangianos es imposible)
            - natulareza de partículas facilita acoplamiento con física de N-body o autogravedad, si tiengo partículas trazando el campo es + fácil conectarlo con el campo gravitatorio (x ej: DM), es como una partícula en ESTE caso
            - distribución de masa entre partículas asegura la conservación exacta de la masa, ya que la masa de c/particle es cte a lo largo del tiempo

en euler fijo la cajita, SPH es mejor que euleriano !

desventajas:- si quiero calcular cualquier valor necesito saber cuáles son los vecinos,   actualizar constantemente la lista de vecinos
            - condiciones iniciales influyen en el resultado
            - resolución está limitada por el número de partículas
            - más difícil implementar transferencia radiativa

### EULER
_adaptive-mesh refinement_ (AMR): el código de forma inteligente busca las regiones de mayor densidad y trabaja ahí, donde valga la pena
con ese gas cuánta temperatura se está transfiriendo
se trabaja con jerarquía de grillas, lo que es distinto es que si hay rejilla level 0 sobrepongo rejillas sobre esta.
afecta periodicidad si es que pongo grillas ... ? tiene que ser por fourier
se centra en ubicaciones específicas en el espacio a través de las cuales el fluido fluye a medida q pasa el tiempo, ec de EULER se resuelven con 
mi primera grilla parte del CMB, de ahí comienzo a buscar sobredensidades

desventajas importantes: - no invariancia de galileo, si tengo 2 fluidos 1 estacionario y otro no, si lo evoluciono un desde 0 y otro a 10, si los fluidos se mueven a distintas veolcidades las soluciones varían y no son invariantes, aunque se muevan a mismo ratio?

_estrellas pop 3, prístino, otra IMF, justo después de la reionización, montón de energía_

### moving mesh
arepo: tratar de generar grillas como si fuese euleriano pero que se puedan ir desplazando en el tiempo con una partícula que es la trazadora, combinar ventajas de SPH (trazar lo q importa) pero el transporte de energía se explica con ec de fluidos

generar grilla con _teselación de voronoi_
teselación: fragmentación de espacio
voronoi: buscar la línea q me une 2 puntos, uno puntos y trazo línea, y hago otra línea
en base a distancias medias define volumen, en regiones más densas las grillas son + chiquitas y regiones - densas grillas + grande

el kernel se autodefine por la densidad, y la tranferencia de energía es mejor, no redondeada como un kernel, sino que las paredes naturales es más realista

la masa en el momento inicial de una partícula no tiene por qué ser igual a la final !
eso es difícil porque no sabemos si viene de una dwarf o de un filamento ...

