# 🚗 Sistema de Bitácora Automotriz 🏍️

Este proyecto es una aplicación de escritorio desarrollada en Python que permite a los usuarios (particulares o talleres mecánicos) llevar un registro detallado y organizado de los mantenimientos, gastos y el historial de servicios de sus vehículos (Autos y Motos).

> **Tecnologías clave:** Python 3.x, CustomTkinter, JSON (persistencia de datos), CSV (generación de reportes).

---

## 🏗️ Descripción

En los entornos cotidianos y en pequeños talleres mecánicos, el control de los mantenimientos vehiculares suele realizarse mediante formatos físicos en papel o herramientas desorganizadas, lo que introduce un alto riesgo de pérdida de datos, falta de trazabilidad histórica y omisión de revisiones críticas. 

Este software resuelve dicha problemática centralizando la gestión operativa en una aplicación de escritorio intuitiva que automatiza los cálculos financieros de los mantenimientos, previene omisiones de servicios esenciales y mitiga riesgos de seguridad al controlar estrictamente que las variaciones del kilometraje sigan un orden cronológico y secuencial lógico.

---

## 🎯 Objetivo

Diseñar e implementar una solución tecnológica de escritorio robusta bajo el paradigma de Programación Orientada a Objetos y la arquitectura MVC, que permita sistematizar la administración, registro y consulta del historial de servicios automotrices, garantizando la persistencia e integridad de los datos financieros y cinemáticos de los vehículos.

---

## 🚀 Características principales

* **Gestión Centralizada Multi-Vehículo:** Registro y control detallado de múltiples unidades automotrices (Autos y Motos) mediante identificadores únicos basados en su placa vehicular.
* **Consolidación Financiera Automática:** Cálculo en tiempo real del costo monetario total invertido por cada vehículo en base a la sumatoria indexada de su histórico de mantenimiento.
* **Restricción Cinemática Estricta:** Mecanismos lógicos de control que impiden anomalías operativas, validando que el kilometraje de un nuevo servicio sea consistente y secuencial con el estado actual del vehículo.
* **Exportación de Reportes en CSV:** Subsistema integrado que permite migrar las bitácoras estructuradas a formatos de hoja de cálculo estándar para la realización de análisis o auditorías externas.

---

## 🛠️ Tecnologías utilizadas

* **Python:** Lenguaje de programación core para el desarrollo de la lógica de negocio y POO.
* **CustomTkinter:** Interfaz gráfica avanzada para la experiencia de usuario con soporte nativo de modo oscuro y claro.
* **JSON:** Mecanismo liviano de persistencia mediante archivos planos estructurados para salvar datos de forma local.
* **pytest:** Framework de automatización para la ejecución de pruebas unitarias y el aseguramiento de la calidad (QA).
* **GitHub:** Plataforma de control de versiones distribuida para el trabajo colaborativo del equipo.

---

## 🏗️ Arquitectura y Patrones de Diseño

El sistema fue construido aplicando principios de **Programación Orientada a Objetos (POO)** y el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** para garantizar un código limpio, escalable, mantenible y con bajo acoplamiento.

### 🧬 Aplicación de Pilares POO
* **Encapsulamiento:** Las clases `Vehiculo` y `Servicio` protegen sus datos. Por ejemplo, el cálculo del total gastado se realiza de forma interna dentro de la propia clase `Vehiculo`, evitando que factores externos manipulen las matemáticas o alteren los estados de forma arbitraria.
* **Validación de Estado Strict:** Los constructores aplican reglas de negocio estrictas (expresiones regulares para control de placas, restricciones numéricas de costo positivo y orden cronológico de kilometraje), lanzando excepciones controladas (`ValueError`) para proteger la integridad de los datos ante ingresos corruptos o anómalos.
* **Composición:** Un `Vehiculo` contiene una lista dinámica de objetos `Servicio` (`list[Servicio]`), reflejando una relación del mundo real donde el ciclo de vida del servicio depende enteramente de la existencia de la entidad vehicular.

### 📐 Aplicación de la Arquitectura MVC
* **Modelo (`app/models/`):** Gobierna la lógica pura del negocio (`Vehiculo`, `Servicio`, `GestorBitacora`). Maneja de forma exclusiva los datos y la persistencia sin ninguna interacción directa con el usuario (completamente libre de `prints` o `inputs`).
* **Vista (`app/views/`):** Construida con la librería avanzada **CustomTkinter** (basada en tkinter), renderizando componentes gráficos asíncronos y una interfaz moderna con soporte nativo para temas oscuros (*Dark Mode*) y claros.
* **Controlador (`app/controllers/`):** Orquesta el flujo de la aplicación. Actúa como el puente de comunicación: captura los eventos y formularios de la Vista, los envía al Modelo para su validación/almacenamiento, intercepta los errores del Modelo mediante bloques estructurados de excepciones y le pide a la Vista desplegar alertas visuales (*Pop-ups*) seguras sin romper el hilo de ejecución.

---

## 📂 Estructura del Proyecto

La organización modular del espacio de trabajo está segmentada de la siguiente manera:

```yaml
bitacora-automotriz-mvc/
├── app/                  # Código fuente principal (Capa MVC)
│   ├── controllers/      # Controladores e intermediarios lógicos
│   │   └── bitacora_controller.py
│   ├── models/           # Entidades de negocio y lógica core
│   │   ├── gestor.py
│   │   ├── servicio.py
│   │   └── vehiculo.py
│   └── views/            # Interfaz Gráfica de Usuario (GUI)
│       └── grafica_view.py
├── docs/                 # Documentación e informes del proyecto
│   ├── capturas/         # Banco de evidencias de QA y UI
│   └── proceso_desarrollo.md
├── tests/                # Suite de pruebas unitarias automatizadas
│   └── test_modelos.py
├── bitacora.json         # Archivo local de persistencia estructurada
├── main.py               # Punto de entrada de la aplicación
└── requirements.txt      # Declaración de dependencias del entorno

```

