# Documento del Proceso de Desarrollo

## 1. Idea inicial
El proyecto surge de la necesidad de optimizar y sistematizar la gestión del mantenimiento preventivo y correctivo de vehículos automotores (autos y motos). En los entornos cotidianos y en pequeños talleres mecánicos, el control de estos eventos suele realizarse mediante formatos físicos en papel o herramientas de cálculo bidimensionales desorganizadas (como Excel), lo que introduce un alto riesgo de pérdida de datos, falta de trazabilidad histórica y omisión de mantenimientos críticos. 

El objetivo principal fue diseñar e implementar una aplicación de escritorio robusta, intuitiva y centralizada que permita registrar la bitácora de servicios de forma ágil, garantizando la integridad de la información y automatizando los cálculos financieros y operativos asociados a la gestión vehicular.

## 2. Análisis del problema
El sistema identifica y delimita dos perfiles de usuario principales dentro de su dominio de aplicación:
* **Propietarios de Vehículos Particulares:** Usuarios que requieren un mecanismo de control personal para monitorear el estado operativo de sus bienes, consolidar el histórico de gastos financieros invertidos en mantenimiento y planificar alertas futuras.
* **Administradores de Pequeños Talleres:** Operadores que necesitan registrar de forma estructurada los servicios prestados a los vehículos de sus clientes, ofreciendo un soporte transparente de los trabajos realizados.

### Requerimientos Funcionales Esenciales
Para resolver la problemática planteada, el software mitiga y controla tres factores operativos críticos:
* **Prevención de Omisiones:** Automatizar el seguimiento de servicios esenciales (cambios de aceite estructural, pastillas de freno, alineación y balanceo) antes de que afecten la vida útil del motor o la seguridad del usuario.
* **Consolidación Financiera:** Calcular de manera automática, exacta y acumulativa el costo monetario total invertido por cada vehículo en base a su historial.
* **Restricción Cinemática:** Controlar estrictamente que las variaciones del kilometraje actual y de los servicios sigan un orden cronológico y secuencial lógico, impidiendo anomalías o registros incoherentes.

## 3. Diseño de la solución
Para garantizar un software mantenible, escalable y con bajo acoplamiento, se implementó el patrón arquitectónico **Modelo-Vista-Controlador (MVC)**, fragmentando el sistema en tres capas claramente diferenciadas:

* **Modelo (`app/models/`):** Capa encargada de la persistencia temporal, el estado y las reglas de negocio puras. Está constituida por las clases core `Vehiculo` y `Servicio`, junto con el componente de lógica global `GestorBitacora` (`gestor.py`). Aquí reside la lógica computacional y los mecanismos de validación mediante expresiones regulares (Regex) y condicionales lógicos.
* **Vista (`app/views/`):** Capa de interacción con el usuario. Desarrollada con la librería externa de interfaz gráfica avanzada `CustomTkinter`, proporcionando una experiencia visual estilizada, componentes asíncronos y soporte nativo para la conmutación a modo oscuro (*Dark Mode*).
* **Controlador (`app/controllers/`):** Actúa como el puente de comunicación e intermediario lógico (`bitacora_controller.py`). Captura los eventos de la interfaz (clics, ingresos de formularios), invoca los métodos de validación del Modelo, coordina la actualización de los datos y encapsula el manejo de excepciones para evitar fallos catastróficos o cierres inesperados de la aplicación en tiempo de ejecución.



## 4. Implementación
El sistema se desarrolló utilizando el lenguaje de programación **Python 3.14**, estructurado de forma modular y fundamentado en los pilares de la Programación Orientada a Objetos (POO):

* **Composición:** Un objeto de la clase `Vehiculo` actúa como un contenedor de alto nivel que posee una relación de composición directa con una lista dinámica de instancias de la clase `Servicio` (`list[Servicio]`). Un servicio no tiene sentido de existir de forma aislada sin un vehículo asociado.
* **Encapsulamiento:** Los atributos críticos de las clases de negocio se encuentran protegidos, forzando a que cualquier alteración de estado o inserción de datos pase obligatoriamente por los métodos constructores (`__init__`) y métodos de validación internos, donde se interceptan los datos anómalos.
* **Persistencia de Datos Ligera:** Con el fin de cumplir con el requerimiento de persistencia sin introducir la complejidad o dependencias externas de un sistema gestor de bases de datos relacionales pesado, se diseñó un mecanismo de serialización y deserialización de objetos hacia un archivo plano estructurado en formato **JSON (`bitacora.json`)**. El sistema realiza operaciones de lectura I/O al inicializar la app y escrituras automáticas ante cada mutación del estado.

