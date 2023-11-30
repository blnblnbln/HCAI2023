# CLASE MARTES 28 NOVIEMBRE ASTROINFORMÁTICA

N-cuerpos : integración numérica en el tiempo de las ecuaciones que gobiernan las distintas fuerzas actuando sobre un conjunto de N partículas
samplear sistema de manera discreta, incluyendo fuerzas que actúan en este sistema, pueden ser:
- gravedad
- fuerzas hidrodinámicas como viscosidad, presión

tierra, luna, sol: problema de 3 cuerpos, simulaciones numéricas, muy complicado, altamente caótico 

siempre hay soluciones analíticas a problema de 3 cuerpos, pero en general la solución a los problemas de +3 cuerpos (no integrables, muchos grados de libertad) son *numéricas*
"En general la solucion a los problemas de mas de 3 cuerpos (no integrables, i.e. demasiados grados de libertad) son _numericas_"
no lineal
si el sistema es integrable o no, si es caótico **no** es integrable
caótico: ante pequeñas pertubaciones el resultado es sumamente diferente en la evolución

¿Por qué usamos las simulaciones?
Obtener información sobre sistemas físicos que no se pueden reproducir en laboratorio.
También ayuda a entender sistemas complejos, no solo por la gran cantidad de elementos, sino por posibles acomplamientos no lineales entre distintos procesos físicos, ejemplo RPS no se pueden hacer los cálculos a mano 

### Pasos a seguir
1. definir al problema que quiero estudiar, específicamente, pregunta científica, qué quiero resolver de la galaxia
2. marco teórico, marco físico de trabajo, ej: *lambda CDM*, gravedad tipo camaleón, warm DM
1 y 2 son transversales a toda la astronomía, ahora en específico para las simulaciones numéricas:
3. generar las condiciones iniciales, es el problema más difícil, ej: cúmulo globular, función suave y continua es la que nos dice la masa, pero esto es discreto... pongo la gravedad, posiciones, va a colapsar porque me faltó la distribución de velocidades, sino se relaja y termina en un sistema soportado por presión pero no tiene que ver con el cúmulo globular, fuerzas interactuando en equilibrio para que no colapse. Densidad en el espacio de las fases, `f dx dv`, lo que distribuye cualquier sistema dinámico, depende de 6 variables, hamiltoniano y lagrangiano x_x, para cada x habrá una v particular, eso lo dice la función, lograr representarla de forma discreta, eso se logra con MonteCarlo, que sea representativa pero aleatoria, la dificultad es intrínseca, no depende de si es discreto o continuo.
4. pensar en cómo discretizar, como va ir saltando mi partícula en el tiempo según la fuerza ???, como evoluciona en el tiempo, tendremos que elegir saltos donde vamos integrando (hay millones de formas de integrar), puedo tener pésima evolución del sistema no por condiciones iniciales sino por no discretizar bien. Para poder resolver las ecs que gobiernan los distintos procesos físicos involucrados con un modelo numérico: hace falta discretizar
5. escribir el código, no es llegar y hacerlo, comúnmente hay que agregar 

Método numérico más simple: resolver una integral
saco el área bajo la curva, pero si la fn es complicada se resuelve con aproximaciones, cuáles? dependen de cuántos errores quiero propagar, con Riemann, mientras + xikito el rectangulito mejor es la aproximación
es mejor la aproximación del trapecio, hacer una línea y rellenar

_de micro a macro_, de estructura estelar a universo a gran escala, pero entremedio tenemos las galaxias.

Auriga: simulaciones de galaxias tipo MW
no nos dice la verdad del universo ... pero nos aproxima
brazos: se forman por atracción gravitatoria de glx host con satélite
lograr descubrimientos gracias a las simulaciones, si en una simulación pasa algo nuevo en una zona inesperada, podemos pedir tiempo de telescopio para observar esa zona distinta y corroborar el proceso físico
reproducir glx elípticas es muy diferente a hacer MW type
"rápido" : 3 Gyr XDDDDDD

Es complicado simular galaxias tipo MW (L*) por la influencia del AGN feedback en el limite de masa de dichas galaxias. A mayor masa el AGN importa mas y a menor masa (que M*) importa menos

si hago elíptica tiene q tener AGN y bien modelado, sino no podré 
migración radial de las estrellas en disco, estrellas que nacieron y migran, mezcla de enriquecimiento químico, por interacción con los brazos espirales, 
si tengo disco me rompe simetría: ya no es triaxial (halo DM es "triesférico")
si tengo elíptica no es importante el efecto del disco
para tener disco tiene q haber gas, si es only DM sim no tengo gas joasjoas no puedo simular
disco afecta órbita de satélites

