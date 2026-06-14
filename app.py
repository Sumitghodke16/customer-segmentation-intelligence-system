import streamlit as st

st.set_page_config(
    page_title="Customer Intelligence System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Intelligence System")

st.markdown("""
### Customer Segmentation & Marketing Recommendation System

This application helps businesses:

- Identify VIP Customers
- Find Loyal Customers
- Detect Inactive Customers
- Predict Customer Segments
- Generate Marketing Recommendations

Built using:

- Python
- Streamlit
- KMeans Clustering
- Hierarchical Clustering
- DBSCAN
- RFM Analysis
""")

st.success("Project Successfully Loaded")