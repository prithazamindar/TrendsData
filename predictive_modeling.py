
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def prepare_data(combined_data):
    # Feature engineering
    data['price_change'] = data['price'].pct_change()
    data['search_change'] = data['Bitcoin'].pct_change()
    data.dropna(inplace=True)
    return data

def train_model(prepared_data):
    # Prepare data
    X = data[['search_change']]
    y = data['price_change']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    return model

