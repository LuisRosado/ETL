# Sistema de Recolección de Datos Meteorológicos

Este proyecto es un sistema automatizado para recolectar, transformar y almacenar datos meteorológicos de varias ciudades utilizando la API de OpenWeatherMap.

## Características

- Extrae datos meteorológicos de múltiples ciudades usando la API de OpenWeatherMap.
- Transforma los datos extraídos para su almacenamiento.
- Almacena los datos en una base de datos SQLite.
- Ejecuta automáticamente la recolección de datos cada 3 horas.

## Requisitos

- Python 3.x
- Bibliotecas de Python:
  - requests
  - pandas
  - sqlalchemy
  - schedule
  - python-dotenv

## Instalación

1. Clona este repositorio:
   ```
   git clone [URL_DEL_REPOSITORIO]
   cd [NOMBRE_DEL_DIRECTORIO]
   ```

2. Instala las dependencias necesarias:
   ```
   pip install requests pandas sqlalchemy schedule python-dotenv
   ```

3. Crea un archivo `.env` en el directorio raíz y añade tu clave API de OpenWeatherMap:
   ```
   API_KEY=tu_clave_api_aquí
   ```

## Estructura del Proyecto

- `main.py`: Script principal que orquesta el proceso ETL y la programación de tareas.
- `extract.py`: Contiene la lógica para extraer datos de la API de OpenWeatherMap.
- `transform.py`: Maneja la transformación de los datos extraídos.
- `load.py`: Gestiona la carga de datos transformados en la base de datos SQLite.
- `create_db.py`: Script para crear la base de datos y la tabla necesaria.

## Uso

1. Primero, asegúrate de que la base de datos esté creada:
   ```
   python create_db.py
   ```

2. Luego, ejecuta el script principal:
   ```
   python main.py
   ```

El script realizará las siguientes acciones:
1. Verificará si la base de datos y la tabla existen, creándolas si es necesario.
2. Ejecutará inmediatamente la recolección de datos para las ciudades especificadas (Guadalajara, Ciudad de México, Monterrey).
3. Programará la recolección automática de datos cada 3 horas.

## Personalización

- Para añadir o modificar las ciudades, edita la lista `cities` en la función `main()` en `main.py`.
- Para cambiar la frecuencia de recolección de datos, modifica la línea `schedule.every(3).hours.do(job, ...)` en `main()`.
- Para ajustar la transformación de datos, edita la función `transform_data()` en `transform.py`.

## Descripción de los Módulos

### extract.py
Contiene la función `extract_data()` que hace una solicitud a la API de OpenWeatherMap y devuelve los datos en un DataFrame de pandas.

### transform.py
Contiene la función `transform_data()` que realiza transformaciones simples en los datos, como convertir la descripción a mayúsculas.

### load.py
Contiene la función `load_data()` que carga los datos transformados en la base de datos SQLite y muestra un resumen de los datos cargados.

### create_db.py
Define la estructura de la base de datos y contiene la función `create_database()` para crear la base de datos y la tabla necesaria.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

[Incluir información de licencia aquí]
