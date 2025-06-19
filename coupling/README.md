# Coupling and Dependency Injection

## Introducción

La **inyección de dependencias** es un patrón de desacoplamiento. Un código desacoplado está formado por unidades de código (funciones o clases) independientes y con una función específica que pueda modificarse mediante sus argumentos. Esto permite reutilizar esas unidades para otros fines (nuevas implementaciones, tests) sin tener que modificar (o incluso romper) el código existente.

### Principios del desacoplamiento:
- No definir el comportamiento de un objeto dentro de la misma función que lo va a utilizar.
- El comportamiento de una clase/función está definido por:
  - Su código.
  - Composición de clases (evitar el uso de herencia).
  - Las variables que utiliza (pasar las variables como argumentos de la clase/función).

---

## Versiones y Soluciones

### v1: Problema inicial
- **Clase:** `S3FilesEntrypoint` acoplada globalmente a los argumentos que definen su comportamiento.
- **Problemas:**
  - Imposible reutilizar con otros fines (por ejemplo, subir documentos a un bucket diferente o realizar tests con un bucket de pruebas).
- **Potenciales soluciones:**
  - Pasar las variables como argumentos → Modificar (romper) el código existente.
  - Duplicar la clase → Repetición de código (violación del principio DRY).

---

### v2: Composición de clases
- **Solución:** Definir las variables de S3 en la clase `bedrock` mediante composición de clases.

---

### v3: Nuevo acoplamiento
- **Problema:** Surge un nuevo acoplamiento entre el servicio `bedrock` y `S3FilesEntrypoint`.
- **Conclusión:** Para lograr el desacoplamiento, debemos definir el comportamiento de las funciones lo más cercano posible a la función que nunca es llamada por otras funciones, es decir, la función `main`.

---

### v4: Tests de integración
- **Implementación:** Tests de integración de la capa de rutas.

---

### v5: Uso de `Pydantic Settings`
- **Ventajas:**
  - Establece un orden de prioridad automático.
  - Permite el uso de un archivo `.env` por cada entorno.
  - `.env` en `.gitignore` ignora únicamente la definición de las variables, pero no su declaración.
  - Carga automáticamente las variables del SSM.
  - Permite definir cadenas complejas (por ejemplo, strings para conexión a bases de datos).

---

## Qué definir como dependencias?

### Ejemplos:
- **Autenticación**
- **Settings**
- **Sesión a la base de datos** como dependencia (Proyecto `bedrock-api`).
- **Conexiones a AWS** (Proyecto `orkid`).

---

## Uso de `Pydantic Settings` con Proyecto `bedrock-api`

---

## Ideas para mejorar el desacoplamiento

### Limitar el uso de clases:
- **Problema:** La herencia es una forma de acoplamiento.
  - Si modificas el padre, modificas el hijo.
- **Solución:** Composición de funciones.
