import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from analysis.kpi import( calculate_kpis ,
    sales_by_region ,
    sales_by_month 
    )
from visualizations.charts import( sales_distribution,
                                sales_by_region,
                                sales_by_month
)

st_autorefresh(
    interval=1000,
    key="jarvis_refresh"
)

def get_chart_command():
    try:
        with open("chart_command.txt", "r") as file:
            return file.read().strip().lower()
    except FileNotFoundError:
        return "none"

chart_command = get_chart_command()

df=pd.read_csv("data/retail sales dataset.csv")
df["Date"]=pd.to_datetime(df["Date"],dayfirst=True)
print("JARVIS Data Assistant Started!!!")
print("---------------------")

print("Number of Rows:",df.shape[0])
print("Number of columns:",df.shape[1])

print("\n Columns")
print(df.columns.to_list())

print("\n First 5 rows")
print(df.head())

print("\n Missing Value")
print(df.isnull().sum())

print("\n Duplicated Values")
print(df.duplicated().sum())

print("\n Data Types")
print(df.dtypes)

print("\n Stastical Describe")
print(df.describe())

print("\n Negative Total sales")
print((df["Total Sales"]<0).sum())



kpi= calculate_kpis(df)
print("\n ======JARVIS KPIS REPORT=====")
for name, value in kpi.items():
    print(name, ":" ,value)

print("\n========SALES BY REGION=======")
region_sales= sales_by_region(df)
print(region_sales)

print("\n=========SALES BY MONTH========")
month_sales= sales_by_month(df)
print(month_sales)

if chart_command == "distribution":

    st.subheader("Sales Distribution")

    fig1 = sales_distribution(df)

    st.plotly_chart(
        fig1,
        width="stretch"
    )


elif chart_command == "region":

    st.subheader("Sales by Region")

    fig2 = sales_by_region(df)

    st.plotly_chart(
        fig2,
        width="stretch"
    )


elif chart_command == "month":

    st.subheader("Sales by Month")

    fig3 = sales_by_month(df)

    st.plotly_chart(
        fig3,
        width="stretch"
    )


elif chart_command == "all":

    st.subheader("Sales Distribution")

    fig1 = sales_distribution(df)

    st.plotly_chart(
        fig1,
        width="stretch"
    )

    st.subheader("Sales by Region")

    fig2 = sales_by_region(df)

    st.plotly_chart(
        fig2,
        width="stretch"
    )

    st.subheader("Sales by Month")

    fig3 = sales_by_month(df)

    st.plotly_chart(
        fig3,
        width="stretch"
    )


else:

    st.info("🎤 Ask JARVIS to open a chart.")