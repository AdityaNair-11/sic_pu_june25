import matplotlib.pyplot as plt

#used for the 1st objective (Identify the Top 3 Sectors (Routes) for IndiGo)
def plot_top_sectors(df, sectors):
    for s in sectors:
        data = df[df["Sector"] == s]
        monthly = data.groupby("Month")["Passengers"].sum()
        plt.plot(monthly.index, monthly.values, label=s)
    plt.title("Top 3 Route Trends")
    plt.xlabel("Month")
    plt.ylabel("Passengers")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#used for (5.How Airlines are coming up with New Routes?(top 5 growing routes or in demand routes))
def plot_growing_sectors(df, sectors):
    for s in sectors:
        data = df[df["Sector"] == s]
        monthly = data.groupby("Month")["Passengers"].sum()
        plt.plot(monthly.index, monthly.values, label=s)
    plt.title("Growing Route Trends")
    plt.xlabel("Month")
    plt.ylabel("Passengers")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#used for (3.Year-wise Growth of IndiGo's Market Share)
def plot_market_share(df):
    df["Share"] = df["Market_Share"].str.replace('%', '').astype(float)

    plt.figure(figsize=(12, 6))
    plt.bar(df["Month"], df["Share"], color="mediumpurple", width=20)  # width controls the bar thickness
    plt.title("IndiGo Market Share (Bar Chart)")
    plt.xlabel("Month")
    plt.ylabel("Market Share (%)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt

#used for (2.Identifying the Busiest months of every Routes)
def plot_busiest_months(df):
    # Limit to first 100 entries
    df = df.head(100)
    
    sectors = df["Sector"]
    passengers = df["Passengers"]
    months = df["Month"].dt.strftime("%b %Y")

    # Adjust figure size to avoid label overlapping
    plt.figure(figsize=(16, 6))
    bars = plt.bar(sectors, passengers, color="skyblue")
    
    plt.title("Busiest Month per Route (Sample of 100 rows)")
    plt.xlabel("Route")
    plt.ylabel("Passenger Count")
    plt.xticks(rotation=90, ha='center', fontsize=7)  # Small font for readability

    # Add month as label above bars
    for bar, month in zip(bars, months):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 200, month,
                 ha='center', va='bottom', fontsize=6, rotation=90)

    plt.tight_layout()
    plt.show()
#used for (3. Seasonal Travel Peaks)
def plot_seasonal_peaks(seasonal_series):
    plt.figure(figsize=(10, 5))
    seasonal_series.plot(kind='bar', color='teal')
    plt.title("Seasonal Travel Peaks by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Passengers")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
