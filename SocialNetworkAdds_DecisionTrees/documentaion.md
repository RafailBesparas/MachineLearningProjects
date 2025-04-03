# 🌳 Decision Tree Classification – Social Network Ads Prediction

This project demonstrates how to use a **Decision Tree Classifier** to predict whether a user will purchase a product based on social network ad data. Using age and estimated salary as input features, the model learns to classify user behavior into purchasing or not purchasing.

---

💡 Insights
Younger users with high salaries are more likely to purchase.

Decision boundaries show sharp splits due to tree-based logic.


## 🎯 Project Objective

- Predict if a user will buy a product after seeing a social media advertisement.
- Visualize the decision boundaries created by the decision tree.
- Explore model behavior and feature influence through decision boundaries.

---

## 📁 Dataset Overview

**File**: `Social_Network_Ads.csv`

| Feature         | Description                       |
|-----------------|-----------------------------------|
| `User ID`       | Unique identifier for each user   |
| `Gender`        | Male or Female                    |
| `Age`           | Age of the user                   |
| `EstimatedSalary` | User's salary in dollars        |
| `Purchased`     | Target variable (0 = No, 1 = Yes) |

---

## 🧠 Model Used

- **Decision Tree Classifier**
  - Non-linear, rule-based classifier
  - Learns decision boundaries by recursively splitting data
  - Easy to visualize and interpret

---

## 🧰 Tech Stack

| Tool/Library     | Purpose                         |
|------------------|---------------------------------|
| Python           | Main programming language       |
| pandas           | Data handling and preprocessing |
| matplotlib, seaborn | Data visualization          |
| scikit-learn     | Model training and evaluation   |

---

## 🚀 Project Steps

1. **Data Preprocessing**
   - Importing and cleaning the dataset
   - Splitting into training and test sets
   - Feature scaling using `StandardScaler`

2. **Model Training**
   - Fitting a `DecisionTreeClassifier` from `sklearn`

3. **Prediction & Evaluation**
   - Predict test results and evaluate using confusion matrix
   - Analyze accuracy and performance

4. **Visualization**
   - Plotting decision regions for both training and test data
   - Understand how the model splits the space

---

## 📊 Sample Output

- **Confusion Matrix**
- **Training/Test Set Decision Boundaries**
- **Model Accuracy Score**

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/decision-tree-social-ads.git
   cd decision-tree-social-ads
