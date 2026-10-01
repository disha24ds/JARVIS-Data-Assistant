from analysis.kpi import calculate_kpis


def answer_question(df, command):

    kpis = calculate_kpis(df)

    command = command.lower().strip()

    print("DEBUG COMMAND:", command)

    # TOTAL SALES
    if "total sales" in command or "total sale" in command:
        return f"Total sales are {kpis['Total_sales']:,.2f}."

    # AVERAGE SALES
    elif (
        "average sales" in command
        or "average sale" in command
        or "avg sales" in command
        or "avg sale" in command
    ):
        return f"Average sales are {kpis['Average_sales']:,.2f}."

    # MINIMUM SALES
    elif (
        "minimum sales" in command
        or "minimum sale" in command
        or "min sales" in command
        or "min sale" in command
    ):
        return f"The minimum sales value is {kpis['Minimum_sales']:,.2f}."

    # MAXIMUM SALES
    elif (
        "maximum sales" in command
        or "maximum sale" in command
        or "max sales" in command
        or "max sale" in command
    ):
        return f"The maximum sales value is {kpis['Maximum_sales']:,.2f}."

    # TOTAL QUANTITY
    elif (
        "total quantity" in command
        or "total unit" in command
        or "units sold" in command
        or "unit sold" in command
        or "quantity sold" in command
    ):
        return f"Total quantity is {kpis['Total_unit_solds']:,.0f}."

    # HIGHEST SALES REGION
    elif (
        "highest sales region" in command
        or "region has the highest sales" in command
        or "highest sales by region" in command
    ):
        region_sales = df.groupby("Region")["Total Sales"].sum()

        region = region_sales.idxmax()
        value = region_sales.max()

        return f"{region} has the highest sales with {value:,.2f}."

    # LOWEST SALES REGION
    elif (
        "lowest sales region" in command
        or "region has the lowest sales" in command
        or "lowest sales by region" in command
    ):
        region_sales = df.groupby("Region")["Total Sales"].sum()

        region = region_sales.idxmin()
        value = region_sales.min()

        return f"{region} has the lowest sales with {value:,.2f}."

    # HIGHEST SALES MONTH
    elif (
        "highest sales month" in command
        or "month has the highest sales" in command
        or "highest sales by month" in command
        or "which month has the highest sales" in command
        or "what month has the highest sales" in command
        or "month with the highest sales" in command
        or "highest selling month" in command
    ):
        month_sales = df.groupby(
            df["Date"].dt.month_name()
        )["Total Sales"].sum()

        month = month_sales.idxmax()
        value = month_sales.max()

        return f"{month} has the highest sales with {value:,.2f}."

    # LOWEST SALES MONTH
    elif (
        "lowest sales month" in command
        or "month has the lowest sales" in command
        or "lowest sales by month" in command
        or "which month has the lowest sales" in command
        or "what month has the lowest sales" in command
        or "month with the lowest sales" in command
        or "lowest selling month" in command
    ):
        month_sales = df.groupby(
            df["Date"].dt.month_name()
        )["Total Sales"].sum()

        month = month_sales.idxmin()
        value = month_sales.min()

        return f"{month} has the lowest sales with {value:,.2f}."

    # NUMBER OF ROWS
    elif (
        "number of rows" in command
        or "how many rows" in command
        or "how many records" in command
        or "number of records" in command
    ):
        return f"There are {len(df)} rows in the dataset."

    else:
        return "Sorry, I don't know that question yet."


def chart_command(command):

    command = command.lower().strip()

    # SALES DISTRIBUTION
    if (
        "sales distribution" in command
        or "sale distribution" in command
        or "distribution chart" in command
        or "distribution graph" in command
        or "show distribution" in command
        or "show sales distribution" in command
        or "distribution" in command
    ):
        return "distribution"

    # SALES BY REGION
    if (
        "sales by region" in command
        or "sale by region" in command
        or "region chart" in command
        or "region graph" in command
        or "regional sales" in command
    ):
        return "region"

    # SALES BY MONTH
    if (
        "sales by month" in command
        or "sale by month" in command
        or "monthly sales" in command
        or "month chart" in command
        or "month graph" in command
    ):
        return "month"

    # ALL CHARTS
    if (
        "all charts" in command
        or "all chart" in command
        or "all graphs" in command
        or "all graph" in command
        or "show all charts" in command
        or "show all graph" in command
        or "show all graphs" in command
    ):
        return "all"

    return None