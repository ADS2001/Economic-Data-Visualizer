"""
Economic Data Visualizer

A Python application that retrieves and visualizes economic data from the World Bank API.
This script demonstrates API integration, data processing, and visualization skills.

Author: Arunavo Dutta
University: University of Alberta
Created: August 2025
License: MIT

Special thanks to Claude (Anthropic) for guidance during development.
"""

import requests
import matplotlib.pyplot as plt
from typing import Tuple, List, Optional


class EconomicDataVisualizer:
    """
    A class for retrieving and visualizing economic data from the World Bank API.
    
    This class encapsulates the functionality to fetch GDP data and create
    professional visualizations, making it easy to analyze economic trends.
    """
    
    def __init__(self):
        """Initialize the visualizer with World Bank API configuration."""
        self.base_url = "https://api.worldbank.org/v2"
        self.default_indicator = "NY.GDP.MKTP.CD"  # GDP in current US dollars
        
    def fetch_gdp_data(self, country_code: str, start_year: int = 2013, 
                       end_year: int = 2023) -> Tuple[List[int], List[float]]:
        """
        Fetch GDP data for a specific country from the World Bank API.
        
        Args:
            country_code (str): ISO 2-letter country code (e.g., 'US', 'CA', 'GB')
            start_year (int): Starting year for data retrieval
            end_year (int): Ending year for data retrieval
            
        Returns:
            Tuple[List[int], List[float]]: Years and corresponding GDP values in trillions
            
        Raises:
            requests.RequestException: If API request fails
            ValueError: If no valid data is returned
        """
        # Construct the API URL
        url = (f"{self.base_url}/country/{country_code}/indicator/{self.default_indicator}"
               f"?format=json&date={start_year}:{end_year}")
        
        print(f"🌐 Fetching GDP data for {country_code.upper()}...")
        print(f"📅 Date range: {start_year}-{end_year}")
        
        try:
            # Make the API request
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Parse the JSON response
            data = response.json()
            
            # World Bank API returns [metadata, data] format
            if len(data) < 2 or not data[1]:
                raise ValueError(f"No data available for country: {country_code}")
            
            gdp_data = data[1]
            
            # Extract years and GDP values
            years = []
            gdp_values = []
            
            for item in gdp_data:
                if item.get('value') is not None:
                    years.append(int(item['date']))
                    # Convert to trillions for readability
                    gdp_values.append(item['value'] / 1e12)
            
            if not years:
                raise ValueError(f"No valid GDP data found for {country_code}")
            
            # Sort by year (oldest first)
            sorted_data = sorted(zip(years, gdp_values))
            years, gdp_values = zip(*sorted_data)
            
            print(f"✅ Successfully retrieved {len(years)} years of data")
            return list(years), list(gdp_values)
            
        except requests.RequestException as e:
            print(f"❌ Network error: {e}")
            raise
        except (KeyError, ValueError, TypeError) as e:
            print(f"❌ Data processing error: {e}")
            raise
    
    def create_gdp_visualization(self, country_code: str, years: List[int], 
                               gdp_values: List[float]) -> None:
        """
        Create a professional GDP visualization.
        
        Args:
            country_code (str): Country code for the title
            years (List[int]): List of years
            gdp_values (List[float]): List of GDP values in trillions
        """
        # Create the figure with professional styling
        plt.figure(figsize=(12, 8))
        
        # Create the main plot
        plt.plot(years, gdp_values, 
                marker='o', 
                linewidth=3, 
                markersize=8, 
                color='#2E86AB',
                markerfacecolor='white',
                markeredgewidth=2,
                label=f'{country_code.upper()} GDP')
        
        # Customize the plot
        plt.title(f'🌍 {country_code.upper()} Economic Growth: GDP Over Time', 
                 fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Year', fontsize=14, fontweight='bold')
        plt.ylabel('GDP (Trillions USD)', fontsize=14, fontweight='bold')
        
        # Add grid for better readability
        plt.grid(True, alpha=0.3, linestyle='--')
        
        # Improve tick formatting
        plt.xticks(years, rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        
        # Add legend
        plt.legend(fontsize=12, loc='upper left')
        
        # Improve layout
        plt.tight_layout()
        
        # Display the plot
        plt.show()
        
    def display_summary_statistics(self, country_code: str, years: List[int], 
                                 gdp_values: List[float]) -> None:
        """
        Display summary statistics for the GDP data.
        
        Args:
            country_code (str): Country code for display
            years (List[int]): List of years
            gdp_values (List[float]): List of GDP values in trillions
        """
        print(f"\n📊 GDP DATA SUMMARY FOR {country_code.upper()}")
        print("=" * 50)
        
        # Display year-by-year data
        for year, gdp in zip(years, gdp_values):
            print(f"{year}: ${gdp:.2f} trillion")
        
        # Calculate and display growth statistics
        if len(gdp_values) > 1:
            total_growth = ((gdp_values[-1] - gdp_values[0]) / gdp_values[0]) * 100
            annual_avg_growth = total_growth / (years[-1] - years[0])
            
            print(f"\n📈 GROWTH ANALYSIS")
            print("-" * 30)
            print(f"Total growth ({years[0]}-{years[-1]}): {total_growth:.1f}%")
            print(f"Average annual growth: {annual_avg_growth:.1f}%")
            print(f"Highest GDP: ${max(gdp_values):.2f} trillion ({years[gdp_values.index(max(gdp_values))]})")
            print(f"Lowest GDP: ${min(gdp_values):.2f} trillion ({years[gdp_values.index(min(gdp_values))]})")


def main():
    """
    Main function to run the Economic Data Visualizer.
    
    This function demonstrates the complete workflow:
    1. Initialize the visualizer
    2. Fetch economic data
    3. Create visualizations
    4. Display summary statistics
    """
    print("🌟 ECONOMIC DATA VISUALIZER 🌟")
    print("Connecting to World Bank API for real economic data")
    print("=" * 60)
    
    # Initialize the visualizer
    visualizer = EconomicDataVisualizer()
    
    # Configuration - easily modify these for different analyses
    COUNTRY_CODE = "US"  # Change to 'CA', 'GB', 'DE', 'JP', etc.
    START_YEAR = 2013
    END_YEAR = 2023
    
    try:
        # Fetch the data
        years, gdp_values = visualizer.fetch_gdp_data(
            country_code=COUNTRY_CODE,
            start_year=START_YEAR,
            end_year=END_YEAR
        )
        
        # Create the visualization
        visualizer.create_gdp_visualization(COUNTRY_CODE, years, gdp_values)
        
        # Display summary statistics
        visualizer.display_summary_statistics(COUNTRY_CODE, years, gdp_values)
        
        print(f"\n🎉 SUCCESS! Analyzed GDP data for {COUNTRY_CODE.upper()}")
        print("\n💡 NEXT STEPS:")
        print("• Try changing COUNTRY_CODE to 'CA' for Canada")
        print("• Modify the date range for different time periods")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 TROUBLESHOOTING:")
        print("• Check your internet connection")
        print("• Verify the country code is valid (US, CA, GB, etc.)")
        print("• Try a different date range")


if __name__ == "__main__":
    main()
