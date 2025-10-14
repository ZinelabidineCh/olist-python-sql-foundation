# File: 05_visualize_customer_distribution.py
# Role: Create a visualization of the customer distribution by state and save it.

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_customer_distribution():
    """
    Creates and saves a bar chart of the number of customers per state.
    """
    db_name = 'olist.db'
    if not os.path.exists(db_name):
        print(f"Error: Database '{db_name}' not found.")
        return

    engine = create_engine(f'sqlite:///{db_name}')

    # We limit to the top 15 states to make the chart more readable
    query = """
    SELECT
        customer_state,
        COUNT(customer_unique_id) as total_customers
    FROM
        customers
    GROUP BY
        customer_state
    ORDER BY
        total_customers DESC
    LIMIT 15;
    """

    print("--- Generating visualization for customer distribution by state ---")
    
    try:
        df_results = pd.read_sql_query(query, engine)

        # --- Chart Creation ---
        # Set a professional style for the plot
        sns.set_style("whitegrid")
        # Create a figure with a specific size for better readability
        plt.figure(figsize=(12, 8))

        # Create the bar plot using Seaborn
        barplot = sns.barplot(
            x='total_customers',
            y='customer_state',
            data=df_results,
            palette='viridis' # A nice color palette
        )

        # Add titles and labels for clarity
        plt.title('Top 15 States by Number of Customers', fontsize=16, weight='bold')
        plt.xlabel('Number of Customers', fontsize=12)
        plt.ylabel('State', fontsize=12)
        
        # Save the figure to a file in the project's root directory
        output_filename = 'customer_distribution_by_state.png'
        plt.savefig(output_filename, bbox_inches='tight')

        print(f"\n✅ Visualization saved successfully as '{output_filename}'!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    visualize_customer_distribution()