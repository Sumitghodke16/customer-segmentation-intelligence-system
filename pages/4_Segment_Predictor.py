import streamlit as st
import pandas as pd
import joblib

# Load model and scaler

model = joblib.load(
    "notebooks/kmeans_customer_segmentation.pkl"
)

scaler = joblib.load(
    "notebooks/rfm_scaler.pkl"
)

st.title("🎯 Customer Segment Predictor")

st.write(
    "Enter customer RFM values to predict customer segment."
)

# Inputs
recency = st.number_input(
    "Recency (Days Since Last Purchase: 0-373)",
    min_value=0,
    max_value=373,
    value=30
)

frequency = st.number_input(
    "Frequency (Number of Orders: 1-209)",
    min_value=1,
    max_value=209,
    value=5
)

monetary = st.number_input(
    "Monetary (Total Spending: £3.75-£280206)",
    min_value=3.75,
    max_value=280206.02,
    value=1000.0
)


# Predict Button

if st.button("Predict Segment"):

    input_data = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=[
            "Recency",
            "Frequency",
            "Monetary"
        ]
    )

    scaled_data = scaler.transform(
        input_data
    )

    cluster = model.predict(
        scaled_data
    )[0]

    # Cluster Mapping

    segment_map = {
        0: "Regular Customer",
        1: "Inactive Customer",
        2: "VIP Customer",
        3: "Loyal Customer"
    }

    recommendation_map = {
        "VIP Customer":
            "Offer Premium Membership and Exclusive Rewards",

        "Loyal Customer":
            "Offer Loyalty Rewards and Referral Programs",

        "Regular Customer":
            "Recommend Bundle Products and Upsell Campaigns",

        "Inactive Customer":
            "Send Discount Coupons and Retention Campaigns"
    }

    segment = segment_map.get(
        cluster,
        "Unknown"
    )

    recommendation = recommendation_map.get(
        segment,
        "No Recommendation"
    )

    st.success(
        f"Predicted Segment: {segment}"
    )

    st.subheader(
        "Marketing Recommendation"
    )

    st.info(
        recommendation
    )