**Hydra**: supercomputadora
3 millones de horas a CPU cada simulación
4800 procesadores, aprox un mes por simulación, sin considerar tiempos de espera
sim. numéricas son muy caros, idem a hacer observaciones en telescopios de última generación

### marco teórico
el modelo cosmológico estándar: _Lambda Cold Dark Matter (CDM)_
tiene asumptions: geometría del universo, distribución de masa (75% Dark Energy 21% DM, 4% normal matter)

**principio cosmológico**
La distribución de masa y energía:
- isotrópico,  donde me pare veré lo mismo, el universo es igua en todas las direcciones
- homogéneo, si miro pa trás o padelante, no hay punto preferencial, veo la misma física

**radiación cósmica de fondo CMB**
cosmología como ciencia exacta
radiación de fondo difusa que se observa princpipalmente (mayor intensidad), en longitudes de onda del cm, mm, y sub mm
industria generó conocimiento científico :o 1965
un electrón no se puede escapar, todo condensado, todo opaco, la luz no pasa
pero está la inflación, entonces el universo se expande, y a medida que se va expandiendo la temperatura se empieza a enfriar y hay + espacio, se corta el scattering, y de pronto puf! ya no hay más fotones atrapados, todos se escapan, desde este momento aún vemos esos fotones, han viajado de forma impertubada, luz prístina enrojecida por el estiramiento del universo.

Pero... tenemos pertubaciones, y esas pequeñas variaciones (10^-5, microvariaciones), es lo que queda realmente limpio del universo, los fotones originales
Si hago transformada de fourier veo patrones y veo BAO
el color habla de frecuencias distintas, temperatures distintas, azul + hot, rojo + cold, un fotón se escapa de una región menos densa a otra + densa, + al rojo las que están en - densas???
hay regiones de hot spot y otras de cold spot, entonces no es uniforme
son diferentes potenciales de masa, no solo temperatura, distribuciones preferenciales de masa
no empiezas con un mega cluster
sino que la distribución se propaga en todo, hay más de lo frío 
muy importante para condición inicial, distribución de partículas

### condiciones iniciales
inestabilidades gravitacionales y formación de estructura
nube de densidad, dónde habrá más fza gravitatoria? una pelota de rugby, después un pankeke, después un filamento y después halo
complicado: régimen no lineal, ya no se puede hacer con lápiz...
lo primero que interactúa son los halos

### método numérico
GADGET: glxs with DM and gas interact
permite resolver simulaciones de N-body
_nunca usarlos como caja negra ... siempre leer la documentación_
nodos: halos
primero no vemos nada porke las preturbaciones son pekeñisimas, después vemos filamentos, paredes, nodos, y esos halos interactúan y forman galaxias
crecen en masa por el canibalismo de objetos pekeñitos
ej: aquarius !!! hermoso csm

todo lo que vimos es DM, pero si quiero modelar una galaxia, tengo que considerar los baryones, estrellas, DM y gas
estrellas: evolución estelar, enriquecimiento químico, procesos de feedback (SN), gravedad
DM: gravedad
gas: gravedad, hidrodinámica, 

_¿qué debemos incluir?_
- formación estelar, nubes moleculares gigantes (GMCs) (simulaciones q sólo modelan las nubes moleculares)
- initial mass function (IMF), tengo que elegir, ley salpeter, o chabrier
- evolución química

para las estrellas: distribución de partícula
hoy no hay ninguna simulación que pueda tener 10^10 partículas, son muchas partículas para integrar en el tiempo, no todas las partículas serán estrellas entonces, o pongo 10^8 y cada partícula son 100 masas solares
modelar cómo la población estelar tiene que evolucionar

Para las estrellas es dificil poder simular una particula con una estrella.. Es imposible computacionalmente hablando. Cada particula es una poblacion estelar con una unica metalicidad y edad

- proceso de feedback: que no se enfríe lo suficiente sino q sea de a poco
incluir SN, AGN
halo DM de la MW : Aquarius (2008), ahí no existían simulaciones que formaran glx de disco, le ponían gas y solo salían redonditas y super condensadas

tenían poder computacional grande para meter partículas extras a los baryones
DM, gas density, stellar light: AURIGA PROJECT, 
primero vemos interacciones de DM, luego se forman las densidades de gas, es más extendido, y finalmente se forma la parte estelar, que da fruto a la galaxia, donde puede sufir pertubaciones provocando brazos, o el canibalismo total

evoluciona autoconsistentemente