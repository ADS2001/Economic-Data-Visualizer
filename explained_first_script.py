# Your First Economic Data Visualizer - EXPLAINED!
# Let's understand exactly how this works

# === IMPORTS: Getting the tools we need ===
import requests      # This lets us ask websites for data
import matplotlib.pyplot as plt  # This creates charts and graphs

# Think of imports like getting tools from a toolbox:
# - requests = tool for downloading data from the internet
# - matplotlib = tool for drawing charts

def get_simple_gdp_data():
    """
    This function gets GDP data for the USA from the World Bank
    Think of a function like a recipe - it has steps to follow
    """
    
    # === STEP 1: Build the URL (web address) ===
    # This is like writing down the address of a library
    url = "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json&date=2013:2023"
    
    # Let's break down this URL:
    # https://api.worldbank.org/v2/  <- The World Bank's data service
    # country/US/                   <- We want USA data
    # indicator/NY.GDP.MKTP.CD      <- GDP in current US dollars (this is World Bank's code for GDP)
    # ?format=json                  <- Give us the data in JSON format (easy for computers to read)
    # &date=2013:2023               <- Data from 2013 to 2023
    
    try:  # "try" means "attempt this, but be ready if something goes wrong"
        
        # === STEP 2: Ask the internet for data ===
        print("🌐 Asking World Bank for GDP data...")
        response = requests.get(url)
        # This is like calling a library and asking for a specific book
        # The "response" is what they give you back
        
        # === STEP 3: Convert the response to data we can use ===
        data = response.json()
        # JSON is like a filing cabinet - organized data in boxes
        # .json() unpacks that filing cabinet so we can look inside
        
        print(f"📦 Received data! Status: {response.status_code}")
        # Status code 200 = success, like getting a "yes" from the library
        
        # === STEP 4: Extract the actual numbers ===
        # The World Bank sends data in a specific format:
        # [metadata, actual_data]
        # We want the actual_data part, which is at position [1]
        gdp_data = data[1]
        
        # === STEP 5: Process each year's data ===
        years = []        # Empty list to store years
        gdp_values = []   # Empty list to store GDP numbers
        
        # Go through each piece of data
        for item in gdp_data:
            # Each "item" looks like this:
            # {"date": "2020", "value": 20950000000000, "country": {...}}
            
            if item['value'] is not None:  # Make sure we have real data (not empty)
                years.append(int(item['date']))  # Add the year (convert text to number)
                
                # GDP numbers are HUGE (like 20,950,000,000,000)
                # Divide by 1 trillion (1e12) to make them readable
                gdp_values.append(item['value'] / 1e12)
                
                print(f"📅 {item['date']}: ${item['value'] / 1e12:.2f} trillion")
        
        # === STEP 6: Sort by year (oldest first) ===
        sorted_data = sorted(zip(years, gdp_values))
        years, gdp_values = zip(*sorted_data)
        
        return list(years), list(gdp_values)  # Give back the processed data
    
    except Exception as e:
        # If ANYTHING goes wrong (internet down, bad URL, etc.), do this:
        print(f"❌ Something went wrong: {e}")
        return [], []  # Return empty lists so the program doesn't crash

def create_simple_chart():
    """
    This function creates the actual chart you see
    """
    print("🚀 Creating your GDP chart...")
    
    # === STEP 1: Get the data ===
    years, gdp_values = get_simple_gdp_data()
    # This calls our other function and gets the years and GDP numbers
    
    # === STEP 2: Check if we got data ===
    if not years:  # If the years list is empty
        print("❌ Couldn't get data. Check your internet connection!")
        return  # Stop here, don't try to make a chart
    
    # === STEP 3: Create the chart ===
    plt.figure(figsize=(10, 6))  # Make a canvas 10 inches wide, 6 inches tall
    
    # Draw the line on the chart
    plt.plot(years, gdp_values,     # x-axis = years, y-axis = GDP values
             marker='o',             # Put a circle (o) at each data point
             linewidth=2,            # Make the line 2 pixels thick
             markersize=6)           # Make the circles 6 pixels big
    
    # === STEP 4: Add labels and titles ===
    plt.title('USA GDP Over Time', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)      # Label for bottom axis
    plt.ylabel('GDP (Trillions USD)', fontsize=12)  # Label for left axis
    plt.grid(True, alpha=0.3)           # Add a faint grid to make it easier to read
    
    # === STEP 5: Make it look nice ===
    plt.tight_layout()  # Automatically adjust spacing so nothing gets cut off
    
    # === STEP 6: Show the chart ===
    plt.show()  # This opens a window with your chart!
    
    # === STEP 7: Also print the data as text ===
    print("\n📊 GDP Data Summary:")
    print("-" * 30)
    for year, gdp in zip(years, gdp_values):
        print(f"{year}: ${gdp:.2f} trillion")
    
    # Calculate and show growth
    if len(gdp_values) > 1:
        total_growth = ((gdp_values[-1] - gdp_values[0]) / gdp_values[0]) * 100
        print(f"\n📈 Total growth from {years[0]} to {years[-1]}: {total_growth:.1f}%")

# === MAIN PROGRAM STARTS HERE ===
if __name__ == "__main__":
    # This only runs when you run this file directly (not when imported)
    
    print("🌟 Your First Economic Data Visualizer! 🌟")
    print("This will show USA GDP data from the World Bank")
    print("-" * 50)
    
    # Call our function to create the chart
    create_simple_chart()
    
    print("\n🎉 Congratulations! You just:")
    print("✅ Connected to a real economic database")
    print("✅ Downloaded actual GDP data") 
    print("✅ Created your first data visualization")
    print("\n💡 Next step: Try changing 'US' to 'GB' for UK data!")
