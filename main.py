import os
import sqlite3
import schedule
import time
from dotenv import load_dotenv
from extract import extract_data
from transform import transform_data
from load import load_data
from create_db import create_database

def database_exists(db_path):
    return os.path.exists(db_path)

def table_exists(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    exists = cursor.fetchone()[0] == 1
    conn.close()
    return exists

def setup_database(db_path, table_name):
    if not database_exists(db_path):
        print("La base de datos no existe. Creándola...")
        create_database()
    elif not table_exists(db_path, table_name):
        print("La tabla no existe. Creándola...")
        create_database()
    else:
        print("La base de datos y la tabla ya existen. Usando la existente.")

def job(api_key, cities, db_url, table_name):
    for city in cities:
        # Extract
        raw_data = extract_data(api_key, city)

        if not raw_data.empty:
            # Transform
            transformed_data = transform_data(raw_data)

            # Load
            load_data(transformed_data, db_url, table_name)
            print(f"Datos de {city} cargados exitosamente.")
        else:
            print(f"No se obtuvieron datos para {city}.")

def main():
    load_dotenv()  # Cargar variables de entorno
    api_key = 'YOUR KEY'
    cities = ['Guadalajara', 'Ciudad de México', 'Monterrey']
    db_path = 'weather_data.db'
    db_url = f'sqlite:///{db_path}'
    table_name = 'weather'

    setup_database(db_path, table_name)

    # Ejecutar el trabajo inmediatamente
    job(api_key, cities, db_url, table_name)

    # Programar la ejecución cada 3 horas
    schedule.every(3).hours.do(job, api_key, cities, db_url, table_name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
