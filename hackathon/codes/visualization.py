import matplotlib.pyplot as plt

def plot_top_sectors(df, sectors):
    for s in sectors:
        data = df[df["Sector"] == s]
        monthly = data.groupby("Month")["Passengers"].sum()
        plt.plot(monthly.index, monthly.values, label=s)
    plt.title("Top 3 Route Trends")
    plt.xlabel("Month")
    plt.ylabel("Passengers")
    plt.legend()
    plt.show()

def plot_growing_sectors(df, sectors):
    for s in sectors:
        data = df[df["Sector"] == s]
        monthly = data.groupby("Month")["Passengers"].sum()
        plt.plot(monthly.index, monthly.values, label=s)
    plt.title("Growing Route Trends")
    plt.xlabel("Month")
    plt.ylabel("Passengers")
    plt.legend()
    plt.show()


def plot_market_share(df):
    df["Share"] = df["Market_Share"].str.replace('%', '').astype(float)
    plt.plot(df["Month"], df["Share"], color='orange')  # Line chart
    plt.title("IndiGo Market Share")
    plt.xlabel("Month")
    plt.ylabel("Market Share (%)")
    plt.grid()
    plt.show()




