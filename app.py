import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# --- AWS RDS connection ---
db_user = "admin"
db_password = "Nithin20045"
db_host = "financedb1.c890gm8wwf6l.us-east-1.rds.amazonaws.com"
db_name = "financedb1"

# Connect to RDS
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:3306/{db_name}")

# --- Streamlit Layout ---
st.title("💰 Personal Finance Tracker")

# Fetch data
df = pd.read_sql("SELECT * FROM expenses", engine)

st.subheader("Raw Expense Data")
st.dataframe(df)

# --- Spending by Category ---
st.subheader("Spending by Category")
category_data = df.groupby("category")["amount"].sum().sort_values(ascending=False)
st.bar_chart(category_data)

# --- Monthly Spending Trend ---
st.subheader("Monthly Spending Trend")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_data = df.groupby('month')['amount'].sum()
st.line_chart(monthly_data)

# --- Top 5 Biggest Expenses ---
st.subheader("Top 5 Biggest Expenses")
top5 = df.nlargest(5, 'amount')[['date', 'description', 'amount', 'category']]
st.table(top5)
