# CLASE VIERNES 10 NOVIEMBRE ASTROINFORMÁTICA

tablas se almacenan de forma unidimensional, pero mi tabla es bidimensional con registros y campos
registros: galaxias
campos: propiedades como luminosidad, brillo, flujo, etc.

por registro: lo hace por filas, pero las escribe unidireccional

por campos: lo hace por columnas, forma secuencial en la memoria, después del último registro (valor N) del campo 1, viene el valor del campo 2 del registro 1

si llego a millones de cosas, eso es importante, si tengo cientos no es tan importante.

si tengo 100 propiedades pero necesito solo las masas, en registro sería muy lento porque tiene que hacer todos los registros para hacer 1 array y después eso lo proceso con np o pandas.

si las hubiera organizado por campo, veo el campo que quiero y lo leo consecutivamente en memoria, me salto el buffer y se va toda la línea consecutiva al lugar donde lo quiero organizar.

si tengo un echelle de espectros, mi registro, si quiero acceder a un registro lo más conveniente es buscar un registro y ver todos los campos asociados.

np tiene un array para binarios ??? nontendí, sip, tiene un binary files, para leerlo tengo que leerlo con np siosi porque solo en np estará cómo lo hicieron.
si tengo datos masivos, si son muy grandes o generarán un problema debo decidir si es mejor guardarlos por campo o por registro, esa es la primera pregunta que debo responder.

### HDF 5

en hdf5 puedo tomar esa decisión de forma directa, es un formato libre que permite almacenar info en un tipo de archivo de tal manera que esta info siga la misma estructura q un sist de archivos de un disco duro. ej: particionar un disco, formato de archivo es la estrategia para definir como se organizará la info en un disco duro, todo el pedazo de silicio jaja lol

algo que puede tener directorios o información, archivos el equivalente en hdf5 es : dataset

es un protocolo de almacenamiento, para utilizarlo siosi necesito una librería, por ej en C: lib oficial de HDF group para C
H5py: para python, no es oficial del HDF sino q es only de python, es probable que 

diferencia de lib python hdf5 a la de hdf original, es muxo más linda y simple.
hay 1 paper q compara rendimiento de hdf5 vs base de datos, ambos con muchos datos, después de cierta cantidad de datos es mejor hdf5.

para usar HDF5 global necesito 3 cosas: la lib de hdf5, hdf view para visualizar archivos en una linda interfaz, h5py para usarlo con python.

INSTALAR HDF5

h5ls para visualizarlo
la versión de desarrollo también incluye compiladores: h5c++

### qué puedo tener en HDF5
- GRUPOS: grupo raíz \
- DATASETS: arrays multidimensionales que tienen el mismo tipo de dato. HDF5 permite crear datos nuevos?, no estamos restringidos a los tipos de datos que existen. Dónde están los datsets? están asignados a cualquier grupo creado en archivo HDF5, puede ser dentro de raíz o en cualquier grupos
- ATRIBUTOS: almacenar obj de info, le asigno un nombre y está asociado a los otros componentes de HDF5, asociados a grupos o a datasets. Fueron creados para almacenar info adicional a los datos, ej: unidades, descripciones, versiones, fecha de creación.

si creo un grupo me retorna una referencia, si no me muesra el contenido necesito pasarlo a una lista: list(f.keys())

HDF5 se bloquea cuando está abierto

para almacenarlo necesitan descriptor??? como tar
son tensores, no array, en hdf5

en hdfview: storage layout: garantizo lectura sequencial si es continuo.

-r veo recursivo, si no lo veo con h5ls test.h5

lo guarda en 64 bits no 32, tiene 3 veces la info original del ascii de 20???

cómo lo leo ??? copiar por referencia o copiar por valor?
para acceder a datos HDF5 utilizamos el operador de indexación []

f["rand1"]

referencia a un obj de tipo dataset, type: f8 flotante de 8 bytes

cuidado con los accesos a hdf5
puedo tomar la ref del obj almacenado al disco y hace la operación directamente en el disco, ventaja: puedo corregir un archivo que estaba malo o aplicar un filtro a un dato, desventaja: si no es un disco sólido, la operación es más lenta y puedo perder algo que no quiero por equivocación

brew install hdf5