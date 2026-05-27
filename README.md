# Stock Market ETL Pipeline

A beginner-friendly **data engineering project** demonstrating a complete ETL (Extract, Transform, Load) pipeline.

## 🎯 Project Objective

Build a production-like data pipeline that extracts stock market data, transforms it, and loads it into a relational database for analysis.

## ✅ What Was Built

### Part 1: Database Design & Setup
- Installed and configured PostgreSQL
- Designed a normalized schema with 3 tables:
- `stocks` - Stock metadata
- `stock_prices` - Historical OHLCV data
- `data_quality_logs` - Audit trail
- Created foreign key relationships and constraints

### Part 2: Data Extraction
- Integrated **Yahoo Finance API** using yfinance library
- Extracted 1 year of historical data for 4 major stocks (AAPL, GOOGL, TSLA, MSFT)
- Implemented error handling and logging
- Saved raw data to CSV format in `data/raw/`

### Part 3: Data Transformation (In Progress)
- Data cleaning and validation framework
- Duplicate detection and removal
- Missing value handling
- Price relationship validation
- Data quality metrics

## 🏗️ Architecture
stock-market-etl-pipeline/
├── data/
│ ├── raw/ # Raw data from API
│ └── processed/ # Cleaned, transformed data
├── src/
│ ├── extract.py # Data extraction script
│ ├── transform.py # Data transformation script
│ ├── load.py # Database loading (planned)
│ └── utils.py # Helper functions (planned)
├── config/
│ └── db_config.py # Database configuration
├── sql_queries/
│ └── analytics.sql # SQL queries (planned)
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore # Git ignore rules
## 🚀 How to Use

### Prerequisites
- Python 3.9+
- PostgreSQL 15+
- Git

### Installation

# Clone the repository
git clone https://github.com/munyigi/stock-market-etl-pipeline.git
cd stock-market-etl-pipeline
# Extract data from Yahoo Finance
python src/extract.py

# Transform and clean data
python src/transform.py

# Load into PostgreSQL (coming soon)
python src/load.py

📄 License

Save it and commit:

git add README.md
git commit -m "Add comprehensive project documentation."
git push
