import streamlit as st
import pandas as pd

# Load data

df = pd.read_csv(
    "notebooks/customer_segments.csv"
)

st.title("📢 Marketing Action Center")

st.write(
    "Customer Segments and Recommended Marketing Actions"
)

# Segment Summary

st.subheader("Segment Summary")

segment_summary = (
    df.groupby("Segment")
      .agg({
          "CustomerID":"count",
          "Monetary":"sum"
      })
      .reset_index()
)

segment_summary.columns = [
    "Segment",
    "Customers",
    "Revenue"
]

st.dataframe(
    segment_summary,
    use_container_width=True
)

# Marketing Action Table

st.subheader("Recommended Actions")

actions = pd.DataFrame({

    "Segment":[
        "VIP Customer",
        "Loyal Customer",
        "Regular Customer",
        "Inactive Customer"
    ],

    "Action":[
        "Premium Membership Program",
        "Loyalty Rewards",
        "Upsell Campaign",
        "Retention Campaign"
    ]
})

st.dataframe(
    actions,
    use_container_width=True
)

# Select Segment

st.subheader(
    "Download Customer List"
)

selected_segment = st.selectbox(

    "Choose Segment",

    df["Segment"].unique()
)

filtered_df = df[
    df["Segment"] == selected_segment
]

st.write(
    f"Customers Found: {len(filtered_df)}"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download Button

csv = filtered_df.to_csv(
    index=False
)

st.download_button(

    label="📥 Download Customer List",

    data=csv,

    file_name=f"{selected_segment}.csv",

    mime="text/csv"
)