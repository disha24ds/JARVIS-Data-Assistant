def calculate_kpis(df):
    kpis={
        "Total_sales": df["Total Sales"].sum(),
        "Average_sales": df["Total Sales"].mean(),
        "Total_unit_solds": df["Units Sold"].sum(),
        "Minimum_sales": df["Total Sales"].min(),
        "Maximum_sales": df["Total Sales"].max()

    }
    return kpis

def sales_by_region(df):
    return df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)

def sales_by_month(df):
    return df.groupby(df["Date"].dt.month_name())["Total Sales"].sum().sort_values(ascending=False)
