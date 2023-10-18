# CLASE JUEVES 07 SEPTIEMBRE ASTROINFORMÁTICA

C creado en los 70 y C++ en los 80
C++ no es un lenguaje de programación en si mismo, es una extensión de C, incluye librerías de C y además incluye las de C++, es orientado a objetos, C solito nop
curva de aprendizaje mayor en C++
mayor diferencia: la arquitectura dependiendo de si ocupa 32 o 64 bits, eso define cómo se almacenan las variables en la memoria 
gestión manual de la memoria 

agregar apuntes
o clases
al portafolio
contribución al conocimiento :)
agregar códigos , sincronizar en repositorios
guardar problema y solución !!!!
es común hacer el mismo error y nos evitamos el proceso de búsqueda de nuevo 
actualizar portafolio.

### LENGUAJE C
javascript owo
python está escrito en C
datos estáticos, esta variable es entero, si lo trato como flotante, lo transformarán a entero para que esté acomodado al formato 
cuidar que el ejecutable compilado no esté transformando float to int or int to float
no es bueno empezar por C, pero ya sabiendo programar es simple aprender C
permite manejar memoria
claves: ; y } , equivalente a salto de línea y a indentación respectivamente
sí indentar! aunque no sea necesario
"#" : lo toma y lo interpreta , no es comentario, es una instrucción, lo hace el pre-procesador de C
hay 2 tipos de comentarios, // es una línea y el /* o */ comentar varias lineas
vim con “i” comienzo a escribir y escape me voy al modo comando

error: no permite usar, el codigo no funciona
el warning te avisa pero te lo compila igual.

### función main necesita llave 
gcc es el compilador, a.out es el 
void es para no ponerle return, es equivalente al none en python pero para tipos de datos 
int necesita retorno, void no necesita retorno
main es obligatorio

respuesta a por qué no puedo descargar cosas o tengo problemas con ….
*compilación con GCC*
compilador megapoderoso
entiende cuando el código está en C
¿cuál es el -o pero en mac?, el q cambia el nombre del .out
tokiens: etiquetas a objetos virtuales , saber que int es una palabra requiere un tokien
no se definen cosas dentro de un loop !!! error semántico
then recién traduce, and only traduce
luego enlazador y ensamblador
pasos separados
optimización se agrega con -O, la más probada es O2
RTFM: -O, optimizadores
depuro y luego O2, si creo que mi algoritmo está correcto
mostrar advertencias -W
-l más el nombre de la librería
-Wall me da warnings, 
si quiero instalar librerías, las instalo del /lib
-L agregar directorios de librerías estáticas o dinámicas
header de la librería está en include (en mi caso en local).