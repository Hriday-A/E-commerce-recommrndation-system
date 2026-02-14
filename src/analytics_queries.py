import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"
engine= create_engine(DB_URL)

def run_analytics():
    rfm_query = """
    WITH customer_orders AS (
        SELECT 
            c.customer_unique_id,
            COUNT(o.order_id) as total_orders, -- Added 'o.' here
            SUM(p.payment_value) as total_spent, -- Added 'p.' for clarity
            MAX(o.order_purchase_timestamp) as last_purchase
        FROM order_items i
        JOIN orders o ON i.order_id = o.order_id
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN order_payments p ON o.order_id = p.order_id
        GROUP BY 1
    )
    SELECT *,
           RANK() OVER (ORDER BY total_spent DESC) as spend_rank
    FROM customer_orders
    ORDER BY total_spent DESC -- Added an explicit sort for the output
    LIMIT 10;
    """
    print("Running RFM analysis...")
    df=pd.read_sql(rfm_query, engine)
    print(("Top 10 customers by total spending:"))
    print(df)

if __name__ == "__main__":
    run_analytics()