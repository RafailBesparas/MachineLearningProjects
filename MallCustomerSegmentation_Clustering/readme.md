# 🛍️ Customer Segmentation with K-Means & Hierarchical Clustering

This project focuses on **unsupervised learning** techniques to group customers into segments based on their shopping habits. By applying both **K-Means Clustering** and **Hierarchical Clustering**, we aim to uncover hidden patterns and group similar customers together — a key step in marketing personalization and customer retention strategies.

---

## 🎯 Project Objective

- Analyze customer behavior using their **Annual Income** and **Spending Score**.
- Identify meaningful customer segments using clustering algorithms.
- Visualize these clusters to support business decision-making in targeting.

---

## 📁 Dataset: `Mall_Customers.csv`

| Feature        | Description                            |
|----------------|----------------------------------------|
| `CustomerID`   | Unique ID assigned to each customer    |
| `Gender`       | Male or Female                         |
| `Age`          | Age of the customer                    |
| `Annual Income (k$)` | Customer's income in thousands   |
| `Spending Score`     | Score assigned based on spending habits (1–100) |

---

## 🧠 Algorithms Implemented

### 📌 1. K-Means Clustering – `KMeansClustering.ipynb`
- Elbow method to determine the optimal number of clusters.
- Groups customers based on similarity in features.
- Visualizes clusters in 2D space with clear color-coded segmentation.

### 📌 2. Hierarchical Clustering – `HierarchicalClustering.ipynb`
- Dendrogram used to find optimal number of clusters.
- Agglomerative clustering to merge clusters based on linkage distance.
- Produces visual plots to explore cluster hierarchies.

---

## 🧰 Tech Stack

| Tool/Library | Purpose                         |
|--------------|---------------------------------|
| Python       | Core programming language       |
| pandas       | Data handling and preparation   |
| matplotlib & seaborn | Data visualization     |
| scikit-learn | Clustering algorithms           |
| scipy        | Dendrogram and linkage          |

---

## 🔍 Key Insights

- Customers with high income don't always have high spending scores.
- 5–6 distinct customer personas can be identified using these features.
- Marketing strategies can be tailored per cluster (e.g., discounts for high spenders, engagement for low spenders).

---

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/MachineLearningProjects.git
cd MachineLearningProjects

# Install dependencies
pip install pandas matplotlib seaborn scikit-learn scipy

# Run the notebooks
jupyter notebook KMeansClustering.ipynb
jupyter notebook HierarchicalClustering.ipynb
