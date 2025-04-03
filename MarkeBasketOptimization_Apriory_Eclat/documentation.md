# 🛒 Market Basket Optimization with Apriori & Eclat

This project applies **Association Rule Learning** techniques—specifically the **Apriori** and **Eclat** algorithms—to discover purchasing patterns from transaction data. By analyzing which products are frequently bought together, this model provides insights for cross-selling, store layout optimization, and targeted marketing strategies.

---

## 📈 Business Applications
🛍 Optimize store layout by placing associated items nearby.

📬 Run targeted promotions for items often bought together.

💡 Recommend items during checkout or in online carts.


## 📊 Project Overview

- **Dataset**: `Market_Basket_Optimisation.csv`  
  Contains anonymized retail transaction data with items bought per transaction.

- **Goal**: Identify strong association rules between products to enhance sales and customer satisfaction.

---

## 🧠 Algorithms Used

### 1️⃣ Apriori Algorithm (`AprioriAssociationLearning.ipynb`)
- Uses a breadth-first search strategy to find frequent itemsets.
- Generates association rules with metrics:
  - **Support**: How frequently the itemset appears in the dataset.
  - **Confidence**: How often rule `A → B` holds true.
  - **Lift**: Strength of the association relative to random chance.

### 2️⃣ Eclat Algorithm (`EclatModel.ipynb`)
- Uses a depth-first search strategy with a vertical data format.
- Focuses on identifying frequent itemsets more efficiently by comparing transaction lists.

---

## 🧰 Tech Stack

| Tool/Library | Purpose                        |
|--------------|--------------------------------|
| Python       | Core programming language      |
| Pandas       | Data wrangling and preparation |
| `apyori`     | Apriori algorithm implementation |
| Custom Logic | Eclat algorithm via set operations |
| Matplotlib / Seaborn | (Optional) Visualization |

---

## 🔍 Example Insights
Customers who buy milk are likely to buy bread.

Eggs and butter frequently occur together.

High lift scores reveal actionable cross-selling opportunities.


