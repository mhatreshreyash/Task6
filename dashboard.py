pip install pandas numpy matplotlib seaborn plotly

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("sales_data.csv")

print(df.head())

print(df.info())

print(df.describe())

df['Date'] = pd.to_datetime(df['Date'])

sns.set_style("whitegrid")

sns.set_palette("Blues")

plt.rcParams['figure.figsize'] = (10,6)

print("========== KPI SUMMARY ==========")

print("Total Sales:", df['Total_Sales'].sum())

print("Average Sales:", df['Total_Sales'].mean())

print("Top Product:",
      df.groupby('Product')['Total_Sales'].sum().idxmax())

print("Top Region:",
      df.groupby('Region')['Total_Sales'].sum().idxmax())

sales_trend = df.groupby('Date')['Total_Sales'].sum().reset_index()

plt.figure(figsize=(12,6))

sns.lineplot(
    x='Date',
    y='Total_Sales',
    data=sales_trend,
    marker='o'
)

plt.title('Sales Trend Over Time')

plt.xlabel('Date')

plt.ylabel('Total Sales')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

product_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()

plt.figure(figsize=(10,6))

sns.barplot(
    x='Product',
    y='Total_Sales',
    data=product_sales
)

plt.title('Product Performance')

plt.xlabel('Product')

plt.ylabel('Total Sales')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


plt.figure(figsize=(10,6))

sns.boxplot(
    x='Region',
    y='Total_Sales',
    data=df
)

plt.title('Sales Distribution by Region')

plt.xlabel('Region')

plt.ylabel('Total Sales')

plt.tight_layout()

plt.show()

plt.figure(figsize=(10,6))

sns.violinplot(
    x='Product',
    y='Total_Sales',
    data=df
)

plt.title('Sales Density by Product')

plt.xlabel('Product')

plt.ylabel('Total Sales')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

plt.figure(figsize=(10,6))

sns.histplot(
    df['Total_Sales'],
    bins=10,
    kde=True
)

plt.title('Sales Distribution Histogram')

plt.xlabel('Total Sales')

plt.ylabel('Frequency')

plt.tight_layout()

plt.show()

numeric_df = df[['Quantity', 'Price', 'Total_Sales']]

correlation = numeric_df.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title('Correlation Heatmap')

plt.tight_layout()

plt.show()



fig, axes = plt.subplots(2, 2, figsize=(14,10))

# Line Chart
sns.lineplot(
    x='Date',
    y='Total_Sales',
    data=sales_trend,
    ax=axes[0,0]
)

axes[0,0].set_title('Sales Trend')

# Bar Chart
sns.barplot(
    x='Product',
    y='Total_Sales',
    data=product_sales,
    ax=axes[0,1]
)

axes[0,1].set_title('Product Performance')

# Box Plot
sns.boxplot(
    x='Region',
    y='Total_Sales',
    data=df,
    ax=axes[1,0]
)

axes[1,0].set_title('Regional Sales Distribution')

# Violin Plot
sns.violinplot(
    x='Product',
    y='Total_Sales',
    data=df,
    ax=axes[1,1]
)

axes[1,1].set_title('Sales Density')

plt.tight_layout()

plt.show()

fig = px.scatter(
    df,
    x='Quantity',
    y='Total_Sales',
    color='Product',
    size='Price',
    hover_data=['Region', 'Customer_ID'],
    title='Interactive Sales Analysis'
)

fig.show()

fig = px.bar(
    product_sales,
    x='Product',
    y='Total_Sales',
    color='Product',
    title='Interactive Product Sales'
)

fig.show()

region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()

fig = px.pie(
    region_sales,
    names='Region',
    values='Total_Sales',
    title='Regional Sales Distribution'
)

fig.show()

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        'Sales Trend',
        'Product Sales',
        'Sales Distribution',
        'Sales vs Quantity'
    )
)

# Sales Trend
fig.add_trace(
    go.Scatter(
        x=sales_trend['Date'],
        y=sales_trend['Total_Sales'],
        mode='lines+markers',
        name='Sales Trend'
    ),
    row=1,
    col=1
)

# Product Sales
fig.add_trace(
    go.Bar(
        x=product_sales['Product'],
        y=product_sales['Total_Sales'],
        name='Product Sales'
    ),
    row=1,
    col=2
)

# Sales Distribution
fig.add_trace(
    go.Box(
        y=df['Total_Sales'],
        name='Sales Distribution'
    ),
    row=2,
    col=1
)

# Scatter Plot
fig.add_trace(
    go.Scatter(
        x=df['Quantity'],
        y=df['Total_Sales'],
        mode='markers',
        name='Sales vs Quantity'
    ),
    row=2,
    col=2
)

fig.update_layout(
    height=800,
    width=1200,
    title_text='Interactive Sales Dashboard',
    showlegend=False
)

fig.show()


