
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Executive KPI Dashboard", layout="wide")

# Title and Intro
st.title("📊 Executive KPI Dashboard")
st.write("An interactive dashboard for visualizing key performance indicators across regions.")

# Sample KPI Data (can be replaced with database/Excel inputs)
data = {
    "Region": ["North", "South", "East", "West"],
    "Revenue ($)": [120000, 95000, 134000, 88000],
    "Profit Margin (%)": [22, 19, 25, 18],
    "Customer Satisfaction (%)": [89, 82, 91, 79],
    "Monthly Growth (%)": [5.2, 4.3, 6.1, 3.9]
}
df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.header("Filters")
selected_regions = st.sidebar.multiselect("Select Regions", df["Region"].unique(), default=df["Region"].unique())

# Filtered Data
filtered_df = df[df["Region"].isin(selected_regions)]

# Show Table
st.subheader("Filtered KPI Data")
st.dataframe(filtered_df)

# Charts
st.subheader("KPI Visualizations")
st.bar_chart(filtered_df.set_index("Region")[["Revenue ($)"]])
st.line_chart(filtered_df.set_index("Region")[["Profit Margin (%)"]])
st.area_chart(filtered_df.set_index("Region")[["Monthly Growth (%)"]])
