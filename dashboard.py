import streamlit as st
import pandas as pd
import analysis as an

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Pizza Analytics Engine", layout="wide")

st.markdown(
    "<h1 style='text-align:center;color:#ff4b4b;'>🍕 Pizza Analytics Engine</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------
# FILE UPLOADER (KEY FEATURE)
# -------------------------------
uploaded_file = st.file_uploader("📂 Upload your Pizza CSV file", type=["csv"])

if uploaded_file is None:
    st.info("Upload a CSV file to generate dashboard")
    st.stop()

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)

    # STANDARDIZE COLUMNS (IMPORTANT FOR REUSABILITY)
    df.columns = [c.strip().lower() for c in df.columns]

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["total_price"] = pd.to_numeric(df["total_price"], errors="coerce")

    df["order_hour"] = df["order_date"].dt.hour
    df["order_dow"] = df["order_date"].dt.day_name()
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    return df


pizza_df = load_data(uploaded_file)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    pizza_df["pizza_category"].dropna().unique(),
    default=pizza_df["pizza_category"].dropna().unique()
)

size_filter = st.sidebar.multiselect(
    "Size",
    pizza_df["pizza_size"].dropna().unique(),
    default=pizza_df["pizza_size"].dropna().unique()
)

filtered_df = pizza_df[
    (pizza_df["pizza_category"].isin(category_filter)) &
    (pizza_df["pizza_size"].isin(size_filter))
]

# -------------------------------
# KPI CALCULATION (DYNAMIC)
# -------------------------------
total_revenue = filtered_df["total_price"].sum()
total_orders = len(filtered_df)
total_pizzas = filtered_df["quantity"].sum()
avg_order = total_revenue / total_orders if total_orders else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Revenue", f"${total_revenue:,.0f}")
col2.metric("🧾 Orders", total_orders)
col3.metric("🍕 Pizzas", int(total_pizzas))
col4.metric("📊 Avg Order", f"${avg_order:,.2f}")

st.markdown("---")

# -------------------------------
# VISUALS (FULLY REUSABLE)
# -------------------------------
st.subheader("Revenue by Category")
st.bar_chart(an.revenue_by_category(filtered_df))

st.subheader("Revenue by Size")
st.bar_chart(an.revenue_by_size(filtered_df))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Pizzas")
    st.bar_chart(an.top_selling_pizzas(filtered_df))

with col2:
    st.subheader("Least Selling Pizzas")
    st.bar_chart(an.least_selling_pizzas(filtered_df))

st.subheader("Hourly Sales")
st.line_chart(an.hourly_sales(filtered_df))

st.subheader("Daily Sales")
st.line_chart(an.daily_revenue(filtered_df))

st.subheader("Weekday Sales")
st.bar_chart(an.weekday_sales(filtered_df))