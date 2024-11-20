
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(crypto_data, trends_data):
    # Merge datasets on date
    combined_data = pd.merge(crypto_data, trends_data, left_on='date', right_on='date', how='inner')

    # Plot trends vs price
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='price', data=combined_data, label='Crypto Price')
    sns.lineplot(x='date', y='Bitcoin', data=combined_data, label='Bitcoin Search Volume')
    plt.legend()
    plt.title('Price vs Search Volume')
    plt.show()

    # Correlation matrix
    correlation = combined_data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    return combined_data

# Example usage
# combined_data = perform_eda(crypto_data, google_trends)
