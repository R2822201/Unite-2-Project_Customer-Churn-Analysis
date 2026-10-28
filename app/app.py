import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Credit Card Churn Analytics",
    page_icon="💳",
    layout="wide"
)

# Title and description
st.title("💳 Credit Card Customer Churn Analytics Dashboard")
st.markdown("Explore customer demographics, behavioral metrics, and churn predictors interactively.")

# Load data function
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/raw/BankChurners.csv")
    except FileNotFoundError:
        df = pd.read_csv("../data/raw/BankChurners.csv")
    return df

data_load_state = st.text("Loading data...")
try:
    df = load_data()
    data_load_state.text("Data loaded successfully!")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("Filter Options")
gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

card_filter = st.sidebar.multiselect(
    "Select Card Category",
    options=df["Card_Category"].unique(),
    default=df["Card_Category"].unique()
)

filtered_df = df[
    (df["Gender"].isin(gender_filter)) & 
    (df["Card_Category"].isin(card_filter))
]

# Main Metrics
col1, col2, col3, col4 = st.columns(4)
total_customers = len(filtered_df)
churned_customers = len(filtered_df[filtered_df["Attrition_Flag"] == "Attrited Customer"])
churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0
avg_credit_limit = filtered_df["Credit_Limit"].mean()

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Avg Credit Limit", f"${avg_credit_limit:,.0f}")

st.markdown("---")

# Visualizations
st.subheader("📊 Key Insights & Visualizations")

tab1, tab2, tab3 = st.tabs(["Demographics", "Financial Metrics", "Transaction Behavior"])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        fig_attrition = px.pie(
            filtered_df, 
            names="Attrition_Flag", 
            title="Customer Attrition Breakdown",
            hole=0.4
        )
        st.plotly_chart(fig_attrition, use_container_width=True)
    with col_b:
        fig_age = px.histogram(
            filtered_df, 
            x="Customer_Age", 
            color="Attrition_Flag", 
            barmode="overlay",
            title="Customer Age Distribution by Attrition"
        )
        st.plotly_chart(fig_age, use_container_width=True)

with tab2:
    col_c, col_d = st.columns(2)
    with col_c:
        fig_limit = px.box(
            filtered_df, 
            x="Attrition_Flag", 
            y="Credit_Limit", 
            color="Attrition_Flag",
            title="Credit Limit by Attrition Status"
        )
        st.plotly_chart(fig_limit, use_container_width=True)
    with col_d:
        fig_bal = px.box(
            filtered_df, 
            x="Attrition_Flag", 
            y="Total_Revolving_Bal", 
            color="Attrition_Flag",
            title="Total Revolving Balance by Attrition"
        )
        st.plotly_chart(fig_bal, use_container_width=True)

with tab3:
    col_e, col_f = st.columns(2)
    with col_e:
        fig_trans_amt = px.histogram(
            filtered_df, 
            x="Total_Trans_Amt", 
            color="Attrition_Flag", 
            barmode="group",
            title="Total Transaction Amount Distribution"
        )
        st.plotly_chart(fig_trans_amt, use_container_width=True)
    with col_f:
        fig_trans_ct = px.histogram(
            filtered_df, 
            x="Total_Trans_Ct", 
            color="Attrition_Flag", 
            barmode="group",
            title="Total Transaction Count Distribution"
        )
        st.plotly_chart(fig_trans_ct, use_container_width=True)

# Raw data preview
if st.checkbox("Show Raw Data Preview"):
    st.dataframe(filtered_df.head(100))

# Add CSV Download Button for Filtered Data
st.markdown("---")
st.subheader("📥 Export Filtered Data Subset")
csv_data = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_customer_segment.csv",
    mime="text/csv",
)
fig = px.pie(
    filtered_df, 
    names='Attrition_Flag', 
    color='Attrition_Flag',
    color_discrete_map={
        'Existing Customer': '#2A9D8F',  # Custom Teal
        'Attrited Customer': '#E76F51'   # Custom Coral/Orange
    }
)
st.plotly_chart(fig, use_container_width=True)

fig_financial = px.histogram(
    filtered_df, 
    x="Credit_Limit",  # Or whatever your financial metric column is named
    color="Attrition_Flag",
    color_discrete_map={
        'Existing Customer': '#2A9D8F',  # Custom Teal
        'Attrited Customer': '#E76F51'   # Custom Coral/Orange
    }
)

# Make sure to display it in Streamlit!
st.plotly_chart(fig_financial, use_container_width=True)


