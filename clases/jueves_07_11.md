# CLASE JUEVES 09 NOVIEMBRE ASTROINFORMÁTICA

> buscar info. sobre JSON y XML

El formato no restringe como guardamos los datos? 
_texto plano_ : 
- .xml: representa un lenguaje de programacion taggeado, donde hay caracteres especiales donde se delimitan campos, en xml se usan las `{}` es un estandar hoy en dia para almacenamiento 
- .json : informacion compleja y estructurada

JSON es un estándar, es útil para metadatos?
XML

### almacenamiento en binario

**binario**: copio directamente la info de la memoria RAM al disco diro, para que la máquina la lea y la cargue donde lo quiero de manera rápida.


### Ventajas:

- Tamaño: utilizará unicamente la cantidad de bits que necesitaré, ninguno extra.

- Rapidez: no tengo que traducirlo, lo copio y lo trabajo como si fuera un array.

- Precisión: no perderé ningún bit de resolución.

### Desventajas:

- Estructura: no puedo llegar y leerlo, debo saber exactamente el tipo de dato almacenado y su orden. Vienen en binario para que nadie lo sepa leer.
- Arquitectura: algunos PC pueden usar representaciones distintas de los datos.

_Endianness_ : orden o secuencia de bytes, leer ! y buscar, puede ayudar si no sé qué datos tengo ??? 

Binario: Usa la arquitectura donde se está corriendo.

wc : cantidad líneas, puede usarse para cantidad de palabras para cuando haces un informe ojito

si hago un array, nunca usar el número 

_unpack_ : darlo vuelta

"*" en python: tomar una tupla y desempaquetarla, ej: *data, elimino la tupla y paso los datos separados por coma

no es un array con los datos sino que son todos los datos que quiero guardar?????


empaquetar: generar un objeto nuevo binary_data

ej_bin = struct.pack("i", ej) es empaquetar en binario, y si ponemos type dice q es bytes

al pack le entrego el valor que quiero guardar más que el objeto

para abrir binario: con open en formato que yo quiera :p 
wb : escritura y binary
se utiliza el mismo método que ASCII : write, pero en bites ????

con ls -lthra veo todo jiji y ahí veo con 8 bytes o ls -l

para leer usamos read también pero con "rb" donde b corresponde al binario

Para usar binario tengo que saber cómo lo escribieron.

Las aplicaciones usan binarios ! 

solo hay caracteres, por eso solo i de int y f de float, no hay string :o

binario guarda la información exacta !!!

