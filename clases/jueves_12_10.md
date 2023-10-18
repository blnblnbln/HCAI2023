# CLASE JUEVES 12 OCTUBRE ASTROINFORMÁTICA

no sincronización de los procesos :o

cómo sincronizo que está pasando al mismo tiempo

representación numérica 0 a 10 

coeficientes con potencias de esa base

parte decimal: exponente negativo

base 10 es en la vida real

pero todo representado en base binario, es decir base 2 

resto de la operación me dará factor alfa sub 0, todo dividido b

le resto alfa sub vero, lo divido por b y me queda todo el factor 

para pasarlo a cualquier base, binario, etc, cuaternario etc

en las potencias negativas es lo mismo pero al revés

en principio no sé cuántos dígitos 

devuelta tengo mi base, tengo mi coeficiente y listo 

placas paralelas : placas de silicio

transistores , tengo carga o no tengo carga, 1 o 0 

entender que número se almacena en la memoria en formato binario y escribirlo en el silicio


132 requiere 8 bits = 1 byte, 132 = 10000100

humanos entendemos número decimal, por lo tanto el camino para la computadora es de ida y de vuelta, lo transforma a binario para 

entenderlo y luego lo transforma a decimal para que nosotros entendamos el resultado

### int

clásico de precisión simple: 32 bits (4 bytes), 31 bits para usar porque 1 se reserva para ser el signo, -2^31 y 2^31

unsigned int : sólo enteros positivos, no considera espacio para el signo

long int : 64 bits, entero con precisión doble, 

python de forma excepcional, el entero de input NO TIENE LÍMITES !!! define automáticamente cuántos bits necesita para su 

representación y los va adaptando a tiempo real 

cambiar tipo de dato al array de numpy NO SE PUEDE CAMBIAR !!! pq hecho en otro lenguaje

### números flotates

buscar en wikipedia sobre mantisa y exponente

decimal, necesita almacenar un signo, una mantisa y un exponente (sesgado para incorporar signo)

cada de los 23 corresponde a los decimales en base binaria, los beta, asumiendo que el primero vale 1

si le sumo un número muy pequeño no podrá hacer la suma

tiene límite mínimo y máximo 10^38 y 10^-38

C introduce tipo double que usa 64 bits


se sigue prefiriendo 32 bits porque ahorra memoria

si pongo 1e50 puede ser un valor que yo si necesite y pueda trabajar entonces me arroja warning de overflow (tb existe underflow)
, pero si pongo 1e400 es obvio que será infinito

en mi compu me tira todo infinito, puede depender de la capacidad de mi compilador para darse cuenta de que me podría enviar un warning

### consideraciones
- errores de redondeo
- representación flotante determina un épsilon e de resolución, de tal manera que la operación (x+2^-e) es equivalente a X


todos los software tienen ese épsilon, excepción python con enteros, tienen completitud en representación 

significa que con ese exponente y si le sumo 1 ???? no tendrá mantisa suficiente, se lo va a comer, sería underflow porque tengo potencia, es mejor trabajar con logaritmos
 
- representación decimal de los números almacenados digitalmente no necesariamente refleja la precisión del número, no me muestre todos los decimales, lo trunca, por lo que el número no siempre es el número real, puede tener menos precisión.
- los caracteres y array de caracteres conocidos como strings son representados de forma equivalente a números enteros de 8 bits (1 byte), para un operador un carácter es un entero muy chiquito, entre 0 y 255, se toma el nº, se mapea con ascii y se reemplaza, siempre son mapeos entre números enteros hasta el 255

### almacenamiento en archivos de texto

ascii, archivo de texto todo archivo que consiste en conjunto de caracteres ordenados de forma secuencial
todos son archivos de txt, los csv, xml, py, sh, html

en ascii perdemos info porque el print trunca, es mejor HDF5, por eso es importante saber cómo guardar los datos para no perder info.