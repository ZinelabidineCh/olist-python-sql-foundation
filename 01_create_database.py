# File: 01_create_database.py
# Role: Read all CSV files and create the SQLite database.

import pandas as pd
import os
from sqlalchemy import create_engine
import time

def create_database():
    """
    Main function to create the database from the CSV files.
    """
    print("--- Starting database creation ---")
    
    # Correct paths for a script run from the project root
    path_to_data = 'data' 
    db_name = 'olist.db'

    # Delete the old database if it exists
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"Old database '{db_name}' deleted.")

    engine = create_engine(f'sqlite:///{db_name}')
    
    csv_files = [f for f in os.listdir(path_to_data) if f.endswith('.csv')]
    
    print(f"\nFound {len(csv_files)} CSV files to process...")
    
    # Loop through each file to load it into the DB
    for csv_file in csv_files:
        start_time = time.time()
        file_path = os.path.join(path_to_data, csv_file)
        df = pd.read_csv(file_path)
        table_name = csv_file.replace('olist_','').replace('_dataset.csv', '')
        
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
        end_time = time.time()
        print(f"  -> Table '{table_name}' created with {len(df)} rows in {end_time - start_time:.2f} seconds.")

    print(f"\n✅ Database '{db_name}' created successfully!")

# This standard Python line ensures the create_database() function is called 
# when the script is executed.
if __name__ == '__main__':
    create_database()