---

## 📋 Prerrequisitos

Para ejecutar el sistema, es necesario tener instalado el lenguaje de programación Python en tu equipo.

1. **Descarga de Python:**
* Ve al sitio web oficial: [python.org/downloads](https://www.python.org/downloads/)
* Descarga la última versión estable compatible para tu sistema operativo (Windows, macOS o Linux).


2. **Instalación (Paso Crítico):**
* **En Windows:** Durante el asistente de instalación, **asegúrate de marcar la casilla que dice "Add Python to PATH"** antes de dar clic en instalar. Esto es fundamental para que la terminal de comandos del sistema reconozca los binarios de `python` y `pip`.


3. **Verificación:**
Para confirmar que Python se configuró correctamente en tu entorno global, abre una terminal y ejecuta:

```bash
   python --version

```

---

## ⚙️ Instalación y Ejecución

Para garantizar la portabilidad y el correcto funcionamiento del software en cualquier entorno local, se han seguido estándares de desarrollo modular:

* **Compatibilidad:** El sistema es completamente multiplataforma (Windows, macOS y Linux).
* **Gestión de Dependencias:** El proyecto automatiza la instalación de librerías mediante el gestor corporativo `pip` utilizando el manifiesto `requirements.txt`.
* **Recomendación de Entorno (Best Practice):** Se aconseja desplegar el proyecto dentro de un Entorno Virtual (`venv`) para aislar las librerías globales de tu máquina y evitar conflictos de versiones.

### Pasos secuenciales para ejecutar el proyecto:

1. Clona este repositorio en tu computador:

```bash
   git clone [https://github.com/2003EVA/bitacora-automotriz-mvc.git](https://github.com/2003EVA/bitacora-automotriz-mvc.git)

```

2. Entra en la carpeta raíz del proyecto:

```bash
   cd bitacora-automotriz-mvc

```

3. Instala las dependencias necesarias de manera automática:

```bash
   python -m pip install -r requirements.txt

```

4. Ejecuta la aplicación:

```bash
   python main.py

```

---

## 🧪 Pruebas Automatizadas (QA)

* El proyecto utiliza el framework **`pytest`** para asegurar la estabilidad operacional del Modelo matemático y lógico mediante el enfoque **TDD (Test-Driven Development)**.
* La suite incluye validaciones integrales para flujos normales (casos de éxito en instanciación y acumulación financiera) y flujos inválidos (disparo programado de excepciones ante datos corruptos o placas mal formateadas).

### Ejecución de Pruebas en Windows (PowerShell):

Para asegurar el correcto mapeo de módulos de la arquitectura, inyecte la variable de entorno local antes de lanzar el motor de pruebas:

```powershell
$env:PYTHONPATH="."
pytest tests/

```

---

## 📈 Diagrama de Clases (UML Estructural)

Modelado de dominio del sistema renderizado mediante sintaxis Mermaid. Se corrigieron los cierres de encapsulamiento para evitar cortes visuales en la plataforma de GitHub:

```mermaid
classDiagram
    class GestorBitacora {
        -dict vehiculos
        +registrar_vehiculo(Vehiculo) void
        +buscar_vehiculo(str placa) Vehiculo
        +eliminar_vehiculo(str placa) bool
        +guardar_datos() void
        +cargar_datos() void
        +exportar_a_csv(str nombre) void
    }

    class Vehiculo {
        +str placa
        +str marca
        +int kilometraje_actual
        +str tipo
        +list historial_servicios
        +agregar_servicio(Servicio) void
        +obtener_resumen() str
        +to_dict() dict
    }

    class Servicio {
        +str fecha
        +str descripcion
        +float costo
        +int kilometraje_servicio
        +to_dict() dict
        +__str__() str
    }

    GestorBitacora "1" --> "*" Vehiculo : Gestiona
    Vehiculo "1" --* "*" Servicio : Contiene

```

---

## 📸 Capturas de pantalla

### 1. Interfaz Gráfica y Menú Principal
Muestra el diseño visual del sistema en modo oscuro desarrollado con CustomTkinter.
![Menú Principal](docs/capturas/menu_principal.png)

### 2. Funcionalidad y Registro
Evidencia del comportamiento del programa al interactuar y registrar datos en los formularios.
![Registro de Mantenimiento](docs/capturas/funcionalidad_registro.png)

### 3. Persistencia de Datos (Formato JSON)
Confirmación de que los registros se salvan de forma permanente en el archivo local.
![Archivo JSON](docs/capturas/evidencia_datos.png)

### 4. Reporte de Pruebas Unitarias Exitosas (Pytest)
Reporte exitoso de la terminal de QA tras la ejecución del comando de pruebas.
![Pytest Verde](docs/capturas/pruebas_pytest.png)

### 5. Repositorio en GitHub
Estado del control de versiones en la plataforma web con la estructura final de carpetas.
![Repositorio de GitHub](docs/capturas/repositorio_github.png)

---

## 👥 Integrantes

* **Eva Miranda**
* **Andrés Hernández**
* **Andrés Novoa**
* **Luis Cantillo**

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT** - consulte el archivo de licencias del repositorio para más detalles.

```
