import sqlite3

def create_analytics_views():
    conn = sqlite3.connect('company_warehouse.db')
    cursor = conn.cursor()

    # Vista 1: Resumen Ejecutivo Mensual por Región (Join + Aggregations)
    view_monthly_performance = """
    CREATE VIEW IF NOT EXISTS v_monthly_performance AS
    SELECT 
        strftime('%Y-%m', f.transaction_date) AS year_month,
        f.branch_region,
        COUNT(DISTINCT f.transaction_id) AS total_transactions,
        SUM(f.quantity) AS total_units_sold,
        ROUND(SUM(f.total_revenue), 2) AS total_revenue,
        ROUND(AVG(f.total_revenue), 2) AS avg_ticket_size
    FROM fact_sales f
    GROUP BY year_month, f.branch_region;
    """

    # Vista 2: Rendimiento de Producto y Margen (Join Hechos + Dimensión)
    view_product_margins = """
    CREATE VIEW IF NOT EXISTS v_product_performance AS
    SELECT 
        p.product_id,
        p.product_name,
        p.category,
        SUM(f.quantity) AS units_sold,
        ROUND(SUM(f.total_revenue), 2) AS gross_revenue,
        ROUND(SUM(f.quantity * p.cost_price), 2) AS total_cost,
        ROUND(SUM(f.total_revenue) - SUM(f.quantity * p.cost_price), 2) AS gross_profit
    FROM fact_sales f
    INNER JOIN dim_products p ON f.product_id = p.product_id
    GROUP BY p.product_id, p.product_name, p.category;
    """

    print("Creando vistas analíticas en SQL...")
    cursor.execute("DROP VIEW IF EXISTS v_monthly_performance;")
    cursor.execute(view_monthly_performance)
    
    cursor.execute("DROP VIEW IF EXISTS v_product_performance;")
    cursor.execute(view_product_margins)

    conn.commit()
    conn.close()
    print("¡Vistas 'v_monthly_performance' y 'v_product_performance' creadas exitosamente!")

if __name__ == "__main__":
    create_analytics_views()