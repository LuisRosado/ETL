def transform_data(df):
    # Por ejemplo, convertimos la descripción a mayúsculas
    df['description'] = df['description'].str.upper()
    return df
