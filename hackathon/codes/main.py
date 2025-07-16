from analysis import FlightDataAnalyzer, IndiGoAnalyzer
from visualization import (
    plot_top_sectors,
    plot_growing_sectors,
    plot_market_share,
    plot_busiest_months,
    plot_seasonal_peaks  
)

def main():
    # Load flight data
    flight = FlightDataAnalyzer("datasets/flight_data.csv")
    
    # Top 3 sectors
    top_sectors = flight.get_top_sectors()
    plot_top_sectors(flight.df, top_sectors)

    # Top 5 growing sectors
    growing = flight.get_growing_sectors()
    plot_growing_sectors(flight.df, growing)

    # Busiest month per route
    busiest_df = flight.get_busiest_months()
    plot_busiest_months(busiest_df)

    #  Seasonal travel peaks
    seasonal_data = flight.get_seasonal_peaks()
    plot_seasonal_peaks(seasonal_data)

    # IndiGo analysis
    indigo = IndiGoAnalyzer("datasets/market_share.csv")
    plot_market_share(indigo.df)
    indigo.print_recent_share()

if __name__ == "__main__":
    main()
