import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"
engine = create_engine(DB_URL)

def ingest_data():
    data_path = 'data/'
    if not os.path.exists(data_path):
        print(f"ERROR: The directory '{data_path}' does not exist.")
        return

    for file in os.listdir(data_path):
        if file.endswith('.csv'):
            # 1. Clean the filename to create a professional table name
            # This removes .csv, olist_, and _dataset
            clean_name = file.replace('.csv', '').replace('olist_', '').replace('_dataset', '')
            
            # 2. Convert to lowercase (Best practice for SQL)
            table_name = clean_name.lower()
            
            file_path = os.path.join(data_path, file)
            
            print(f"--- Processing {file} ---")
            print(f"Target Table Name: {table_name}") # This confirms the logic worked
            
            df = pd.read_csv(file_path)
            
            # 3. Load into Database
            # 'if_exists=replace' ensures that old, long-named tables are overwritten
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Successfully loaded {table_name}!\n")

if __name__ == "__main__":
    ingest_data()