# CLASE JUEVES 05 OCTUBRE ASTROINFORMÁTICA

computadora es determinista

algoritmo: coherencia y orden específico, sino no cumplo la tarea

linealidad de los algoritmos es fundamental 

con instrucciones son consecutivas

código: agente inteligente: caracterizar las entidades que se pueden comportar de forma autónoma, que solucionen un problema sin que uno le explique cómo hacerlo 

programas se comportan como agentes, tienen medio de comunicación a mundo no virtual

esto es input(los parámetros q le inserto, etc) y output(lo q muestra en pantalla, etc)

ningún algoritmo vive por sí solo, tiene q comunicarse por entrada y salida

input y output son datos

### principios generales

**DRY**: Don’t Repeat Yourself

NO PROGRAMAR ALGO Q YA PROGRAMARON !

LO IDEAL ES PROGRAMAR ALGO 1 VEZ Y NO VOLVER A PROGRAMARLO

idea de la POO

también aplica en el mismo código, no repetir las mismas líneas en el mismo código, significa que no está 100% eficiente

**KISS**: Keep it Simple and Stupid

buscar la simplicidad ! si tenemos 2 soluciones en la mente para el mismo problema, hacer la más simple, probablemente sea la más 

elegante para mi código

evitar complicar las cosas.

**RTFM**: Read the fucking manual

**PSEUDOCÓDIGO**

representación de alto nivel

texto libre informal, uno lo piensa en el lenguaje de programación que vaya a usar, o sepa

pseudo código tiene q ser claro y breve

**DIAGRAMAS DE FLUJO**

ordinograma o flujodrama ? XD 

similar a pseudocódigo pero contienen condicionales, iteraciones y objetos

si pongo un bucle debo poner en el diagrama el flujo el camino

rombo: condicionales, 2 posibles caminos 

ejemplo aplicación diagrama cris

ganancia en el rendimiento

reducir 10 horas a 1 !!!! identificando llamados duplicados, o bucles

lectura disco más lenta 

diseño de flujo antes !!!!

orden del cálculo, determina cuántas veces una instrucción se tiene q repetir

### algoritmos en POO vs procedimental

identificar las componentes del problema, los sustantivos

1. principio de la responsabilidad única: clase que defino tiene q tener una única razón para cambiar, cambiar de estado, q los atributos de mi clase o algo cambien, estos cambios se asocian a una responsabilidad, cada clase nace en respuesta a algo que quiero hacer, y esa idea se debe mantener, mientras más responsabilidades tenga una clase más difícil es … , clase interfaz: permite comunicarse entre clases? un integrador, que no dependan entre ellas. Una clase por cada responsabilidad.
2. Principio de open/close: abiertas para extensión pero cerradas para modificación, para ello _atr_private y eso q nos enseñó la clase anterior
3. Principio de sustitución de Liskov: los objetos pueden ser reemplazables y no alterar el funcionamiento de la clase. Programas q utlizan obj de una clase: esos obj pueden ser reemplazados con obj creados con clases derivadas de eso. - Sustitución de Liskov: Se sustituye una clase del programa con una clase heredada de la misma clase
4. Principio de segregación de interfaces: si tenemos un programa, si una persona utiliza una interfaz (clase método …) usar solo la q necesito usar ?? segregación de interfaz: distintos interfaz para distintos ??, x ej en matplotlib para el eje, para el label, para la escala, etc. Métodos de clase para cada interfaz, plt la rompe x eso. Sólo usar la interfaz q necesito, no es necesario llamarlas todas siempre, solo si las necesito
5. Principio de inversión de la dependencia: si tengo 2 clases, y uno es de más alto nivel q el otro, si estas 2 clases dependen de una 3ra q puede ser interfaz, la dependencia con esa 3ra no debería ser explícita, sino q a través de una abstracción, clases q no dependan de los datos q escribo de forma explícita en el código. 

la modularidad, códigos q sean escalables, q puedan trabajar más de 1 persona en el mismo código, que sea independiente el código dentro de sí mismo.

**UML**

que sea visual la especificación, las tareas, la documentación etc

conjunto de posibles diagramas predefinidos q permiten hacer planos o modelos de mis códigos.

se incluyen 2 tipos de diagramas: estructura y comportamiento : 

estructura: representar de forma gráfica

diagrama de clases el más utilizado, pq acopla a los q programan con POO

hacer el programa 

ayuda a los POO más complejos

herencia lo + bkn pero se usa harto la composición

ambas cosas son atributos pero el uso q le damos es distinto y sirve diferenciarlo para el diseño, 

iterador: obj q devuelve una secuencia de valores, métodos especiales, init next y nose q otro

yield: especial , dentro de una función o una clase

ej: fn range: es un iterador no una función

iterador: evita q uno construya grande lista de cosas para hacer loops sino q la van generando 

iterador q recorre un conjunto de elementos no es necesario saber el detalle de lo que contiene

