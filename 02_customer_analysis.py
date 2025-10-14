# File: 02_customer_analysis.py
# Role: Connect to the database and perform a first analysis.

import pandas as pd
from sqlalchemy import create_engine
import os

def analyze_customers_by_state():
    """
    Analyzes the number of customers by state and prints the results.
    """
    db_name = 'olist.db'
    
    # Check if the database exists before continuing
    if not os.path.exists(db_name):
        print(f"Error: Database '{db_name}' not found.")
        print("Please run '01_create_database.py' first to create it.")
        return # Stops the function if the DB does not exist

    engine = create_engine(f'sqlite:///{db_name}')

    # SQL query to count customers in each state and sort the result
    query = """
    SELECT
        customer_state,
        COUNT(customer_unique_id) as total_customers
    FROM
        customers
    GROUP BY
        customer_state
    ORDER BY
        total_customers DESC;
    """

    print("--- Running analysis of customers by state ---")
    
    try:
        # Execute the query with Pandas
        df_results = pd.read_sql_query(query, engine)

        print("\n✅ Analysis complete. Here is the number of customers by state:")
        
        # .to_string() ensures the full DataFrame is printed in the terminal
        print(df_results.to_string())

    except Exception as e:
        print(f"An error occurred while running the query: {e}")


if __name__ == '__main__':
    analyze_customers_by_state()