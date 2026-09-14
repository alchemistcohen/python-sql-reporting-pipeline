import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Semilla para que los datos sintéticos sean reproducibles
np.random.seed(42)
n_rows = 1200

  # Generar ventas diarias sin procesar (Raw Sales)


start_date = datetime(2026, 1, 1)
dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 90, n_rows)]
products = [f"PROD-{x:03d}" for x in np.random.randint(1, 25, n_rows)]
customers = [f"CUST-{x:04d}" for x in np.random.randint(1, 150, n_rows)]
quantities = np.random.randint(1, 12, n_rows)
unit_prices = np.round(np.random.uniform(15.0, 450.0, n_rows), 2)
branches = np.random.choice(["Norte", "Sur", "Este", "Oeste", None], n_rows, p=[0.27, 0.25, 0.25, 0.18, 0.05])

df_raw = pd.DataFrame({
    "transaction_id": [f"TX-{i:06d}" for i in range(1, n_rows + 1)],
    "transaction_date": dates,
    "customer_id": customers,
    "product_id": products,
    "quantity": quantities,
    "unit_price": unit_prices,
    "branch_region": branches
})

# Inserción deliberada de duplicados para simular error de origen
df_duplicates = df_raw.head(45).copy()
df_raw = pd.concat([df_raw, df_duplicates], ignore_index=True)
df_raw.to_csv("raw_sales_daily.csv", index=False)


# Generar dimensión de productos (dim_products)

products_data = pd.DataFrame({
    "product_id": [f"PROD-{i:03d}" for i in range(1, 25)],
    "product_name": [f"Producto_{i}" for i in range(1, 25)],
    "category": np.random.choice(["Electrónica", "Hogar", "Oficina", "Tecnología"], 24),
    "cost_price": np.round(np.random.uniform(5.0, 200.0, 24), 2)
})
products_data.to_csv("dim_products.csv", index=False)


#  Generar dimensión de clientes (dim_customers)

customers_data = pd.DataFrame({
    "customer_id": [f"CUST-{i:04d}" for i in range(1, 150)],
    "customer_segment": np.random.choice(["B2B", "B2C", "Corporativo"], 149),
    "registration_date": [datetime(2025, 1, 1) + timedelta(days=int(x)) for x in np.random.randint(0, 365, 149)]
})
customers_data.to_csv("dim_customers.csv", index=False)

print("¡Archivos generados con éxito!")
print("1. raw_sales_daily.csv")
print("2. dim_products.csv")
print("3. dim_customers.csv")