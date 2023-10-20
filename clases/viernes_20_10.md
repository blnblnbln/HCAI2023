# CLASE VIERNES 20 OCTUBRE ASTROINFORMÁTICA

obligación de pensar en los datos que estamos trabajando

puntos a considerar sobre sus datos:
- almacenamiento: disco duro dura 5 años :c, like vinilo y agjua 
- composición: header de los fits, vectores para encontrar los espectros en multislit, unidades tabla. Datos relacionales: , Datos no relacionales: arxiv o ads porque no están estructurados, no tiene estructura fija, la info no depende de otra cosa. Homo o Heterogéneo: mezcla de int con float, falta precisión o otro tipo de dato.
- tamaño: hacer predicciones de cuánto pesará mi dato, tiempo de vida
- comunicación: hacer que mi dato sea usado por otras personas
- escalamiento: ese dato es estático o se modificará con el tiempo, proyectar crecimiento de los mismos, agregar o quitar columnas que estén malas?

# almacenamiento en texto plano

archivos donde la representación de los datos se realiza en texto sin formato. Tomar archivo, pasarlo a ascii. Es un formato simple de leer, no contiene datos masivos. Ojo si es info que no quiero perder

**.txt**, **.csv**, .dat no es nada, una extensión que uno se inventa

ventaja: cualquier computador lo puede leer

ventaja csv contra libres: puedo tener espacios vacíos sin datos si pongo dos comas consecutivas , , ya que la separación es por comas, le pone NaN

función open permite obtener
open: primer argumento nombre del archivo, 2 argumento es si quiero escribir "w" o leer "r", para hacer ambos buscar el comando, leer manual función open

función write no funcionan en tiempo real !!! es una cajita mágica en el software que se llama buffer (en memoria RAM), hasta que se completa ???? y llena el bloque ???? y entonces pasa al disco, porque escribir de una vez la info es mucho más rápido que escribirlo de a poco por piezas.

flush escribe en tiempo real, le dice al objeto no importa el buffer escribe altiro, es malo a futuro pero a veces funciona ! , comuniación cruzada

si ocupo el write, para que entre la info y esté en el archivo ocupo f.close()

with crea un objeto temporalmente, tiene un objeto que va a desaparecer cuando termine la instrucción ?

si quieres hacer un archivo lo recomendable es usar with

:d entero, si tengo flotante entonces :d hace que eso se represente como enteros

open cuidado !!!! quiero leer no sobreescribir, automatizarse a escribir open 'r' 

no es bueno hacer archivos de txt masivos, en ese caso no sirve numpy o pandas, es mejor open para más de cientos de GB

readline devuelve una lista, donde cada linea es un string porque archivo de texto duh

volvemos a usar f porque usamos f.close()

el with lo cierra solito, x eso es + bkn

readline me devuelve la línea en lacual está trabajando el archivo este momento, me devuelve la primera, si lo compilo de nuevo me devuelve la segunda y así, queda ahí, no regresa al principio, porque el proceso de moverse por el disco es caro computacionalmente, solución a este problema: que la aguja se quede ahí y no vuelva al principio. f.readline()

seek tiene indicadores, principio: f.seek(0), final, entremedio

como pasar de string a número? tengo que saber qué tipo de dato es, lo transformo con: float(l.split()[1])
l.split