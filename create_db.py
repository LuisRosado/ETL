import sqlite3
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir la base de datos y el modelo
DATABASE_URL = 'sqlite:///weather_data.db'
Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    feels_like = Column(Float, nullable=True)
    humidity = Column(Float, nullable=False)
    description = Column(String, nullable=False)

# Crear la base de datos y la tabla
def create_database():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        feels_like REAL,
        humidity INTEGER,
        pressure INTEGER,
        description TEXT,
        wind_speed REAL,
        timestamp TEXT
    )
    ''')
    conn.commit()
    conn.close()
    print("Base de datos y tabla creadas.")

if __name__ == "__main__":
    create_database()
