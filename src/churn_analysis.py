import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"
engine= create_engine(DB_URL)

def export_rfm_features():
    # This query uses the CTE logic we discussed to ensure data integrity
    rfm_query = """
    WITH order_totals AS (
        SELECT order_id, SUM(payment_value) as order_value
        FROM order_payments
        GROUP BY 1
    )
    SELECT 
        c.customer_unique_id,
        ('2018-09-03'::date - MAX(o.order_purchase_timestamp)::date) as recency,
        COUNT(DISTINCT o.order_id) as frequency,
        SUM(ot.order_value) as monetary
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_totals ot ON o.order_id = ot.order_id
    GROUP BY 1;
    """
    
    print("Generating RFM Feature Table...")
    df = pd.read_sql(rfm_query, engine)
    
    # Create the data directory if it doesn't exist (safety first!)
    os.makedirs('data/processed', exist_ok=True)
    
    # Save the file
    output_path = 'data/processed/rfm_features.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Success! Feature table saved to {output_path}")
    print(f"Total customers processed: {len(df)}")

if __name__ == "__main__":
    export_rfm_features()