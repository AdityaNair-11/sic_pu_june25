from analysis import FlightDataAnalyzer, IndiGoAnalyzer

def main():
    # Flight sector analysis
    flight = FlightDataAnalyzer("flight_data.csv")
    
    # 1. Top 3 sectors
    top_sectors = flight.get_top_sectors()
    flight.plot_top_sectors(top_sectors)

    # 2. Growing sectors
    growing_sectors = flight.get_growing_sectors()
    flight.plot_growing_sectors(growing_sectors)

    # IndiGo market share analysis
    indigo = IndiGoAnalyzer("market_share.csv")
    
    # 3. IndiGo market trend
    indigo.plot_market_share()
    indigo.print_recent_share()

if __name__ == "__main__":
    main()
