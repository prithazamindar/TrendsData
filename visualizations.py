
import matplotlib.pyplot as plt

def plot_predictions((y_test, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Actual Prices', color='blue')
    plt.plot(predicted, label='Predicted Prices', color='orange')
    plt.legend()
    plt.title('Actual vs Predicted Prices')
    plt.show()

