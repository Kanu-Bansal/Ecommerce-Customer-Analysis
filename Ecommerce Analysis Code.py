"""
“I worked on an e-commerce dataset where I performed data cleaning, feature engineering,
and exploratory data analysis. I calculated key metrics like total revenue, average order
value, and customer retention. I also identified high-value customers and provided insights
to improve business performance.”
"""



import pandas as pd
import matplotlib.pyplot as plt
# import datetime

# Load Dataset
df = pd.read_csv("ecommerce_dataset.csv")
print(df.info())
print(df.isnull().sum())
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df.drop_duplicates())

# Feature Engineering
df["Total_Amount"] = df["Quantity"] * df["Price"]
print(df)

# Total Revenue
total_revenue = df["Total_Amount"].sum()
print("Total Revenue:",total_revenue)

# Customer Wise Spending
customer_spending = df.groupby("Customer_ID")["Total_Amount"].sum().sort_values(ascending=False)
print(customer_spending)

# Repeat VS New Customers
order_counts = df.groupby("Customer_ID")["Order_ID"].nunique()
repeat_customers = (order_counts > 1).sum()
new_customers = (order_counts == 1).sum()
print("Repeat Customers:",repeat_customers)
print("New Customers:",new_customers)

# Average Order Value
aov = df["Total_Amount"].sum()/df["Order_ID"].nunique()
print("Average Order Value:",aov)

# Top Customers
top_customers = customer_spending.head(10)
print(top_customers)

# Monthly Sales
df["Month"] = df["Order_Date"].dt.month
df.groupby("Month")["Total_Amount"].sum().plot(kind="line")
plt.show()

# Product Sales
df.groupby("Product")["Total_Amount"].sum().plot(kind="bar")
plt.title("Product Wise Total Sales")
plt.show()

# Visualization
top_customers.plot(kind="bar")
plt.title("Top 10 Customers")
plt.show()

df.to_csv("ecommerce_updated.csv", index=False)

## Key Insights
# - Total revenue: 3453464
# - Repeat Customers: 95
# - New Customers: 3
# - AOV: 6906.928
# - Top customers contribute highest revenue
# - Repeat customers are more valuable
# - Peak sales observed in specific months