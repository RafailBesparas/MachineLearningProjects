#### Note: This project is under refinement and I need more time to clean the code and create something modular. Also not all the steps involved are finished. Moreover the algorithm accuracy is low.

I will use also a pre-trained model if the neural network keep the low performance

# Project Title: Loan Approval Risk Prediction Using Neural Networks

The goal of this project is to build a binary classification model that predicts whether a loan application will be approved or rejected based on various applicant and financial features. The target variable is LoanApproved, with values 0 (rejected) or 1 (approved).

# Description: 
This project uses a neural network-based model built with Keras and TensorFlow to predict the risk of loan approval. By leveraging historical loan application data, the model is trained to classify whether a loan will be approved or not. The dataset includes features such as the applicant’s credit score, income, loan amount, employment history, and debt-to-income ratio.

# Steps Involved:

1. Data Preprocessing: Clean the data, handle missing values, encode categorical variables, and scale numerical features.
2. Feature Selection: Choose relevant features based on domain knowledge or feature importance.
3. Model Development: Create a neural network model with multiple layers (Dense layers), activation functions (ReLU, Sigmoid), and dropout layers to avoid overfitting.
4. Model Compilation: Compile the model with appropriate loss function (binary_crossentropy), optimizer (adam and not only), and evaluation metric (accuracy).
5. Model Training: Train the model on the training data, validate it on the validation set, and evaluate the performance.
6. Hyperparameter Tuning: Tune hyperparameters (such as learning rate, batch size, number of epochs, and hidden layers) using techniques like GridSearchCV or RandomizedSearchCV for improved model performance.
8. Model Evaluation: Evaluate the model using test data and performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
   
# Outcome:
A trained neural network model capable of predicting whether a loan will be approved based on input features, with an optimized set of hyperparameters for better generalization to unseen data.
