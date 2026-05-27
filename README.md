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
