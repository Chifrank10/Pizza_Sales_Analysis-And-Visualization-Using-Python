import matplotlib.pyplot as plt
import analysis as an


def plot_daily_revenue(pizza_df):
    data = an.daily_revenue(pizza_df)
    plt.figure()
    data.plot(kind="line")
    plt.title("Daily Revenue Trend")
    plt.show()


def plot_monthly_revenue(pizza_df):
    data = an.monthly_revenue(pizza_df)
    plt.figure()
    data.sort_index().plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.show()


def plot_revenue_by_category(pizza_df):
    data = an.revenue_by_category(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Revenue by Category")
    plt.show()


def plot_revenue_by_size(pizza_df):
    data = an.revenue_by_size(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Revenue by Size")
    plt.show()


def plot_hourly_sales(pizza_df):
    data = an.hourly_sales(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Hourly Sales")
    plt.show()


def plot_weekday_sales(pizza_df):
    data = an.weekday_sales(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Weekday Sales")
    plt.show()


def plot_top_selling_pizzas(pizza_df):
    data = an.top_selling_pizzas(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Top Selling Pizzas")
    plt.xticks(rotation=45)
    plt.show()


def plot_least_selling_pizzas(pizza_df):
    data = an.least_selling_pizzas(pizza_df)
    plt.figure()
    data.plot(kind="bar")
    plt.title("Least Selling Pizzas")
    plt.xticks(rotation=45)
    plt.show()


def plot_quantity_distribution(pizza_df):
    pizza_df["quantity"].value_counts().sort_index().plot(kind="bar")
    plt.title("Quantity Distribution")
    plt.show()