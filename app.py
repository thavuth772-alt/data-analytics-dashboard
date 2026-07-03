import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Sales Data Analytics Dashboard", layout="wide")

st.title("Sales Data Analytics & Visualization Dashboard")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [25000, 32000, 28000, 40000, 45000, 52000],
    "Profit": [5000, 7000, 6000, 9000, 11000, 13000],
    "Orders": [120, 150, 135, 180, 210, 250]
}

df = pd.DataFrame(data)

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Basic Analytics")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Orders"].sum()
average_sales = df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales}")
col2.metric("Total Profit", f"₹{total_profit}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Sales", f"₹{average_sales:.2f}")

st.subheader("Monthly Sales Visualization")

fig1, ax1 = plt.subplots()
sns.barplot(x="Month", y="Sales", data=df, ax=ax1)
ax1.set_title("Monthly Sales")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
st.pyplot(fig1)

st.subheader("Profit Trend Visualization")

fig2, ax2 = plt.subplots()
sns.lineplot(x="Month", y="Profit", data=df, marker="o", ax=ax2)
ax2.set_title("Monthly Profit Trend")
ax2.set_xlabel("Month")
ax2.set_ylabel("Profit")
st.pyplot(fig2)

st.subheader("Orders vs Sales Comparison")

fig3, ax3 = plt.subplots()
ax3.plot(df["Month"], df["Sales"], marker="o", label="Sales")
ax3.plot(df["Month"], df["Orders"], marker="o", label="Orders")
ax3.set_title("Sales and Orders Comparison")
ax3.set_xlabel("Month")
ax3.legend()
st.pyplot(fig3)

st.subheader("Conclusion")

st.write("""
From this analysis, we can understand monthly sales performance, profit growth, 
and order trends. The highest sales and profit were achieved in June, showing 
positive business growth.
""")