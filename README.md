# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción

Este reto técnico consiste en el procesamiento automatizado de transacciones bancarias a través de una herramienta de línea de comandos (CLI). A partir de un archivo `.csv` con datos de transacciones, la aplicación analiza y valida la información para generar un reporte financiero con los siguientes resultados clave:

1. **Balance final** de todas las transacciones válidas.
2. **ID y monto** de la transacción con el mayor valor.
3. **Conteo total** de transacciones de tipo *Crédito* y *Débito*.

Además, la herramienta permite identificar e imprimir las transacciones inválidas según un sistema de validación robusto. El reporte se puede almacenar en un archivo `.txt` ubicado en la carpeta \`output\`, lo que facilita la auditoría y el control de calidad de los datos procesados.

---

## Instrucciones de Ejecución  

### Requisitos Previos  

- Python 3.10.0  
- pip (gestor de paquetes)  

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/marjo1994/interbank-academy-25.git
   cd interbank-academy-25

3. Instalación en modo desarrollo:
   ```bash
   pip install -e .

4. Ejecutar el comando para generar el reporte (solo archivos `.csv` en la carpeta `input`):
   ```bash
   interbank-transacciones data.csv

5. Generar el reporte y mostrar errores de validación:
   ```bash
   interbank-transacciones data.csv --mostrar-errores

5. Generar reporte, mostrar errores y guardar el resultado en un archivo `.txt`:
   ```bash
   interbank-transacciones data.csv --mostrar-errores -o finalreport

**El archivo de salida se guarda automáticamente en la carpeta `output/`.**

---

## Enfoque y Solución

Para resolver el reto se utilizaron tres librerías principales: **Pandas**, **Pydantic** y **Pytest**.

Con **Pydantic** se definieron modelos que validan cada transacción (`id`, `tipo`, `monto`) y estructuran el reporte final (`balance_final`, transacción de mayor valor y conteo de créditos/débitos). Esto garantiza la integridad de los datos y evita errores durante el procesamiento. Los modelos están definidos en `models.py`, y las validaciones adicionales se implementaron en `validation.py`.

El análisis de datos y la generación del reporte se desarrollaron en `reporting.py`, utilizando funciones de **Pandas** para calcular de forma eficiente los indicadores solicitados.

En `main.py` se integran tanto las validaciones como la lógica de generación del reporte, permitiendo obtener el resultado completo y registrar posibles errores en los datos de entrada.

El archivo `cli.py` define la interfaz por línea de comandos (CLI), permitiendo al usuario:
- Cargar un archivo `.csv` con las transacciones.
- Visualizar errores de validación mediante la opción `--mostrar-errores`.
- Generar un archivo de salida personalizado con la opción `-o`.

Por último, la carpeta `tests` contiene las pruebas unitarias implementadas con **Pytest**, asegurando que los modelos, funciones de validación y lógica de reporte funcionen correctamente y arrojen los resultados esperados.

---
## Estructura del proyecto

```
└── 📁output # Reportes generados (.txt)
└── 📁input  # Archivos de entrada (.csv)
    └── data.csv
└── 📁src # Código fuente principal
    └── 📁services
        └── reporting.py # Lógica del reporte (balance, máximas transacciones, conteo)
        └── validation.py # Validaciones utilizando modelos Pydantic 
    └── 📁tests # Pruebas unitarias con Pytest
        └── test_models.py
        └── test_reporting.py
        └── test_validation.py
    └── __init__.py
    └── cli.py # Comandos y argumentos de la interfaz CLI
    └── config.py # Configuración de rutas de entrada/salida
    └── main.py # Orquestación del flujo: validación + reporte
    └── models.py Modelos de datos y validaciones con Pydantic
└── .gitignore
└── README.md  # Documentación del proyecto
└── requirements.txt # Dependencias del entorno
└── setup.py # Instalación del paquete en modo desarrollo
```

