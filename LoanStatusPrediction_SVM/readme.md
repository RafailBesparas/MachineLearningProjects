# 🏦 Loan Status Prediction using Support Vector Machine (SVM)

This project applies a **Support Vector Machine (SVM)** classification algorithm to predict whether a loan application should be approved or rejected based on applicant details. It's a practical example of applying machine learning in the **FinTech** and **credit risk assessment** domain.

---

## 📈 Sample Output
✅ Confusion matrix with TP/TN/FP/FN values

📊 Accuracy: Model correctly predicts loan status with a high success rate

🔍 Visual insights into which features impact approval

## 💡 Key Insights
Credit History and Applicant Income are major predictors of loan approval.

Preprocessing plays a critical role in boosting model performance.

## 📊 Project Overview

- **Goal**: Predict the loan status (approved or not) based on applicant features such as income, credit history, and loan amount.
- **Dataset**: `LoanStatusProject.csv` – real-world-inspired loan application dataset with multiple financial and demographic indicators.

---

## 📁 Dataset Features

| Column              | Description                                |
|---------------------|--------------------------------------------|
| `Gender`            | Male or Female                             |
| `Married`           | Applicant marital status                   |
| `Dependents`        | Number of dependents                       |
| `Education`         | Graduate or Not Graduate                   |
| `Self_Employed`     | Employment status                          |
| `ApplicantIncome`   | Income of the applicant                    |
| `CoapplicantIncome` | Income of co-applicant                     |
| `LoanAmount`        | Requested loan amount                      |
| `Loan_Amount_Term`  | Term of loan in months                     |
| `Credit_History`    | Credit history (1 = good, 0 = bad)         |
| `Property_Area`     | Urban/Rural/Semiurban                      |
| `Loan_Status`       | Target variable (Y = Approved, N = Rejected) |

---

## 🧠 Machine Learning Model

- **Algorithm**: Support Vector Machine (SVM)
  - Supervised learning algorithm for classification
  - Good for high-dimensional datasets
  - Uses different kernels (e.g., linear, RBF) for flexibility

---

## 🔧 Technologies Used

| Tool/Library | Role                                    |
|--------------|------------------------------------------|
| Python       | Main programming language                |
| pandas       | Data preprocessing and manipulation      |
| scikit-learn | Model training, preprocessing, evaluation |
| matplotlib   | Visualization of model performance       |

---

## 🚀 Workflow

1. **Data Cleaning**
   - Handle missing values
   - Encode categorical variables
   - Normalize numerical data

2. **Model Training**
   - Train-test split
   - Apply SVM classifier using `sklearn.svm.SVC`
   - Try different kernels (e.g., linear, RBF)

3. **Model Evaluation**
   - Confusion matrix
   - Accuracy score
   - Precision & recall (optional)

---

## 🧪 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/MachineLearningProjects.git
cd MachineLearningProjects

# Install dependencies
pip install pandas matplotlib scikit-learn

# Run the notebook
jupyter notebook LoanStatusPredictionSupportVectorMachine.ipynb
