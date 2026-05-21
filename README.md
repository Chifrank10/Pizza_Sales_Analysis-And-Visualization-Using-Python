# Pizza Sales Data Analysis Project 🍕

## Project Overview
This project analyzes transactional pizza sales data to uncover customer purchasing behavior, sales performance trends, operational demand patterns, and revenue-driving products. The analysis focuses on optimizing staffing schedules, improving inventory planning, and developing data-driven promotional strategies to enhance operational efficiency and business revenue.

The project combines business intelligence, exploratory data analysis, and operational insights using Python, SQL, Excel, and Power BI to support data-driven decision-making for a restaurant business.

---

## Business Problem
Restaurant businesses generate large volumes of sales data daily, but without proper analysis, valuable operational and revenue insights remain hidden.

The business faced challenges in:
- Identifying high-performing and low-performing pizza products
- Understanding customer purchasing behavior
- Detecting peak operational hours and demand periods
- Optimizing staffing allocation during busy periods
- Managing inventory efficiently
- Developing effective promotional strategies to improve revenue

This project addresses these challenges through comprehensive sales and operational analysis.

---

## Project Objective
The objective of this project is to perform a comprehensive analysis of pizza sales transactions to uncover customer purchasing behavior, evaluate sales and revenue performance, identify peak demand periods, optimize staffing schedules and inventory management, and develop data-driven promotional strategies that improve operational efficiency, product performance, and overall business revenue.

---

## Dataset Information
The dataset contains transactional pizza sales records, including:
- Order details
- Pizza categories and sizes
- Product pricing
- Quantity sold
- Date and time of orders
- Revenue generated per transaction

### Key Columns
- `order_id`
- `order_date`
- `order_time`
- `pizza_name`
- `pizza_category`
- `pizza_size`
- `quantity`
- `unit_price`
- `total_price`
- `pizza_ingredients`

---

## Tools & Technologies Used

- Python – Core programming language for data analysis and automation
- Pandas & NumPy – Data cleaning, transformation, and numerical analysis
- Matplotlib & Seaborn – Data visualization and exploratory analysis
- Jupyter Notebook (VS Code) – Interactive analysis and experimentation
- Visual Studio Code – Primary development environment
- Streamlit – Interactive web dashboard for KPI and visualization reporting
- Git & GitHub – Version control and project documentation
- CSV – Structured dataset format used for analysis

