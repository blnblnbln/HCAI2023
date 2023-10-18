# CLASE MARTES 03 OCTUBRE ASTROINFORMÁTICA


**herencia:**, 
herencia responde al verbo to be, 
¿cuándo usar herencia? cuando lo que construimos como propagación del algoritmo responde al verbo to be, 
herencia: podemos definir métodos vacíos dentro de una clase, para poder usarlos mas adelante en la clase que hereda dicha característica, y se puede editar en la “subclase”

**polimorfismo**: consecuencia de la POO,
sin POO no tenemos polimorfismo

### función super
si tengo una herencia y tengo un método, cómo lo utilizo?,
rompe reglas de python: pq es una función que se trata como un objeto,
¿cuándo uso super? viene de la mano con la herencia, forma que uno tiene para conectar toda la maquinaria que uno hace en la clase base para conectarla en la base nueva,
extensión de la categoría, o modificación,
es como una rama de github pero creando un objeto nuevo

si hago una class A y una class B(A), B puede tener 2 constructores? el propio y el de A, B es herencia de A?

aunque esté heredando puedo llamar un método de una clase?,
super hace que el cambio sea sólo donde se pone la herencia,
no tener q utilizar el nombre de la clase, sino que uso super ,

super para llamar a los métodos que están en la **clase base**,
super invoca o llama a los métodos de la clase base,
return super(). area(lado, lado) toma el área de arriba de rectángulo no de cuadrado, el de la base original,

recursividad: algoritmo : toma una fn o método y dentro del método q se llame el mismo método (ej: factorial),
problema: fácil hacer un loop infinito y  x cada llamado se genera una nueva instancia, fácil llenar la ram

### ENCAPSULAMIENTO (ahora empiezan las derivaciones de POO)

capacidad de tomar un montón de cosas y compactificarlas para que tengan sentido en si misma y no desde afuera

propiedad o práctica de restringir el acceso a componentes de un objeto, permite ocultar los detalles

**si empieza con _ es atributo protegido (solo 1 guión bajo), solo acceden a las clases derivadas**,
**si empieza con __ es atributo privado (2 guión bajo), no quiero q ese atributo sea accesible por nada ni nadie**

name mangling: toma el nombre y una vez q se define una clase 

python todo es público, pero hay convención para ocultamiento.

__ asdf __ métodos especiales,
**si sólo empieza __ asdf toma el nombre del atributo y lo cambia**

consecuencia: ocultar más la info

name mangling: le cambia el nombre para que no la puedan usar, para dificultar su acceso

### polimorfismo

cambia de forma dependiendo de cómo lo use

2 tipos de polimorfismo: 1) a través de funciones y objetos como matplotlib con python, mat no le importa si es array, lista o cualker cosa y 2) polimorfismo con métodos, como el perro que habla, utilizando reescritura de métodos, nuevas clases permiten generar objetos con características similares

puedo utilizar esos objetos como si fueran iguales

comprobación de tipo,
el algoritmo debe preguntar que es 

C : subo la escalera, saco la ampolleta, pongo la nueva,
POO : ampolleta : cámbiate

**hacer ejercicio polimorfismo**

### herencia múltiple

capacidad de generar una clase derivada usando varias clases base

todo todos los atributos de mis clases q incluye atributos de datos, métodos, y todo eso es parte de mi nueva clase

python método automático: MRO method resolution orden

devuelve una lista q dice cuál es el orden que sigue para poder buscar

clase primordial: objeto

int.mro()

primero irá a “int” luego a objeto

mro es obvio en orden secuencial, pero en herencia múltiple se complica

mro establece el orden de búsqueda

primer problema herencia múltiple:

1. mismo nombre
2. herencia en diamante, como el ornitorrinco

### composición, objetos compuestos

como el teclado q pertenece a la computadora

utilizar objs como atributos de otros 

motor con el auto 

no es lo mismo que la herencia!!

no se lleva por el verbo to be

auto tiene componente q es el motor, y ese motor puede tener sus propios métodos, y puede 

método preferido: composición

no confundir verbo de la caracterización

en simulación su composición serían las partículas, etc