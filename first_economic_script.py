# Your First Economic Data Visualizer
# This is a simple starting point - we'll build on this!
import requests
import matplotlib.pyplot as plt

def get_simple_gdp_data():
    """
    Get GDP data for USA from World Bank API
    Don't worry about understanding every detail yet!
    """
    # This URL gets USA GDP data for the last 10 years
    url = "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json&date=2013:2023"
    
    try:
        # Ask the internet for the data
        response = requests.get(url)
        data = response.json()
        
        # The data comes in a specific format - we extract what we need
        gdp_data = data[1]  # The actual data is in the second part
        
        years = []
        gdp_values = []
        
        # Go through each year's data
        for item in gdp_data:
            if item['value'] is not None:  # Make sure we have real data
                years.append(int(item['date']))
                gdp_values.append(item['value'] / 1e12)  # Convert to trillions for readability
        
        return years, gdp_values
    
    except Exception as e:
        print(f"Something went wrong: {e}")
        return [], []

def create_simple_chart():
    """
    Create a basic chart showing USA GDP over time
    """
    print("Getting GDP data...")
    years, gdp_values = get_simple_gdp_data()
    
    if not years:
        print("Couldn't get data. Check your internet connection!")
        return
    
    # Create the chart
    plt.figure(figsize=(10, 6))
    plt.plot(years, gdp_values, marker='o', linewidth=2, markersize=6)
    plt.title('USA GDP Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP (Trillions USD)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Make it look nice
    plt.tight_layout()
    
    # Show the chart
    plt.show()
    
    # Also print the data so you can see it
    print("\nGDP Data:")
    for year, gdp in zip(years, gdp_values):
        print(f"{year}: ${gdp:.2f} trillion")

if __name__ == "__main__":
    print("🌟 Your First Economic Data Visualizer! 🌟")
    print("This will show USA GDP data from the World Bank")
    print("-" * 50)
    
    create_simple_chart()
    
    print("\n🎉 Congratulations! You just:")
    print("✅ Connected to a real economic database")
    print("✅ Downloaded actual GDP data")
    print("✅ Created your first data visualization")
    print("\nNext step: Try changing 'US' to 'GB' for UK data!")
