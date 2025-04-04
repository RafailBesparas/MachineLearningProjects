# 🍷 Principal Component Analysis on Wine Dataset

This project applies **Principal Component Analysis (PCA)** to a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The goal is to reduce dimensionality, visualize clusters, and uncover the most important features explaining variance in the dataset.

---

### 📌 Use Cases
- 📊 Preprocessing step before classification
- 🍇 Understanding wine clustering and chemical composition
- 🧠 Teaching dimensionality reduction concepts

## 🎯 Project Objective

- Apply **PCA** for dimensionality reduction.
- Visualize the dataset in a reduced 2D or 3D feature space.
- Identify wine categories through clustering and feature correlation.
- Enhance model interpretability and reduce overfitting in future ML models.

---

## 📁 Dataset Overview

**File**: `Wine.csv`

- Features: 13 numerical attributes (alcohol, malic acid, ash, etc.)
- Target: Cultivar class (three categories)

| Column              | Description                     |
|---------------------|---------------------------------|
| Alcohol             | Ethanol content                 |
| Malic_Acid          | Acid concentration              |
| Ash                 | Mineral content                 |
| ...                 | ...                             |
| Target              | Wine class (1, 2, or 3)         |

---

## 🧠 Techniques Used

- 📉 **Standardization** – Normalize features using `StandardScaler`.
- 📊 **PCA** – Reduce to 2 components for visualization.
- 🧪 **Explained Variance Ratio** – Analyze how much information is retained.
- 📈 **2D Plotting** – Scatter plot of the first 2 principal components.

---

## 🛠️ Libraries Used

- `pandas`, `numpy` – Data manipulation
- `matplotlib`, `seaborn` – Data visualization
- `sklearn.decomposition.PCA` – Principal Component Analysis
- `sklearn.preprocessing.StandardScaler` – Feature scaling

---

## 🔍 Key Outputs

- ✅ Scree plot to show explained variance by each component
- ✅ 2D PCA plot showing clustering by wine type
- ✅ Reduced feature matrix (`PC1`, `PC2`)

---

## 🚀 How to Run

1. Install necessary libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
