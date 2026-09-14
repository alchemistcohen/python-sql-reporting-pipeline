import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import time
import logging

# Configuración de logs para auditar el proceso automatizado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_etl_pipeline():
    start_time = time.time()
    logging.info("Iniciando Pipeline ETL automatizado...")

    # 1. EXTRACCIÓN
    logging.info("Extrayendo datos de archivos CSV...")
    try:
        df_raw = pd.read_csv("raw_sales_daily.csv")
        df_customers = pd.read_csv("dim_customers.csv")
        df_products = pd.read_csv("dim_products.csv")
    except FileNotFoundError as e:
        logging.error(f"Error al cargar archivos: {e}")
        return

    initial_rows = len(df_raw)
    logging.info(f"Registros crudos extraídos: {initial_rows}")

    # 2. TRANSFORMACIÓN Y LIMPIEZA
    logging.info("Aplicando reglas de limpieza y transformación...")

    # A. Eliminar duplicados exactos
    df_clean = df_raw.drop_duplicates().copy()
    duplicates_removed = initial_rows - len(df_clean)

    # B. Manejo de valores nulos
    df_clean['branch_region'] = df_clean['branch_region'].fillna('Sin Asignar')

    # C. Tipos de datos
    df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'])
    df_clean['quantity'] = df_clean['quantity'].astype(int)
    df_clean['unit_price'] = df_clean['unit_price'].astype(float)

    # D. Métrica calculada
    df_clean['total_revenue'] = np.round(df_clean['quantity'] * df_clean['unit_price'], 2)

    # E. Validación de calidad
    df_clean = df_clean[(df_clean['quantity'] > 0) & (df_clean['unit_price'] > 0)]

    final_rows = len(df_clean)
    logging.info(f"Registros duplicados eliminados: {duplicates_removed}")
    logging.info(f"Registros limpios procesados: {final_rows}")

    # 3. CARGA A SQLITE
    logging.info("Conectando a la base de datos SQLite (company_warehouse.db)...")
    engine = create_engine('sqlite:///company_warehouse.db')

    with engine.begin() as connection:
        df_clean.to_sql('fact_sales', con=connection, if_exists='replace', index=False)
        df_customers.to_sql('dim_customers', con=connection, if_exists='replace', index=False)
        df_products.to_sql('dim_products', con=connection, if_exists='replace', index=False)

    execution_time = round(time.time() - start_time, 2)
    logging.info(f"Pipeline ETL completado con éxito en {execution_time} segundos.")

if __name__ == "__main__":
    run_etl_pipeline()