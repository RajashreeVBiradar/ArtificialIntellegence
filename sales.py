import pandas as pd
import matplotlib.pyplot as plt

# Load sample sales data (replace with your data source)
# Example using a sample CSV file:
sales_data = pd.read_csv("salesdata_new.csv")

# Preprocess data (adapt based on your data source)
# Assuming columns include "product_id", "product_name", "quantity", "price", "date", "region"
sales_data["revenue"] = sales_data["quantity"] * sales_data["price"]  # Calculate revenue per transaction

# Top-Selling Products Analysis
top_selling_products = (
 sales_data.groupby("product_name")["revenue"]
 .sum()
.reset_index()
 .sort_values(by="revenue", ascending=False)
 .head(10)  # Show top 10
)
"""sales_data.group=sales_data.groupby("product_name")
sales_data.group_revenue=sales_data.group["revenue"].sum()
sales_data.group_revenue_reset_index=sales_data.group_revenue.reset_index()
sales_data.group_revenue_reset_index_sort_values=sales_data.group_revenue_reset_index.sort_values(by="revenue", ascending=False)
     # Show top 10"""


# Sales Trends Over Time Analysis (assuming "date" is a datetime format)
sales_by_date = sales_data.groupby("date")["revenue"].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(sales_by_date["date"], sales_by_date["revenue"])
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Sales Performance by Region Analysis
sales_by_region = sales_data.groupby("region")["revenue"].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(sales_by_region["revenue"], labels=sales_by_region["region"], autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.show()

# Additional Analysis (optional)
# You can explore further analysis based on your data:
# * Compare sales performance across different demographics (e.g., customer age groups)
# * Identify products with the highest profit margin
# * Analyze trends in customer behavior (e.g., most popular purchase combinations)

print("Top 10 Selling Products:")
print(top_selling_products.to_string(index=False))