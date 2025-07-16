import pandas as pd

class FlightDataAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.df['Month'] = pd.to_datetime(self.df['Year'].astype(str) + '-' + self.df['Month'].astype(str) + '-01')
        self.df = self.df[['Month', 'Sector', 'Passengers']]

    def get_top_sectors(self):
        top = self.df.groupby("Sector")["Passengers"].sum().sort_values(ascending=False).head(3)
        print("Top 3 routes with most passengers:")
        print(top)
        return top.index.tolist()

    def get_growing_sectors(self):
        growth = []
        for s in self.df["Sector"].unique():
            data = self.df[self.df["Sector"] == s].sort_values("Month")
            if len(data) >= 6:
                start = data.iloc[0]["Passengers"]
                end = data.iloc[-1]["Passengers"]
                if start > 0:
                    change = ((end - start) / start) * 100
                    growth.append((s, change))
        growth.sort(key=lambda x: x[1], reverse=True)
        print("Top 5 growing routes:")
        for s in growth[:5]:
            print(f"{s[0]} - {round(s[1], 2)}%")
        return [s[0] for s in growth[:5]]

    def get_busiest_months(self):
        busiest = self.df.loc[self.df.groupby("Sector")["Passengers"].idxmax()]
        print("Busiest month for each route:")
        print(busiest[["Sector", "Month", "Passengers"]])
        return busiest

    def get_seasonal_peaks(self):
        self.df["Month_Num"] = self.df["Month"].dt.month
        seasonal = self.df.groupby("Month_Num")["Passengers"].sum()
        return seasonal

class IndiGoAnalyzer:
    def __init__(self, filepath):
        df = pd.read_csv(filepath)
        df['Month'] = pd.to_datetime(df['Month'])
        self.df = df[df['Airline'].str.lower() == 'indigo'].sort_values("Month")

    def print_recent_share(self):
        print("Recent IndiGo market share:")
        print(self.df[["Month", "Market_Share"]].tail(10))
