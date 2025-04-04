# 🍽️ ReviewRadar: Classifying Restaurant Sentiment with NLP & Machine Learning

**ReviewRadar** is a sentiment analysis project built to detect whether restaurant reviews are **positive or negative** using Natural Language Processing (NLP) techniques and supervised machine learning. It helps automate feedback analysis for restaurants, food apps, or customer experience teams looking to monitor sentiment at scale.

---

## Real-World Applications
- 🍔 Restaurant feedback monitoring
- 📲 Customer review analytics for apps like UberEats, Yelp
- 🤖 Automated chatbot sentiment interpretation
- 🧾 Brand reputation management

## 🎯 Project Objective

To build a model that reads raw restaurant reviews, processes the text data, and classifies each review as either **positive** (1) or **negative** (0).

---

## 📁 Dataset Overview

**File**: `Restaurant_Reviews.tsv`  
- Contains 1,000 restaurant reviews.
- Each entry includes:
  - 📝 The review text
  - ✅ A sentiment label (0 = negative, 1 = positive)

---

## 🧠 What’s Inside

### 🧹 1. Data Cleaning & Preprocessing
- Removal of punctuation and stopwords
- Lowercasing and stemming using `PorterStemmer`
- Tokenization and reconstruction into clean strings

### 📊 2. Feature Extraction
- **Bag of Words (BoW)** model using `CountVectorizer`
- Transforms text into numerical matrix format for ML

### 🧪 3. Classification Model
- Trains a **Naive Bayes classifier** on the cleaned text features
- Splits data into **Training** and **Test** sets
- Evaluates with a **confusion matrix** for accuracy

---

## 📈 Key Outputs

- ✅ Cleaned text reviews
- 🧠 Trained classification model
- 📊 Confusion matrix showing model performance
- 🔍 Prediction labels for test data

---

## 🛠️ Technologies Used

| Tool/Library         | Purpose                         |
|----------------------|---------------------------------|
| `pandas`, `numpy`    | Data handling                   |
| `nltk`               | Text processing and stemming    |
| `scikit-learn`       | Feature extraction & classification |
| `matplotlib`         | (Optional) Visualization        |

---

## 🚀 How to Run

1. Install required libraries:
```bash
pip install pandas numpy sklearn nltk