## 5. Pruebas
El aseguramiento de la calidad del software (QA) se estructuró mediante un entorno de pruebas unitarias automatizadas utilizando la librería estándar de la industria **`pytest`**, aislado en el directorio `tests/`. Se diseñaron suites de pruebas enfocadas en dos espectros operacionales:

1. **Flujos Normales (Casos de Éxito):** Validación del comportamiento ideal del sistema, incluyendo la instanciación de entidades vehiculares con parámetros óptimos, la inserción correcta de registros de mantenimiento en la lista de composición y la precisión matemática del método encargado de computar el gasto financiero acumulado.
2. **Flujos de Error (Excepciones Controladas):** Verificación de las barreras de seguridad del modelo de negocio. Se programaron pruebas específicas para comprobar que los mecanismos de control disparen de forma correcta excepciones nativas de tipo `ValueError` al detectar intentos de violación de reglas de negocio, tales como el ingreso de costos monetarios negativos o kilometrajes inversos.

## 6. Dificultades encontradas
Durante la fase de integración y control de calidad en el entorno local, se identificaron y solventaron dos problemas técnicos de alta criticidad:

* **Incoherencia de Tipos y Mutación en Datos de Prueba:** En la etapa inicial de QA, las pruebas de software fallaban arrojando estados de error (`FAILURES`). Tras una auditoría del archivo `tests/test_modelos.py`, se determinó que los datos de prueba suministrados utilizaban un formato de placas con caracteres especiales y guiones (ej. `ABC-123`), los cuales violaban las expresiones regulares de validación estricta programadas en el Modelo de `Vehiculo`. Adicionalmente, el script de pruebas invocaba una importación de un módulo inexistente o desactualizado denominado `gestor_bitacora.py`. La dificultad se superó reestructurando completamente el script de pruebas, normalizando el formato de las placas a cadenas alfanuméricas puras y corrigiendo el direccionamiento de importación hacia el archivo real `gestor.py`.
* **Restricción de Ámbito en el Entorno de Ejecución (Windows PowerShell):** Al ejecutar el comando secuencial de `pytest` desde la terminal nativa de Windows, el intérprete de Python lanzaba errores de tipo `ModuleNotFoundError` debido a que el entorno global de la consola local no reconocía la raíz del proyecto dentro del árbol de directorios de la aplicación. Se solucionó inyectando y configurando de manera explícita la variable de entorno del sistema `PYTHONPATH` con la ruta absoluta del espacio de trabajo antes del lanzamiento del motor de pruebas.

## 7. Mejoras futuras
* **Subsistema Predictivo de Alertas Temporales:** Desarrollar un módulo asíncrono en la capa del Controlador que evalúe de forma heurística el kilometraje del vehículo, desplegando notificaciones emergentes visuales (*Pop-ups*) en la Vista cuando falten menos de 500 kilómetros para el umbral del próximo mantenimiento preventivo estandarizado.
* **Migración a Motor de Persistencia Relacional:** Reemplazar el archivo estructurado JSON (`bitacora.json`) por un motor de base de datos embebido e indexado como **SQLite**. Esto permitirá soportar una mayor concurrencia de datos, la ejecución de consultas transaccionales complejas mediante lenguaje SQL y garantizará el cumplimiento de las propiedades ACID en volúmenes de datos masivos.

---

## 📸 Evidencias del Proyecto y Control de Calidad (QA)

### 1. Interfaz Gráfica y Menú Principal
Muestra el diseño visual del sistema en modo oscuro desarrollado con CustomTkinter.
![Menú Principal](capturas/menu_principal.png)

### 2. Funcionalidad y Registro
Evidencia del comportamiento del programa al interactuar y registrar datos en los formularios.
![Registro de Mantenimiento](capturas/funcionalidad_registro.png)

### 3. Persistencia de Datos (JSON)
Confirmación de que los registros se salvan de forma permanente en el archivo local.
![Archivo JSON](capturas/evidencia_datos.png)

### 4. Pruebas Unitarias Automatizadas (Pytest)
Reporte exitoso de la terminal de QA tras corregir las importaciones y la lógica de placas.
![Pruebas Exitosas con Pytest](capturas/pruebas_pytest.png)

### 5. Repositorio en GitHub
Estado del control de versiones en la plataforma web con la estructura final de carpetas.
![Repositorio de GitHub](capturas/repositorio_github.png)