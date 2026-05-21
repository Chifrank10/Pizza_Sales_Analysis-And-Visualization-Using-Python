def daily_revenue(pizza_df):
    return pizza_df.groupby("order_date")["total_price"].sum()


def monthly_revenue(pizza_df):
    return pizza_df.groupby("order_month")["total_price"].sum()


def revenue_by_category(pizza_df):
    return pizza_df.groupby("pizza_category")["total_price"].sum()


def revenue_by_size(pizza_df):
    return pizza_df.groupby("pizza_size")["total_price"].sum()


def hourly_sales(pizza_df):
    return pizza_df.groupby("order_hour")["total_price"].sum()


def weekday_sales(pizza_df):
    return pizza_df.groupby("order_dow")["total_price"].sum()


def top_selling_pizzas(pizza_df, top_n=10):
    return (
        pizza_df.groupby("pizza_name")["total_price"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )


def least_selling_pizzas(pizza_df, top_n=10):
    return (
        pizza_df.groupby("pizza_name")["total_price"]
        .sum()
        .sort_values()
        .head(top_n)
    )