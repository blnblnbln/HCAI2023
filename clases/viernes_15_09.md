# CLASE VIERNES 15 SEPTIEMBRE ASTROINFORMÁTICA
python: lenguaje interpretado

python se instala en un lugar, es un software,
se pueden tener varias versiones de python
x ej en conda tener algunos
y en el pc tener otros , 
python es autocontenido, 
C si define una var como int entonces será int 4ever, 
en python no es correcto hablar de variables, todo es un objeto,
a no es equivalente al contenido de a,
tipado dinámico de datos,
para saber qué tipo de dato es usamos type,
todo lo que tiene nombre tiene type, 
todas las cosas que son definidas son iguales,
ipython -> var = … -> type(var) o (print),
tiene booleanos: true & false,
y python crea str,
todo es un objeto en python,

declaraciones en python
**instancia**: concretización materialización efectivización? o realización en memoria de lo que yo quiero crear

qué define cómo se crea? el tipo,
en cada creación se crea una referencia, es el identificador de la instancia,
en cada declaración se crean estas 2 cosas,
python siempre tiene una lista de todas las referencias a las cuales puede acceder,
dir dice cuáles son mis referencias 
dir()

_ : variables ocultas de python

_ _ : referencias que guarda cosas de lib

_ _ name _ _ : nombre de la rutina q está ejecutándose en este momento (doble guión no negrita !!!)

python agrega referencias automáticas

### qué son los objetos?
clases: templates que permiten generar generalizaciones de tipos de datos,
cómo se componen?: tipos de datos nuevos que se construyen con las clases tienen atributos o componentes,
también incluyen funciones que son parte del dato,
que sólo se activan cuando un dato las llama : métodos,
operador ‘’.’’: tomar algo definido por una clase y acceder a sus componentes,
las clases permiten redefinir operadores,
clases: componentes + funciones + operadores,
un objeto es una instancia de una clase,
tomo el template y lo materializo,
ej: el flotante : pi = 3.14 : genera una instancia : genera un objeto tipo flotante,

s.		(doble tab): eso me muestra los no ocultos,
o dir(s) : esos me muestra los ocultos __ ,
operador unario: ++, 
operador binario: funciones : 2 argumentos de entrada (como la suma), 
u operador ternario:

### UN OBJETO ES UNA INSTANCIA DE UNA CLASE DEFINIDA

la referencia es el nombre,
la instancia es el contenido,
una ref no es equivalente a una instancia

las referencias (identificador) apuntan a objetos (instancias)

atributos y métodos de los obj son accesibles con el punto. desde sus referencias

cada objeto tiene asociado un tipo: la clase de la instancia

cada objeto tiene un identificador (id()), basado en la dirección de memoria donde se almacena

id() es como el amperson que me dice dónde está físicamente,
la referencia es como el puntero *,
mismo objeto con 2 referencias: misma instancia (ejemplo de l1 y l2)

### TIPOS DE DATOS COMPUESTOS (TIPOS COMPUESTOS)
set no admite cualquier tipo de objeto,
pq compuestos? pq son clases o tipos de, 
listas puede contener objetos, y como todo es un objeto, puedo contener todo, no le importa si es int o str o lo q sea,
si la referencia y el objeto son … funciona,


tuplas: cuando paso argumentos o genero return de compuestos, es un objeto inmutable,
cuando le pongo coma es ‘,’
no tiene límite de cuánto le pongo,
agrupaciones que permitan tomar una colección de objetos y trasladarlos encapsulados,
los errores se devuelven con tuplas,
tuplas sirven para encapsular cosas, hacer paquetes de transmisión de datos

(array es homogéneo)

set: listas sin orden con elementos únicos, elementos son tipos de datos básicos de python, tipos de datos que no tienen componentes internas que se modifican,
elimina los repetidos , si tengo dos ceros y hago un set de esa lista me mostrará sólo 1 cero

diccionarios: objetos, tomar un obj meterlo al diccionario permite tomar objetos (funciones, str, lo ke sea iwal q las listas),
diccionario pesa una lista y les pone nombre y lo trabajo solo con el nombre apesar de q sea un array gigaaaaaante

el copiado de listas, sets, y diccionarios debe ser explícito, decir directamente que se copie

d[“array”][-5:]  ->  (los últimos 5 del array)
