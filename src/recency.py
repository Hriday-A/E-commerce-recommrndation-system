import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"
engine= create_engine(DB_URL)

def run_recency():
    recency_query = """
    select c.customer_unique_id,
    max(o.order_purchase_timestamp) as last_purchase_date,
    ('2018-09-30'::date - max(o.order_purchase_timestamp)::date) as days_since_last_purchase
    from orders o
    join customers c on o.customer_id = c.customer_id
    group by 1 """
    print("Running recency analysis...")
    df=pd.read_sql(recency_query, engine)
    print(("Customer recency analysis:"))
    print(df)

if __name__ == "__main__":
    run_recency()