import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("notebooks/customer_segments.csv")

st.title("🔍 Customer Lookup")

st.write("Search any customer and view segment information.")

# Customer ID input

customer_id = st.number_input(
    "Enter Customer ID",
    min_value=int(df["CustomerID"].min()),
    max_value=int(df["CustomerID"].max()),
    step=1
)

# Search button

if st.button("Search Customer"):

    result = df[df["CustomerID"] == customer_id]

    if len(result) > 0:

        row = result.iloc[0]

        st.success("Customer Found")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Recency", int(row["Recency"]))

        with col2:
            st.metric("Frequency", int(row["Frequency"]))

        with col3:
            st.metric("Monetary", round(row["Monetary"], 2))

        st.subheader("Customer Segment")

        st.info(row["Segment"])

        st.subheader("Marketing Recommendation")

        st.warning(row["Recommendation"])

    else:

        st.error("Customer Not Found")