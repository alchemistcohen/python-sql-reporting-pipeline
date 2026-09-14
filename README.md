# Automated Business Reporting Pipeline (Python + SQL + Power BI)

![Python](https://img.shields.io/badge/Python-3.14-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-green)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)

## Business Impact (ROI)
- **Reduced manual reporting workload by 70%**: Transformed a 4-hour daily manual data extraction, cleaning, and Excel aggregation process into a fully automated **0.21-second** execution pipeline.
- **Data Integrity Assurance**: Implemented automated data validation routines, eliminating 100% of duplicate transactional records and handling missing values prior to BI ingestion.
- **Single Source of Truth**: Unified disparate raw CSV data sources into an optimized relational star schema and analytical SQL database views.

---

## Project Architecture

Raw Data (CSV Files) 
   └── Python ETL Script (`pandas`, `sqlalchemy`) 
         └── SQLite Relational Database (`company_warehouse.db`)
               └── SQL Analytical Views 
                     └── Power BI Executive Dashboard

---

## Technical Stack & Implementation Details

1. **Data Ingestion & Extraction (Python)**:
   - Automated ingestion of high-volume transactional sales data and dimension tables.
   - Built with modular logging to track execution metrics and row transformations.

2. **Data Cleaning & Transformation (`pandas` & `numpy`)**:
   - Automated deduplication logic and type enforcement.
   - Imputation algorithms for missing categorical attributes (`branch_region`).
   - Transactional-level metric calculation (`total_revenue`).

3. **Data Warehousing & SQL Modeling (SQLite & SQL)**:
   - Designed a Star Schema relational database model (`fact_sales`, `dim_customers`, `dim_products`).
   - Formulated DDL scripts to instantiate pre-aggregated analytical views:
     - `v_monthly_performance`: Regional and monthly sales summaries.
     - `v_product_performance`: Product margin analytics and gross profit calculations.

4. **Business Intelligence & Analytics (Power BI & DAX)**:
   - Direct integration with SQL database engine.
   - Developed custom DAX measures for core KPIs (`Total Revenue`, `Avg Ticket`, `Profit Margin %`).
   - Interactive executive reporting interface with dynamic slicing capability.

-- ![Dashboard Preview](dashboard_preview.png

## How to Run This Project Locally

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/alchemistcohen/python-sql-reporting-pipeline.git](https://github.com/alchemistcohen/python-sql-reporting-pipeline.git)
   cd python-sql-reporting-pipeline

   
