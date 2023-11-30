# CLASE JUEVES 30 NOVIEMBRE ASTROINFORMÁTICA
recordamos los pasos a seguir ... problema, marco físico, condiciones iniciales, discretizar, codiguear.

para poder llegar a esos filamentos, empezamos como un cubo de gelatina, cómo llegamos a conseguir eso?

_principio cosmológico_: distribución de masa/energía es isotrópica y homogénea

cluster galaxias con su host y satélites, parado dentro de un filamento , en DM en Millennium-XXL simulation
de cerca vemos "no homogénea", pero si nos alejamos mucho, vemos que todos los cuadrados son iguales

funciona en distribución de DM, la representación de los bariones, e trazado no 1 a 1, un bias traces, los bariones no nos dicen del todo cómo es la distribución del universo

### radiación cósmica de fondo
1. primero encontraron sólo 1 estructura: todo igual color, T = 2.728 K
2. dipolo, es efecto de proyección de nuestro movimiento respecto al universo en sí, está el desplazamiento de la glx c/r al ambiente, nuestro mov, mov sol alrededor glx, mov tierra alrededor del sol, nube de magallanes está metida, es una velocidad adicionada, si le resto 2728 K
3. CMB real? 18 $\mu$ K

la llegada del satélite Planck 
7 grados, 20 min arco, 10 min arco

muy pequeña diferencia en T

caja de tamañao limitado : 300 Mpc
si universo homogéneo e isotrópico, pero...
si lo dejo así se va a colapsar, las partículas se van a desintegrar

¿cuál es el truco? puedo replicar la caja pero me tomará mucho tiempo que corra.
entonces: utilizar esas asumption a una escala mayor, si realmente es homo e iso, no me importa qué viene después, para qué hacer más si puedo hacerlo infinito, si salgo por la izquierda entro por la derecha.
suficientemente grande para que esa separación no sea significante
**condiciones de contorno periódica**: infinite, periodic boundary conditions

¿cómo homogeneizar potencial del de abajo con el de arriba? hago como que mi objeto siempre esté en el centro
lo mando del radio abajo para arriba, es un switch en la simulación

1er paso: homogéneo e isotrópico, infinito
2do paso: perturbar esta distribución de acuerdo al CMB, redshift=100-120

**transformada de fourier**: suma de senos y cosenos, donde la amplitud dice q tan importante es esa onda en partícula

eje x: frecuencia, eje y: amplitud, amplitud mayor pq es la q domina, pero la q està por encima con frecuencia mayor pero amplitud menor

power spectrum: línea continua de frecuencias, donde dice cuán importante es la frecuencia para poder determinar la señal

más profundo : más perturbaciones
es mi criterio el que decide hasta dónde observo

no nos importa la densidad, nos importa **el contraste de densidad**
saber cuánto c/r a la densidad media 
cuántas veces más denso el pedacito del universo
k número de ondas: frecuencia
power spectrum, amplitud

contraste es el rojo, ver figurita denuevo, épica

transformada fourier, períodico, hace q sea más fácil el cálculo por la periodicidad

típicamente uno encuentra q el power spectrum de CMB es una power law

hay ciertas escalas donde las estructuras existen o no existe, a qué se debe? cuando el universo comienza todas las partículas tienen un sigma
no será suficiente para mantener, se irán
el DM dice q las sigma son bajas, grupos pekeños logran sobrevivir estos sigmas
hay otros modelos donde ese sigma es mayor y se llaman warm y hot DM

caja en 3D es cuando veo una nebulosidad
pozo potencial es xikito en galaxias xikitas, entonces desaparecen
xikito el pozo potencial y su velocidad de escape asociada

diferencia es la velocidad de dispersión inicial:
COLD DM, WARM DM, HOT DM

hot DM corta de 10^5 para abajo
**más hot + dispersión: desaparecen xikitas**
**más cold : - dispersión: xikitas sobreviven**

lambda es dark energy, paralelo al DM
lambda nos da el tipo de geometría del universo

euclidiana: sería cuadrado
pero nop, somos esfera: se forma un "triángulo" esférico

**época reionización**: potencial y cualker obj calienta el gas y se difumina el gas, el gas no colapsa, está ahí pero no lo vemos ???

power spectrum observado ... a distintas escalas con distintos telescopios

homo e iso + power spectrum observado = initial conditions (img en 3D)

### evolución temporal
sistema dinámico más simple : péndulo, a medida q avanza en posición tiene una cierta velocidad, cuando está en su máximo: **apocentro**
**espacio de fase**: amplitud de la onda, ángulo es la frecuencia angular

f(x,v,t)

_colissionless boltzmann equation_
si no hay colisiones la fn f es cte en el tiempo, es decir la masa no desaparece del espacio de las fases, si hay colisión desaparece, pke vengo con velocidad y choco contra la otra partícula, después la otra salta, la otra cae, entonces desaparecen en el espacio de fase, esto ocurre en **sistemas colisionales**
**sistemas no colisionales**: si mis partículas se expanden, su velocidad decrece, si vel aumenta entonces más pegaditas entre ellas

stellar streams: al principio finito y después más disperso: no colisional

df a dt es 0

considerando que la masa es un fluido ideal

sumado a la ecuación de Poisson

- Colisionless boltzmann equation: La masa de las particulas no se escapa de un pupnto de tiempo a otro en un salto temporal, ya que no hay colisiones, por ejemplo las stellar streams jejej (se observa en como se vuelve angosta o ancha dependiendo del momento de la orbita en la que se encuentre) Para extraer trayectorias y velocidades (E cinetica)
    - Ecuacion de poisson: La masa se comporta como un fluido ideal sin colisiones. Para extraer el potencial 
    - Ejemplo: Galactic dynamics pag.190

si integro en todo espacio? distribución en espacio real
si integro en toda distribución real? dispersión de velocidades


se la posición de ese

**simulaciones cosmológicas**
calcular fuerza entre partículas

con la fuerza ya se donde corregir velocidad???

**MonteCarlo**
### MODELO N CUERPOS !
en vez de ponemos fluido constante, discretizamos
agarrar algo suave, tomar cuadrados gruesos y tomar distribución
se van desarrollando de forma autoconsistente

### softening length
hay que regularizar para que no colapse
es una aproximación, pero es necesaria porque sino colapsará
inherente a la discretización de un fluido
va dentro, no es global, es con respecto a las fuerzas
por debajo no le creo nada ! 

ej: Auriga tiene 180 kpc, dentro de 180 kpc no le debería creer tanto.

ej 3 kpc: todo lo q esté dentro de 3kp no es creíble ...

la realidad no es que todo el cuadradito esté en una sola partícula, porque el pozo potencial es muy grande y no es real porque en verdad son muchas partículas chiquitas que el único potencial que le importa es el global

particle-particle método más simple pero 2 años de cómputo !!!

- Softening length : Distacia de duavizado para que la integracion de la fuerza (la fuerza mencionada anterior $F_{i}$) para evitar que se destruya el sistema por la distancia entre las particulas y su posible interaccion chocadora. 

* Integracion particle-particle (PP): Demasiadas operaciones... no sirve para simulaciones de galaxias por ejemplo.