### CLASE JUEVES 14 SEPTIEMBRE ASTROINFORMÁTICA

RECAPITULACION, 
Para que sirve cada cosa? 
   - MPI > libreria para hacer correr cosas en paralelo
   - Hay cosas que estan solo en C y fortran sobre todos las cosas de red
   - bajo nivel en GPU > CUDA, OpenCL
   - TSL, Ruby
   - Lenguajes desarrollo machine learning > LISP
   - Python con R > Estandares opensource ciencia de datos (R no es un lenguaje como tal, ya que se hizo para estadistica)
   - C dentro de Python con Cython
   - JAVA lenguaje interpretado > virtual machine trae cosas para hacer ventanas bonitas
CATEDRA CLASE ANTERIOR:
Arrays y memoria estatica ,
Se parecen a python pero no son lo mismo
   - python > indexacion
   - C > solo corchetes ajhjshja 
Meterle numeritos a los arrays en C en con doble loop, si te gusta la topologia entonces hacer una funcion bilineal que 
lleve de un espacio a otro
__Punteros y memoria dinamica:__
El entero se puede interpretar como yo quiera si tengo el puntero!!
C no reclama por las barbaridades.
### Memoria dinamica:
   - Para acceder a la memoria dinamica antes habia que hacer una cosa rara, pero con el puntero ahora es directo
   - malloc (instruccion barbarica): 'Sistema operativo dame esta cantidad de memoria para lo que yo quiero'
**Recordar x++ o x+=1**
TAREA:
makefile sirve para dar instrucciones y compilar muchos archivos necesario para correr un programa
en particular para C. Da instrucciones en bash dentro de un archivo por eso se llama makefile que sirvan
para compilar muchos programas de manera automatica a partir de un solo archivo

***

punteros y memoria dinámica, 
malloc reserva memoria, sizeof(int) , 
este size me devuelve en bytes cuánto espacio de memoria necesito, 

puntero ventaja: acceso directo a memoria, paso por referencia (paso la dirección de memoria), no hago copia, también sirve para hacer estructuras de datos dinámicas, para hacer árboles, redes, enlaces

complicaciones: si uso un punto no inicializado puede ser un gran error, si intento acceder a un valor , puntero nulo, segmentation fault x_X y fugas de memorias, fuera del borde de array, dato que se creó después de un cómputo y quedó perdido en la memoria RAM

strings son objetos inmutables en python, 
probablemente porque sean un array de C , 
malloc retorna memoria reservada , 
y devuelve la dirección del trozo reserva, 
la reserva dura hasta que se libera o hasta que se termine el programa , 

char necesita 1 bite , 
usa RAM, si se llena empieza a llenar sWP, 

en python no existe makefile, 
makefile automatiza el proceso de compilación, 
El objetivo de Makefiles es compilar cualquier archivo que sea necesario compilar, en función de los archivos que han cambiado. Pero cuando los archivos en idiomas interpretados cambian, no es necesario volver a compilar nada. Cuando se ejecuta el programa, se utiliza la versión más reciente del archivo.

makefile sirve para dar instrucciones y compilar muchos archivos necesarios para correr un programa en particular para C

***

### 2.3 GNU MAKE 
no sólo sirve para compilar sino para automatizar procesos, 
make permite hacer una lista ordenada de qué son las cosas q kero crear, q necesito para crearlas, 
compilación: generar código objeto y liker, 
herramienta q borre automáticamente los .o ,  
limpieza de temporales se puede automatizar, 
y decidir dónde va la instalación final , 
make puede identificar automáticamente hasta dónde se modificó para compilar solo lo necesario , 
sólo compila los archivos modificados ,
necesito el software Make ,
***brew install make*** ,
make es un archivo de texto con cierta estructura  ,
objetivo: dependencias … receta ,
necesita el tab ! en el tab pongo mi regla, un -o crear un archivo ejecutable en base a archivos objetos : es el linkeado, -o dice el nombre del archivo de salida, 
-c compilado y linkeado, depende si es .c o .o, C sabe, 
se compila como gcc -o contarpares contarpares.c , 
make


makefile, make es un lenguaje propio,
makefile no es un script como los .py o .sh o .jar,
makefile es un archivo de config, make lo lee entero según make cree,

make hace reemplazos literales de las variables

cd ../2.3

cp ../2.2/myhola/*.c .

cp ../2.2/myhola/*.h .

cp programa.c hola.c

para cumplir el objetivo empiezo a buscar dependencias,
busco regla para esa dependencia ,
clean no tiene ninguna dependencia, cada vez q se llame clean ,
.PHONU : clean ,
make tiene reglas implícitas, no le tengo que decir cómo compilar un .C ,

%.o toma cualquier archivo .o ,
make compila automáticamente 