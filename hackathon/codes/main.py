from analysis import FlightDataAnalyzer, IndiGoAnalyzer
from visualization import (
    plot_top_sectors,
    plot_growing_sectors,
    plot_market_share,
    plot_busiest_months,
    plot_seasonal_peaks  
)

def main():
    flight = FlightDataAnalyzer("datasets/flight_data.csv")
    indigo = IndiGoAnalyzer("datasets/market_share.csv")

    while True:
        print("\n--- Flight Analysis CLI ---")
        print("1. Top 3 Routes with Most Passengers")
        print("2. Top 5 Growing Routes")
        print("3. Busiest Month per Route")
        print("4. Seasonal Travel Peaks")
        print("5. IndiGo Market Share Trend")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            top_sectors = flight.get_top_sectors()
            plot_top_sectors(flight.df, top_sectors)

        elif choice == "2":
            growing = flight.get_growing_sectors()
            plot_growing_sectors(flight.df, growing)

        elif choice == "3":
            busiest_df = flight.get_busiest_months()
            plot_busiest_months(busiest_df)

        elif choice == "4":
            seasonal_data = flight.get_seasonal_peaks()
            plot_seasonal_peaks(seasonal_data)

        elif choice == "5":
            plot_market_share(indigo.df)

        elif choice == "0":
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
