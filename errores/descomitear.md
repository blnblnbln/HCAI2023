**Solución a "descommitear" archivos que ya fueron añadidos con `git add` y commiteados con `git commit -m "..."` pero que no pueden ser "pusheados" debido a su tamaño**

Se debe aplicar el comado `git reset` en su modo "mixed" (no soft) que es el que viene por defecto, acompañado del nombre del commit en que fueron comiteados. Este commit se puede buscar usando `git log`.

> git reset aa415fa7b3d4a17a8f1ea42d362f98d0cc1dcfb2

### nota:
Sólo incluir archivos livianos (códigos, txt).
Para evitar el permiso a commitear o añadir archivos que sean muy pesados, se les puede cortar el acceso desde `.gitignore`, un archivo de texto donde incluyo, por ejemplo, las extensiones o formatos que deben ser ignoradas en caso de agregarlas por error.

> *.fits