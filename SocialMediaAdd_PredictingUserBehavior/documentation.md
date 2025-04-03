# 📌 Kernel SVM Classification – Predicting User Behavior on Social Media Ads

This project applies a **Kernel Support Vector Machine (SVM)** to classify whether a user will purchase a product based on their age and estimated salary, using data from social network advertisements.

---

## 💡 Insights
The Kernel SVM performs significantly better than linear models for non-linear distributions.

High-income + older age users are more likely to purchase based on the decision boundaries.



## 📊 Project Overview

- **Goal**: Predict user purchase behavior using non-linear classification with a Kernel SVM.
- **Dataset**: `Social_Network_Ads.csv` – includes user age, salary, and purchase outcome.

---

## 📁 Dataset Description

| Feature         | Description                        |
|-----------------|------------------------------------|
| `User ID`       | Unique ID for each user            |
| `Gender`        | Gender (not used in model)         |
| `Age`           | Age of the user                    |
| `EstimatedSalary` | Income level in USD              |
| `Purchased`     | Target variable (1 = purchased)    |

---

## 🧠 Algorithm: Kernel Support Vector Machine (SVM)

- Transforms the original input space into a higher-dimensional space using a **Radial Basis Function (RBF) kernel**, allowing the model to learn non-linear decision boundaries.
- Maximizes the margin between classes while minimizing misclassification.

---

## 🛠️ Tools & Libraries

| Tool         | Purpose                           |
|--------------|-----------------------------------|
| Python       | Core programming language         |
| pandas       | Data processing and analysis      |
| matplotlib & seaborn | Data visualization       |
| scikit-learn | Model training, scaling, metrics  |

---

## 🚀 Workflow

1. **Data Preprocessing**
   - Load CSV file, extract relevant columns
   - Feature scaling using `StandardScaler`
   - Train-test split

2. **Model Training**
   - Apply `SVC(kernel='rbf')` from `sklearn.svm`
   - Fit the model to the training set

3. **Evaluation**
   - Predict on the test set
   - Evaluate performance using a **confusion matrix**
   - Plot decision boundaries to visualize classification regions

---

## 📈 Visual Output

- 🌈 Clear decision boundary plots
- ✅ Confusion matrix for test set evaluation
- 📊 Accuracy measurement and model diagnostics

---

## 🧪 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/MachineLearningProjects.git
cd MachineLearningProjects

# Install dependencies
pip install pandas matplotlib seaborn scikit-learn

# Launch Jupyter Notebook
jupyter notebook KernelSMVClassification.ipynb
