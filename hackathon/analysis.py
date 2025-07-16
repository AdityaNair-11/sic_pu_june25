import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Flight Data Analysis
# -------------------------------
class FlightDataAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

        # Combine year and month into one column
        self.df['Month'] = pd.to_datetime(self.df['Year'].astype(str) + '-' + self.df['Month'].astype(str) + '-01')

        # Keep only needed columns
        self.df = self.df[['Month', 'Sector', 'Passengers']]

    def get_top_sectors(self):
        top = self.df.groupby("Sector")["Passengers"].sum().sort_values(ascending=False).head(3)
        print("\nTop 3 routes with most passengers:")
        print(top)
        return top.index.tolist()

    def plot_top_sectors(self, sectors):
        for s in sectors:
            data = self.df[self.df["Sector"] == s]
            monthly = data.groupby("Month")["Passengers"].sum()
            plt.plot(monthly.index, monthly.values, label=s)
        plt.title("Top 3 Route Trends")
        plt.xlabel("Month")
        plt.ylabel("Passengers")
        plt.legend()
        plt.show()

    def get_growing_sectors(self):
        growth = []
        for s in self.df["Sector"].unique():
            data = self.df[self.df["Sector"] == s].sort_values("Month")
            if len(data) >= 6:
                start = data.iloc[0]["Passengers"]
                end = data.iloc[-1]["Passengers"]
                if start > 0:
                    percent = ((end - start) / start) * 100
                    growth.append((s, percent))
        growth.sort(key=lambda x: x[1], reverse=True)
        print("\nTop 5 growing routes:")
        for i in range(5):
            print(f"{growth[i][0]} - {round(growth[i][1], 2)}%")
        return [g[0] for g in growth[:5]]

    def plot_growing_sectors(self, sectors):
        for s in sectors:
            data = self.df[self.df["Sector"] == s]
            monthly = data.groupby("Month")["Passengers"].sum()
            plt.plot(monthly.index, monthly.values, label=s)
        plt.title("Growing Route Trends")
        plt.xlabel("Month")
        plt.ylabel("Passengers")
        plt.legend()
        plt.show()

# -------------------------------
# IndiGo Market Share Analysis
# -------------------------------
class IndiGoAnalyzer:
    def __init__(self, filepath):
        df = pd.read_csv(filepath)
        df['Month'] = pd.to_datetime(df['Month'])
        df = df[df['Airline'].str.lower() == 'indigo']
        self.df = df.sort_values("Month")

    def plot_market_share(self):
        self.df["Share"] = self.df["Market_Share"].str.replace('%', '').astype(float)
        plt.plot(self.df["Month"], self.df["Share"], marker='o', color='purple')
        plt.title("IndiGo Market Share")
        plt.xlabel("Month")
        plt.ylabel("Market Share (%)")
        plt.grid()
        plt.show()

    def print_recent_share(self):
        print("\nRecent IndiGo market share:")
        print(self.df[["Month", "Market_Share"]].tail(10))
