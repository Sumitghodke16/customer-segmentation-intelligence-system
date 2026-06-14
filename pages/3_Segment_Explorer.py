import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("notebooks/customer_segments.csv")

st.title("📈 Segment Explorer")

st.write("Explore customer segments and business insights.")

# ----------------------------------
# Segment Selection
# ----------------------------------

segment = st.selectbox(
    "Select Customer Segment",
    df["Segment"].unique()
)

# Filter Data

filtered_df = df[df["Segment"] == segment]

# ----------------------------------
# KPI
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Customers",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Avg Frequency",
        round(filtered_df["Frequency"].mean(),2)
    )

with col3:
    st.metric(
        "Total Revenue",
        round(filtered_df["Monetary"].sum(),2)
    )

# ----------------------------------
# Top Customers
# ----------------------------------

st.subheader("Top Customers")

top_customers = (
    filtered_df
    .sort_values(
        by="Monetary",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top_customers,
    use_container_width=True
)

# ----------------------------------
# Revenue Chart
# ----------------------------------

st.subheader("Top Revenue Customers")

fig = px.bar(
    top_customers,
    x="CustomerID",
    y="Monetary",
    color="Monetary"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# Frequency Chart
# ----------------------------------

st.subheader("Purchase Frequency")

fig2 = px.scatter(
    filtered_df,
    x="Frequency",
    y="Monetary",
    color="Monetary",
    hover_data=["CustomerID"]
)

st.plotly_chart(
    fig2,
    use_container_width=True
)