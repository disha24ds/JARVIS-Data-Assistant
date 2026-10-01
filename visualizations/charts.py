import pandas as pd
import plotly.express as px


def sales_distribution(df):

    fig = px.histogram(
        df,
        x="Total Sales",
        y="Category",
        nbins=20,
        title="Sales Distribution"
    )

    return fig


def sales_by_region(df):

    region_sales = (
        df.groupby("Region", as_index=False)["Total Sales"]
        .sum()
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Total Sales",
        title="Total Sales by Region"
    )

    return fig


def sales_by_month(df):

    temp = df.copy()

    temp["Month"] = temp["Date"].dt.month_name()

    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    month_sales = (
        temp.groupby("Month", as_index=False)["Total Sales"]
        .sum()
    )

    month_sales["Month"] = pd.Categorical(
        month_sales["Month"],
        categories=month_order,
        ordered=True
    )

    month_sales = month_sales.sort_values("Month")

    fig = px.bar(
        month_sales,
        x="Month",
        y="Total Sales",
        title="Total Sales by Month"
    )

    return fig