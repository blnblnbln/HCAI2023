### CLASE JUEVES 28 SEPTIEMBRE ASTROINFORMÁTICA


clase: template para fomrar tipos,
compuestos, tiene atributos y métodos,
atributos: variables u objs,
métodos: funciones asociadas a las clases,
métodos: accesibles siempre a través del punto.

cuando se define un método en la clase, ese método se aplica sobre el objeto instanciado,

parámetro, si pongo = lo rellena

la instancia conoce su propio método y se llama a sí mismo

todo lo que tiene self pertenece a la instancia

diferencia entre instancia y clase,
de que tipo es instancia? es complex definido en modulo main,
modulo main: scope superior,
punto: asignar componente

clase: no le importa si es int, str, todo lo toma como str? python no le importa

si accedo a través de la clase: dependencia de la clase

atributo de una clase 


**clases:**

instancias son las realizaciones de las clases,
al generar instancias genero objetos

le puedo agregar atributos solo a la instancia sin que sea de la clase 

si cierro la instancia todo muere, 
función metida dentro de una clase es un método, para saber q la fn opera dentro de la clase,
función y método son lo mismo, método: fn que pertenece a la clase

self: referencia a la instancia que se crea usando esta clase, 
todo lo que esté con self pertenecen a la instancia,
la referencia sería “d” en el de dog 

el nombre sería una ,
componente .name ,
d es la instancia


referencia: nombre que utilizamos en la variable

importancia de self ! ,
métodos de instancia, 
método: fn q pertenece a una clase y se puede llamar de una instancia ?

omito al self si lo llamo desde la instancia pq se pasa a si mismo ???

atributo: cualker cosa q pertenece a un obj

nunca hacer from numpy import * pq queda la cagá,
demasiaaadas activadas,
mejor especificar

# scope: 

2 métodos +: método de clase (análogo a atributo de clase pero método), uno le pasa al método de clase, @classmethod ponemos de primer argumento una referencia a la clase q se define:cls, en vez de self, 
defino atributos de instancia,
defino método de instancia : utiliza los atributos de instancia

python da libertad de crear atributos y métodos que operen para todos los obj definidos en una clase particular

@static method, por el contrario son básicamente fn metidas dentro de la clase, no modifican atributos de instancia ni atributo de instancia q se quiera trabajar

otros métodos: getters y setters,
POO fue pensado como cosas encapsuladas

set_xlabel :oooo

privados, para no romper nada

constructor %__init__% 
destructor %__del__%