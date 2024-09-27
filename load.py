from sqlalchemy import create_engine

def load_data(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    
    # Imprimir un resumen de los datos cargados
    print(f"\n\nResumen de datos cargados para {df['city'].iloc[0]}:")
    print(df.to_string(index=False))
