# CLASE MARTES 07 NOVIEMBRE ASTROINFORMÁTICA
formato es respuesta a un problema que tengamos, si el problema es comunicación por survey, hablar de la comunicación es fundamental, quiénes lo van a leer, cómo lo van a leer, esto definirá el mejor formato.

Que no haya dependencia de formato, que se adapte a cualquier formato porque sino perdemos info por limitancia.

Crearemos un archivo de texto plano, de formato libre

pensar en estrategia de lectura antes de programar

trabajar con datos en memoria RAM (ej una operación matemática)suele ser 1 millón de veces más rápido que la misma operación en el disco duro

with cierra el archivo, por eso es mejor que open

en codes , seguimos usando el jupyter "datos"

string son arrays

puntero ! igual que C, que dice exactamente en qué sector del disco está.

- readline: se detiene en el primer salto de línea que encuentra, no se mueve, no vuelve
- seek: vuelve al principio, o moverse dentro del archivo
- readlines: lee todo el archivo y queda en la última

readline(s): lee, asigna referencia, y te devuelve el objeto asignado que es una lista

exclamación ! para llamar a bash

con print puedo llamar a una línea en específico ej : print(f.readline(40)) , o asignarle una variable a esa fila específica, si pongo f.readline() solito me lee la primera por defecto como es el método por defecto.

### parseo: tomo algo de una cosa y le sako lo k me sirva ????

split subentiende que existen separadores entre strings, espacios, tabs, salgos de línea, etc, todos esos substrings los mete a una lista. El primer elemento lo toma como string.

No puedo sumar strings con string, eso es concatenarlos. 

### leer
readlines para leer archivo completo

csv no tiene espacios, tiene comas, ojito, es importante comunicárselo al programa

**unpack** empaquetamiendo, toma un registro y lo desempaqueta, toma c/u de mis registros, que esté por las columnas no por los registros, buscar ! y releer sobre registro y campo :c don't remember. cambia el shape, quedaría (2, 1500000)

abrir texto con numpy : accesibilidad a los datos por columnas queda restringida, restringe forma que lo leemos a que sea por registro

registro : filas? donde cada galaxia tiene campos: columnas: luminosidad, etc

pandas muy bkn
para pandas y csv es normal tener header, si no tengo toma la primera fila de dato como header y eso está mal. Solución: header=None, entonces sabe que no tenemos header. Le podemos agregar nombre a las columnasSigue estando malo porque agregó un índice, solución: index_col=0, sep=' ' para que separe los datos

ventaja de pandas sobre numpy: tabla organizada y accesible, y tiene control de los datos omitidos(ej: NaN o espacio). Otra ventaja: subentiende los tipos de datos, no debería tener problema si es str, en cambio np necesita info detallada de datos que son no homogéneos.

desvantaja pd sobre np: versatilidad para hacer cosas simples, no matar moscas con cañón ! jeje
ncesito saber pandas para usar pd, no necesito saber numpy para usar np

ventaja: leer columnas gigantes

pddata1 = pd.read_csv('datos.txt', header=None, sep='\t', index_col=0, names=['index', 'value'])

chunksize : será un iterador, cuántos registros quiero leer por c/iteración del iterador.

concepto importante 

suma de chunk es diferente a suma de np, probablemente np es mejor pq la hace de una sola vez , es razonable que la de 