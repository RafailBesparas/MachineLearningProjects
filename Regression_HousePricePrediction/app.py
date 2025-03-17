from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained ElasticNet model
model = joblib.load('elasticnet_best_model.pkl')

# Define top 10 features from the analysis
top_10_features = [
    'TotalSF', 'OverallQual', 'GrLivArea', 'GarageCars',
    'GarageArea', 'TotalBsmtSF', 'TotalBath', '1stFlrSF',
    'TotRmsAbvGrd', 'YearBuilt'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = None
    
    if request.method == 'POST':
        try:
            # Get user input from the form
            input_data = [float(request.form[feature]) for feature in top_10_features]
            
            # Convert to array and reshape for model input
            input_array = np.array(input_data).reshape(1, -1)
            
            # Make prediction
            predicted_price = model.predict(input_array)[0]
            predicted_price = f"${predicted_price:,.2f}"  # Format as currency
        except Exception as e:
            predicted_price = f"Error: {str(e)}"
    
    return render_template('index.html', features=top_10_features, predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
