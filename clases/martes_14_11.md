# CLASE MARTES 14 NOVIEMBRE ASTROINFORMÁTICA

última clase hdf5 !

h5repack: orden de archivos, permite ordenar en chunks, reduce tamaño sin necesidad de cambiar tanto el archivo.

h5dump: permite sacar datos directamente hacia la consola

h5ls explorar archivos

### en jupyter

.keys() devuelve lista de referencias asociadas a ese objeto, me devuelve todos los grupos, el grupo principal es el grupo raíz.

si yo hago f.create_group("Data") me devuelve una referencia del mismo tipo.

f.keys() le pregunta al grupo que está asociado esta referencia

### Exploramos nuestro archivo creado

> f = h5py.File("test.h5", "r")

si el archivo es menor a 250 MB (pequeño)
a menos de q esté comprimido el archivo, debería pesar lo mismo q dice XD osea ocupar en la RAM

> hdfview test.h5 # se abre la interfaz

> h5ls "..." # permite ver qué hay adentro e incluso de manera recursiva : `h5ls -r "..."`

si no puedo usar ninguna herramienta, siempre está python

> type(f) : tipo archivo file

> list(f.keys()) : para pasarlo a lista, 

> f["rand1"]
> f["Data"]

puedo rescatar referencias de esto, asignándole una variable

> r = f["rand1"] # apunta al disco duro no a la memoria RAM

si queremos ver qué es cada cosa, debemos preguntar a las referencias respectivas: `type(r)`, siendo r la referencia del data set

copiar un array de numpy igual, es decir `[:]`

entonces debemos copiar los datos del disco a la RAM, ya que ahora no está en la RAM

> rand_ram = r[:]
> rand_ram

f.close() # no olvidar cerrarloouououoouou

### ATRIBUTOS (recordar que ya vimos ### GRUPOS y ### DATASETS)

> r+ : leer y editar, r solito es sólo leer

para usar atributos, la liberería incorpora una componente (que es un objeto) que se llama `attrs` y está asociado a todos los objetos HDF5, ya sea dataset, file o group.

Los atributos sirven para agregar **_información_** adicional que permiten tener registro de qué son los datos incluidos. Estos son **metadatos**

### METADATOS

útiles en el contexto astronómico, por ej:
- fecha de creación y dónde lo creé
- versión del código que utilicé
- modificaciones a la versión utilizada
- parámetros utilizados
- opciones de compilación, relavante para códigos de bajo nivel
- naturaleza de los datos (qué son?)
- unidades de medida
- etc ...

Si hago mi fn de luminosidad, tomo el histograma y los bines y los meto a archivo hdf5 **DE INMEDIATO !!!** lo ahorro para el futuro, cargar de vuelta del archivo con hdf5 its a candy 

> f = h5py.File("test.h5", "r+")
> type(f.attrs) : Esta referencia `f.attrs` permite manipular los atributos del archivo, es decir, asociados al grupo raíz `\`.

> f.attrs.keys() : para saber los atributos asociados de este grupo

> f.attrs["Description"] = "este es un archivo de ejemplo creado en clases"

> f.attrs.keys() ahora me mostrará ["Description"]
> f.attrs["Description"] : printea el contenido, es decir : "este es un archivo de ejemplo creado en clases"

> f.attrs["Fecha"] = "2023-11-14"

con esto puedo extraer la info que yo quiero en específico sin explotar el kernel, por ejemplo cuando tengo 1 millón de datos

los atributos pueden estar asociados a cualquier grupo o dataset del HDF5

header : registro de lo hecho, git de imágenes :o, si quiero replicar eso: me invento un log o lo ke sea para jugar con los atributos.

ej: agregamos info al grupo "Header":

> f["Header"] : referencia de un grupo de HDF5, si le pongo un punto para acceder al atributo

> f["Header"].attrs.keys()

### método 1 
> f["Header"].attrs.["Clase"] = "HCAI 2023"

### método 2 
> g = f["Header"]
> g.attrs["Clima"] = "Sunny" 

### método 3
> a = g.attrs, o también:
> a = f["Header"].attrs
> a["Hora"] = "12:44"

Luego podemos ver los atributos asociados:
> f["Header"].attrs.keys()

También podemos asociar atributos a dataset:
> f["rand1"].attrs["Desciption"] = "Array de números aleatorios que siguen una distribución normal con sigma en 0"

>f.close()

en HDF5 no es como herencia, es decir los atributos de raíz se quedan en raíz y los que están en grupos se quedan en grupos.

_Es muy importante guardar cómo se guardan los datos, cómo se creo el archivo y así evitar que deje de ser inútil a corto (o largo) plazo_

_revisar qué caracteres no se pueden incluir_

Todos los archivos de GADGET contienen HEADER, grupo lleno de atributos con info. original 

Almacenar en paralelo, cuántas cosas hay en c/archivo y cuántas cosas hay en total.

Opciones de configuración, todas las compilaciones del código, aunque los atributos tengan 0 info lo que importa es que ese atributo fue usado al momento de codiguear.

Seed : números aleatorios pueden ser los mismos incluso cambiando de pc.

Parámetros de entrada: usar encapsulamiento ! POO, un obj que guarde todo! radio, límites, treshold, para que después si algo no resulta no esté meses buscando la diferencia ?????

scale factor es 1 a z=0, `scale factor`: cómo varían las distancias cuando cambia el redshift en las simulaciones.

atributos son flotantes, no arrays, no ocupan tanto espacio

