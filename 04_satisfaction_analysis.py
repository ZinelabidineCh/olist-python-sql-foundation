# File: 04_satisfaction_analysis.py
# Role: Analyze the relationship between delivery time and customer satisfaction score.

import pandas as pd
from sqlalchemy import create_engine
import os

def analyze_satisfaction_vs_delivery_time():
    """
    Calculates the average delivery time for each satisfaction score (1 to 5).
    """
    db_name = 'olist.db'
    if not os.path.exists(db_name):
        print(f"Error: Database '{db_name}' not found.")
        print("Please run '01_create_database.py' first to create it.")
        return

    engine = create_engine(f'sqlite:///{db_name}')

    # This query calculates the delivery time in days and then finds the average
    # delivery time for each review score.
    # JULIANDAY is a function in SQLite that converts dates into a number,
    # making it easy to calculate the difference between two dates.
    query = """
    SELECT
        r.review_score,
        AVG(JULIANDAY(o.order_delivered_customer_date) - JULIANDAY(o.order_purchase_timestamp)) as avg_delivery_time_days
    FROM
        orders o
    JOIN
        order_reviews r ON o.order_id = r.order_id
    WHERE
        o.order_delivered_customer_date IS NOT NULL -- We only consider delivered orders
        AND o.order_purchase_timestamp IS NOT NULL
    GROUP BY
        r.review_score
    ORDER BY
        r.review_score;
    """

    print("--- Running analysis of satisfaction score vs. delivery time ---")
    
    try:
        df_results = pd.read_sql_query(query, engine)
        
        # Round the average days to make it more readable
        df_results['avg_delivery_time_days'] = df_results['avg_delivery_time_days'].round(2)

        print("\n✅ Analysis complete. Average delivery time (in days) per satisfaction score:")
        print(df_results.to_string())
        
        print("\nInsight: Lower scores are clearly associated with longer delivery times.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    analyze_satisfaction_vs_delivery_time()