## Full BI Pipeline for Project
CSV → Python (analysis) → Streamlit (dashboard) → GitHub (portfolio
##  Project Architecture

Pizza Sales Analytics Project is structured into modular components:

Pizza_Data_analysis/
│
├── app/
│   └── dashboard.py        
│
├── src/
│   ├── analysis.py        
│   ├── cleaning.py
|   ├──visualization.py   
│
├── data/
│   └── Pizzavv.csv        
│
├── requirements.txt   
└── README.md              
## Analytical Engine

The analytical engine is built in `analysis.py`, which handles all business logic calculations.

It includes:

- Revenue calculations (daily, monthly, category-wise)
- Sales aggregation (hourly, weekday trends)
- Product performance ranking
- KPI computations

Example:

```python
def daily_revenue(pizza_df):
    return pizza_df.groupby("order_date")["total_price"].sum()
```
## Dashboard Preview

!(assets/dash1.png)

## Executive Summary
This project analyzes transactional pizza sales data to uncover customer purchasing behavior, sales performance trends, operational demand patterns, and revenue-driving products. The analysis focuses on optimizing staffing schedules, improving inventory planning, and developing data-driven promotional strategies to enhance operational efficiency and business revenue.The dashboard was designed in such a way that it was an analytic engine which would take future csv files of similar formart and give usefule output for management view and decision making

### Overall Business Findings
- The business generated strong revenue from a small group of high-performing pizza products.
- Large-sized pizzas contributed the highest share of revenue.
- Sales demand varied significantly across hours, weekdays, and months.
- Peak operational periods occurred during lunch and evening hours.
- Certain pizza categories consistently outperformed others in both sales quantity and revenue generation.
- Some low-performing products contributed minimal revenue despite occupying inventory resources.

### Key Insights
- A few top-selling pizzas accounted for a significant percentage of total sales revenue.
- Weekend sales volumes were higher than weekday sales.
- Peak demand periods indicated the need for optimized staffing allocation during high-traffic hours.
- Customer purchasing patterns showed stronger preference for specific pizza categories and sizes.
- Inventory demand was concentrated around frequently ordered ingredients and products.
- Underperforming pizzas presented opportunities for targeted promotions and menu optimization.

### Recommendations
- Increase staffing levels during peak lunch and evening periods to improve service efficiency.
- Prioritize inventory allocation for high-demand pizza ingredients and sizes.
- Implement promotional campaigns for low-performing products during off-peak periods.
- Focus marketing efforts on best-selling pizza categories to maximize revenue growth.
- Introduce bundle offers and upselling strategies to increase average order value.
- Continuously monitor sales trends to support data-driven operational decisions.

---

## Business Questions

### Sales & Revenue Analysis
1. What is the total revenue generated?
2. What is the total number of orders placed?
3. What is the total quantity of pizzas sold?
4. Which pizza categories generate the most revenue?
5. Which pizza sizes generate the most revenue?
6. Which individual pizzas generate the highest revenue?

### Product Performance Analysis
7. Which pizzas are the best-selling by quantity?
8. Which pizzas are the least-selling by quantity?
9. Which products contribute the least revenue?
10. Which pizza categories are most preferred by customers?

### Time-Based Analysis
11. When do peak demand periods occur?
12. Which hours record the highest order volume?
13. Which days generate the highest sales?
14. Are weekends busier than weekdays?

### Operational Analysis
15. Which periods require additional staffing?
16. Which products require higher inventory allocation?
17. Which low-performing products need promotional support?

---

## Data Cleaning & Preparation
The following data cleaning and preprocessing steps were performed:
- Checked for missing values
- Removed duplicate records
- Converted date and time columns to proper formats
- Created additional calculated columns for analysis
- Standardized categorical variables
- Validated revenue and quantity calculations

---

## Exploratory Data Analysis
The exploratory data analysis focused on:
- Revenue trends over time
- Sales distribution by pizza category and size
- Peak sales hours and weekdays
- Best-selling and least-selling pizzas
- Customer ordering behavior
- Product demand patterns
- Revenue contribution analysis

---

## Key Insights
- Large pizzas generated the highest revenue contribution.
- A small number of products accounted for a significant share of sales.
- Peak ordering periods occurred during lunch and evening hours.
- Weekend transactions exceeded weekday order volumes.
- Certain pizza categories consistently outperformed others.
- Some products showed low sales performance despite occupying inventory resources.

---

## Dashboard / Visualizations
The project includes interactive dashboards and visualizations such as:
- Total Revenue KPI
- Total Orders KPI
- Total Pizzas Sold KPI
- Revenue by Pizza Category
- Revenue by Pizza Size
- Top 10 Best-Selling Pizzas
- Least-Selling Pizzas
- Hourly Sales Trend
- Daily Sales Trend
- Peak Demand Heatmaps
- Product Performance Charts

---

## Recommendations
- Increase staffing levels during peak operational hours.
- Improve inventory planning for high-demand ingredients and products.
- Introduce promotions for underperforming pizzas.
- Focus marketing campaigns on top-performing pizza categories.
- Implement upselling and bundle strategies to increase average order value.
- Continuously monitor operational and sales trends for better decision-making.

---

## Conclusion
This project demonstrates how transactional sales data can be transformed into actionable business insights that support operational efficiency, inventory optimization, staffing management, and revenue growth.

By leveraging data analytics and visualization techniques, the analysis provides practical recommendations that can help restaurant businesses improve performance and make data-driven strategic decisions.
