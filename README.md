# 🛒 Olist SLA & Delivery Performance Analysis

## 📌 Overview

This project analyzes delivery performance and SLA (Service Level Agreement) compliance using the Olist E-commerce dataset.
The goal is to identify delays, evaluate logistics efficiency, and uncover patterns affecting customer satisfaction.

---

## 🎯 Business Problem

In e-commerce, delivery delays can significantly impact customer experience.
This project aims to:

* Measure delivery delays
* Evaluate SLA compliance
* Identify high-risk states and product categories

---

## 📂 Dataset

The dataset used is the **Olist E-commerce Dataset**, available on Kaggle.
It contains information about:

* Orders
* Customers
* Products
* Order items
* Delivery timestamps

---

## ❓ Key Questions

* Which states have the highest delivery delays?
* Which product categories are most associated with delays?
* How effectively is SLA being applied?
* What are the patterns behind late deliveries?

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* Jupyter Notebook

---

## ⚙️ Data Processing

* Merged multiple datasets (orders, customers, items, products)
* Handled missing values
* Created new features:

  * `delay` (difference between actual and estimated delivery)
  * `apply_SLA` (whether SLA conditions are met)

---

## 📊 Key Insights

* Certain states show consistently higher delivery delays
* Specific product categories are more prone to late delivery
* SLA is not consistently respected across all orders
* Delay distribution reveals significant outliers

---

## 📈 Visualizations

Some of the analysis results:

![Delay Distribution](images/delay_distribution.png)
![Top Delayed States](images/top_states.png)
![Top Delayed Products](images/top_products.png)

---

## 💡 Recommendations

* Improve logistics in high-delay states
* Re-evaluate suppliers for problematic product categories
* Enhance SLA monitoring and enforcement
* Optimize shipping routes and fulfillment processes

---

## 📎 Project Structure

```
olist-sla-analysis/
│
├── notebooks/
│   └── sla_analysis.ipynb
│
├── images/
│
├── presentation/
│   └── sla_analysis.pptx
│
├── README.md
└── requirements.txt
```

---

## 📽️ Presentation

[View Presentation](#)  <!-- Replace with your link -->

---

## 🚀 Future Work

* Build a predictive model to forecast delivery delays
* Create an interactive dashboard (Power BI / Streamlit)
* Integrate real-time monitoring system

---

## 👤 Author

**Abdelrhman Khalil Abdullah**
