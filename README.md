# Economic Data Visualizer

A Python application that retrieves and visualizes real economic data from the World Bank API. Perfect for analyzing economic trends and comparing countries' GDP performance over time.

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🌟 Features

- **Real-time data retrieval** from World Bank API
- **Interactive visualizations** showing GDP trends over time
- **Easy country comparison** with simple code modifications
- **Professional charts** with clean formatting
- **Error handling** for robust performance
- **Beginner-friendly code** with detailed comments

## 📊 Sample Output

The application generates professional economic visualizations like this:

*GDP trends showing economic growth patterns from 2013-2023*

## 🚀 Quick Start

### Prerequisites

- Python 3.13+ 
- Internet connection (for API calls)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ADS2001/Economic-Data-Visualizer.git
   cd economic-data-visualizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python src/economic_visualizer.py
   ```

## 📈 Usage Examples

### Basic Usage
```python
# Run the main script to see USA GDP data
python src/economic_visualizer.py
```

### Customize for Different Countries
```python
# Edit the country code in the URL:
# Change 'US' to 'CA' for Canada
# Change 'US' to 'GB' for United Kingdom
# Change 'US' to 'DE' for Germany
```

### Available Economic Indicators
- `NY.GDP.MKTP.CD` - GDP (current US$)
- `SL.UEM.TOTL.ZS` - Unemployment rate (%)
- `FP.CPI.TOTL.ZG` - Inflation rate (%)
- `SP.POP.TOTL` - Population, total

## 🛠️ Technical Details

### Architecture
- **Data Source**: World Bank Indicators API
- **Visualization**: Matplotlib
- **Data Processing**: Native Python with error handling
- **Format**: JSON data retrieval and processing

### API Integration
The application uses the World Bank API v2 with the following structure:
```
https://api.worldbank.org/v2/country/{COUNTRY}/indicator/{INDICATOR}?format=json&date={DATE_RANGE}
```

### Code Structure
```
economic-data-visualizer/
├── src/
│   └── economic_visualizer.py    # Main application
├── requirements.txt              # Dependencies
├── README.md                    # Documentation
├── .gitignore                   # Git ignore rules
└── LICENSE                      # MIT License
```

## 📚 What I Learned

Building this project taught me:

- **API Integration**: How to connect to real economic databases
- **Data Processing**: Converting raw JSON into usable data structures
- **Error Handling**: Making robust applications that handle network issues
- **Data Visualization**: Creating professional charts with matplotlib
- **Documentation**: Writing clear, professional README files
- **Version Control**: Using Git and GitHub for project management

## 🌍 Future Enhancements

- [ ] Add support for multiple countries in one chart
- [ ] Include more economic indicators (inflation, unemployment)
- [ ] Create interactive web dashboard with Streamlit
- [ ] Add data export functionality (CSV, Excel)
- [ ] Implement caching for faster repeated queries
- [ ] Add statistical analysis (correlations, trends)

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **World Bank** for providing free access to their economic data API
- **Claude (Anthropic)** for guidance and assistance during development
- **University of Alberta** community for inspiration and support
- **Python community** for excellent data science libraries

## 👨‍💻 Author

**ARUNAVO DUTTA**
- International Student at University of Alberta
- Studying *Computer Science*
- Interested in data science and economic analysis

---

⭐ Star this repository if you found it helpful!

*Built with Python and curiosity about global economics* 🌎📊