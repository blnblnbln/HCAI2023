# CLASE MARTES 10 OCTUBRE ASTROINFORMÁTICA

*analizar ejemplo de super

*preguntar fecha portafolio

*buscar cómo encontrar la versión anterior de un archivo en github

### documentación de software

no hacer cosas sin escribir por qué lo hago

objetivo documentación: 
si veo el archivo vacío, y si no vi el diagrama UML, tratar de desencriptarlo es muy complicado

documentación más necesaria mientras más complejidad en código

ayuda al yo del futuro <3

eficiencia ! no perder tiempo, documentación no! es pérdida de tiempo

público objetivo: usuarios, saber dónde está, qué hace, sus limitaciones, saber hacer funcionar el código en su ambiente

desarrolladores: …

¿qué se debería documentar?

readme

se pueden hacer tutoriales de uso, o sitio web, etc

mientras mejor esté la documentación final más personas pueden usar el software

si mi proyecto es pequeño no es necesario el wiki

documentado siempre: el código fuente, conocido como documentación interna, ahí llega solo la gente entusiasta o la que lo necesita

si quiero facilitar, qué debo documentar siempre

si hago creación de archivos, esta creación es mental, esas ideas deben incluirse en la documentación

dejar registro de por qué existe

documentar las clases, funciones, métodos

siempre documentar la función para saber qué hace, qué argumentos tiene, qué retorna y cuáles son sus limitaciones

i.e. todos los input y output, ojalá los tipos de input

ej: suma, su limitación no aguanta números complejos

sobreindicaciones, describir el propósito, no el cómo

todo esto es la parte técnica

manual para usuarios y manual para técnicos

**buenas prácticas**
- claridad
- actualizada: anotar si hago cambios, para el yo del futuro
- consistente: si pongo parámetros en una parte y en la otra solo una línea, nop, que sea todo homogéneo, si se profundiza el código: deep manual
- objetiva, no es necesario describir, sino justificar, el por qué hice eso

jupyter notebook diseñado para que uno documente

**documentación de código fuente**

bloques de código:
- si gasté tiempo en una línea de código, entonces ahorrar ese tiempo para posterior y documentarlo
clases:
- descripción de atributos, métodos u objetos junto a su propósito para cada clase
- documentación de privados más técnica, no es parte de la docstring
métodos:
- tener overview de los métodos más importantes de las clases y ojalá un ejemplo de uso 

proyectos más grandes necesitas más documentación, como pag web

**documentación externa**

**¿qué pasa si necesito doc externa de ?**

en función, uno como usuario espera encontrar en una función:
1.  texto q describa qué hace la fn, para qué sirve y las limitaciones

2. los parámetros, qué tipo de dato son y qué es y cómo se llaman

finalmente los valores de retorno, qué tipo de dato es el retorno

auto docstrings : visual code :OOOO

para las clases espero el brief (pequeña intro),  qué representa, atributos, métodos

brief, métodos en orden en q aparecen en la 

ejemplo : código q conecta telescopio con computador

crear documentación usando pags web

doxygen no es su foco principal python, pero lo incluye

software GNU y ggraphviz, esto anda bien C++ pero no sabemos con python 

qué tipo de documentación crea? pdf

en html hace la pag web lista para publicar

contra: es un software viejoooooo

vim : ***te sales del intérprete y pones / para buscar , como el cmd+F

otra herramienta: sphinx, diseñado para python

incorpora documentación técnica

es parte de python, se instala con sist operativo, desde conda o con pip

primero git clone el repositorio con url de git y donde lo quiero poner (usar otra carpeta) no lamisma dd esta el del profe

git add b, debe estar dentro del repositorio que descargué