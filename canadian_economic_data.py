# Canadian Economic Data Visualizer
# Perfect for University of Alberta students entering the Canadian job market!

import requests
import matplotlib.pyplot as plt
import pandas as pd

def get_country_gdp_data(country_code, country_name):
    """
    Get GDP data for any country from World Bank API
    """
    print(f"📊 Getting GDP data for {country_name}...")
    
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&date=2013:2023"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if len(data) < 2 or not data[1]:
            print(f"❌ No data available for {country_name}")
            return [], []
        
        gdp_data = data[1]
        
        years = []
        gdp_values = []
        
        for item in gdp_data:
            if item['value'] is not None:
                years.append(int(item['date']))
                gdp_values.append(item['value'] / 1e12)  # Convert to trillions
        
        # Sort by year
        sorted_data = sorted(zip(years, gdp_values))
        if sorted_data:
            years, gdp_values = zip(*sorted_data)
            return list(years), list(gdp_values)
        else:
            return [], []
    
    except Exception as e:
        print(f"❌ Error getting data for {country_name}: {e}")
        return [], []

def get_unemployment_data(country_code, country_name):
    """
    Get unemployment data - very relevant for students looking for jobs!
    """
    print(f"💼 Getting unemployment data for {country_name}...")
    
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/SL.UEM.TOTL.ZS?format=json&date=2013:2023"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if len(data) < 2 or not data[1]:
            return [], []
        
        unemployment_data = data[1]
        
        years = []
        unemployment_values = []
        
        for item in unemployment_data:
            if item['value'] is not None:
                years.append(int(item['date']))
                unemployment_values.append(item['value'])
        
        # Sort by year
        sorted_data = sorted(zip(years, unemployment_values))
        if sorted_data:
            years, unemployment_values = zip(*sorted_data)
            return list(years), list(unemployment_values)
        else:
            return [], []
    
    except Exception as e:
        print(f"❌ Error getting unemployment data for {country_name}: {e}")
        return [], []

def create_canada_vs_world_comparison():
    """
    Compare Canada with other major economies
    Perfect for showing understanding of Canadian economic position
    """
    countries = {
        'Canada': 'CA',
        'United States': 'US',
        'United Kingdom': 'GB',
        'Germany': 'DE',
        'Japan': 'JP'
    }
    
    plt.figure(figsize=(15, 10))
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
    
    # GDP Comparison
    ax1.set_title('🇨🇦 Canada vs Major Economies: GDP Comparison (2013-2023)', 
                  fontsize=16, fontweight='bold', pad=20)
    
    colors = ['#FF0000', '#0066CC', '#228B22', '#FFD700', '#800080']  # Canada in red
    
    for i, (country_name, country_code) in enumerate(countries.items()):
        years, gdp_values = get_country_gdp_data(country_code, country_name)
        
        if years and gdp_values:
            color = colors[i % len(colors)]
            linewidth = 4 if country_name == 'Canada' else 2  # Make Canada line thicker
            ax1.plot(years, gdp_values, marker='o', linewidth=linewidth, 
                    markersize=6, label=country_name, color=color)
    
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('GDP (Trillions USD)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Unemployment Comparison (Focus on Canada, US, UK)
    ax2.set_title('💼 Unemployment Rates: Canada vs Key Partners', 
                  fontsize=16, fontweight='bold', pad=20)
    
    unemployment_countries = {
        'Canada': 'CA',
        'United States': 'US', 
        'United Kingdom': 'GB'
    }
    
    for i, (country_name, country_code) in enumerate(unemployment_countries.items()):
        years, unemployment_values = get_unemployment_data(country_code, country_name)
        
        if years and unemployment_values:
            color = colors[i % len(colors)]
            linewidth = 4 if country_name == 'Canada' else 2
            ax2.plot(years, unemployment_values, marker='s', linewidth=linewidth, 
                    markersize=6, label=country_name, color=color)
    
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Unemployment Rate (%)', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return True

def create_canada_deep_dive():
    """
    Focus specifically on Canadian economic indicators
    Shows detailed knowledge of the Canadian economy
    """
    print("\n🇨🇦 Creating detailed Canadian economic analysis...")
    
    # Get multiple indicators for Canada
    indicators = {
        'GDP': 'NY.GDP.MKTP.CD',
        'GDP Per Capita': 'NY.GDP.PCAP.CD',
        'Inflation': 'FP.CPI.TOTL.ZG',
        'Unemployment': 'SL.UEM.TOTL.ZS'
    }
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('🇨🇦 Canadian Economic Indicators Dashboard (2013-2023)', 
                 fontsize=18, fontweight='bold')
    
    axes = [ax1, ax2, ax3, ax4]
    colors = ['#FF0000', '#0066CC', '#228B22', '#800080']
    
    for i, (indicator_name, indicator_code) in enumerate(indicators.items()):
        ax = axes[i]
        
        url = f"https://api.worldbank.org/v2/country/CA/indicator/{indicator_code}?format=json&date=2013:2023"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if len(data) >= 2 and data[1]:
                years = []
                values = []
                
                for item in data[1]:
                    if item['value'] is not None:
                        years.append(int(item['date']))
                        if indicator_name == 'GDP':
                            values.append(item['value'] / 1e12)  # Trillions
                        elif indicator_name == 'GDP Per Capita':
                            values.append(item['value'])  # Regular value
                        else:
                            values.append(item['value'])  # Percentage
                
                # Sort by year
                sorted_data = sorted(zip(years, values))
                if sorted_data:
                    years, values = zip(*sorted_data)
                    
                    ax.plot(years, values, marker='o', linewidth=3, 
                           markersize=7, color=colors[i], markerfacecolor='white', 
                           markeredgewidth=2)
                    
                    # Customize each subplot
                    if indicator_name == 'GDP':
                        ax.set_ylabel('GDP (Trillions CAD)')
                    elif indicator_name == 'GDP Per Capita':
                        ax.set_ylabel('GDP Per Capita (CAD)')
                    else:
                        ax.set_ylabel(f'{indicator_name} (%)')
                    
                    ax.set_title(f'{indicator_name}', fontweight='bold')
                    ax.grid(True, alpha=0.3)
                    ax.set_xticks(years[::2])  # Show every other year
                    
                    # Add trend line for visual appeal
                    if len(values) > 1:
                        z = pd.Series(values).rolling(window=3).mean()
                        ax.plot(years, z, '--', alpha=0.7, color=colors[i])
        
        except Exception as e:
            ax.text(0.5, 0.5, f'Data not available\n{indicator_name}', 
                   ha='center', va='center', transform=ax.transAxes)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("🍁 CANADIAN ECONOMIC DATA VISUALIZER 🍁")
    print("Perfect for University of Alberta students!")
    print("=" * 60)
    
    print("\n📊 Part 1: Canada vs World Major Economies")
    create_canada_vs_world_comparison()
    
    print("\n📈 Part 2: Deep Dive into Canadian Economic Indicators")
    create_canada_deep_dive()
    
    print("\n🎉 ANALYSIS COMPLETE!")
    print("\n💡 What this shows employers:")
    print("✅ You understand Python and data visualization")
    print("✅ You can work with real economic APIs")
    print("✅ You understand the Canadian economic landscape")
    print("✅ You can present complex data clearly")
    print("✅ You have initiative to learn independently")
    
    print("\n🚀 Next steps for your portfolio:")
    print("• Add this to GitHub with good documentation")
    print("• Create a web dashboard version")
    print("• Add Alberta-specific economic data")
    print("• Include analysis of key Canadian industries")
