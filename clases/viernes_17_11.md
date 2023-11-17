# CLASE VIERNES 17 NOVIEMBRE ASTROINFORMÁTICA

### BASES DE DATOS Y SQL

### bases de datos:
software, sistema organizado para almacenar, administrar y recuperar grandes cantidades de _información_ de manera eficiente y segura.
Como es un software, presenta un servicio para las demás aplicaciones que actúan como clientes de la base de datos, esos clientes son usuarios, personas, por ej a través de SQL donde el software recibe la info y decide con métodos internos (algoritmos), ya no me preocupo de organizar por columnas o filas (campo o registro) pke el algoritmo sabe hacerlo.

Cualquier sitio web es: USER -> DBSM (DataBase Management System, gestiona solicitudes de Users)

Estos servidores asegurar la integridad de los datos

ej: ADS o VO observatorio virtual

Bases de datos estáticas o dinámicas, le puedo agregar o quitar datos.

Los usuarios siempre son estáticos, osea depende del sitio web, en ADS sería estático. si fuera creador sería dinámicos porque pueden agregar o quitar datos.

Base de datos es el servidor que administra los datos, después hay una aplicación que permite conectarme con los datos.

DBMS vienen con sus aplicaciones propias.

Dependiendo de los datos y cómo se organizan yo determino con qué usarlos.

**Bases de datos**
- _relacionales_: se expresan como tablas
- _no relacionales_: ADS ? 
- _jerárquicas_ : usan trees, no tablas
- grafos: todos los objetos tienen conexiones no estructuradas (sirve para arrays neuronales :o)
- POO: estructura, clases y herencias

más utilizada es: __relacionales__ puedo almacenar datos numéricos, tipo string, categóricos

Decisiones de cómo almacenar datos lo dice el software

**Esquemas de las bases de datos**
Estructura para visualizar bases de datos, similar a diagrama UML en el sentido q visualiza.

registro es la info que quiero agregar a mi base de datos, esta tabla tiene campos.

Permite conectar objetos con otras tablas dentro de la misma base de dato, gracias a q está construida sobre el software
_relaciones base_: si lo organizo en campos y registros, para la base de datos no es lóigifoc, relación base es q todo el es mismo 

después hay otras ... 

ej esquema: cada campo de la tabla: nombre, correo, etc.

Cuando tengo que hacer demasiados ! request, homogéneos pero distintos, ahí es problema para la base de datos, porque cada request tiene un lag, hacer 3millones no es buena idea, es un problema de funcionamiento. 

### SQL: Structured Query Language**
Lenguaje informático específico diseñado para administrar y recuperar información de sistemas DBMS (el lenguaje de programación es lenguaje informático formal). Permite incluir álgebra, cálculo relacional, es como sifuera un lenguaje de teoriía de conjuntos, así podemos realizar cambios en la base de datos

- Uno dice qué quiero, no cómo, el algoritmo es el responsable del cómo.
- Operaciones estándar (Create, REad, Update), también puedo hacer usuarios: accesos.
- Independiente de la plataforma de base de datos que esté usando, funciona en múltiples DBMS.
- Utiliza instrucciones o comandos específicos, para controlar acceso.

SQL: instrucciones de solicitud **SIEMPRE TIENEN QUE TERMINAR CON ;**
- `SELECT` y `FROM`: Selección de tablas y datos , siempre tiene q estar disponible el nombre de las tablas. Pueden ser en mayúscula o minúscula. Uso `select` para decirle al query que quiero esto de la info y el `from` es para decirle de dónde lo quiero sacar. Utilizado para seleccionar datos de una o más tablas

> `SELECT` columnas `FROM` tabla
> `SELECT` Nombre, Correo `FROM` Usuarios

- `WHERE`: Aplicación de filtros, permite filtrar registros que cumplan ciertas condiciones.

> `SELECT` columnas `FROM` tabla
    `WHERE` condición;

La condición puede tener AND, OR, IN, BETWEEN, LIKE

> `SELECT` * `FROM` Usuarios `WHERE` ID = 5

- Selección de campos: `SELECT` también permite definir qué campo desea leer

Selección de todos los campos:
> SELECT * FROM tabla;
Selección de campos específicos:
> SELECT campo1, campo2 FROM tabla;
Ejemplo:
> SELECT Nombre, Fecha FROM Usuarios

- Limitar Resultados `LIMIT`: limita número de registros solicitados.

_columnas categóricas_: datos clasifican, early type y late type por ejemplo, me establece categorías, no rangos pero sí operadores de igualdad.

doble punto .. : jerarquía