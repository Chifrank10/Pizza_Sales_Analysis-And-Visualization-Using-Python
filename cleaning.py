import pandas as pd

def preprocess_data(pizza_df):

    pizza_df.columns = (
        pizza_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    pizza_df['order_date'] = pd.to_datetime(pizza_df['order_date'], errors='coerce')

    pizza_df['order_time'] = pd.to_datetime(
        pizza_df['order_time'],
        format='%H:%M:%S',
        errors='coerce'
    )

    numeric_cols = ['quantity', 'unit_price', 'total_price']

    for col in numeric_cols:
        pizza_df[col] = pd.to_numeric(pizza_df[col], errors='coerce')

    pizza_df['order_month'] = pizza_df['order_date'].dt.to_period('M').astype(str)
    pizza_df['order_day'] = pizza_df['order_date'].dt.date
    pizza_df['order_dow'] = pizza_df['order_date'].dt.day_name()
    pizza_df['order_hour'] = pizza_df['order_time'].dt.hour

    return pizza_df