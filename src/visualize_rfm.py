import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

def plot_customer_segments():
    df = pd.read_csv('data/processed/rfm_features.csv')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df,x='recency', y='monetary', alpha =0.5)
    plt.yscale('log')
    plt.title('Customer Segments based on Recency and Monetary Value')
    plt.xlabel('Days since last purchase (Recency)')
    plt.ylabel('Total Spending (log scale)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.2)
    plt.savefig('docs/customer_segments_plot.png')
    plt.show()

if __name__ == "__main__":
    plot_customer_segments()