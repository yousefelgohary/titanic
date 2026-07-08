# NTI: Machine Learning for Data Analysis - Titanic Dashboard

This repository contains an interactive exploratory data analysis (EDA) dashboard for the **RMS Titanic Passenger Dataset**, built as part of the Machine Learning training program at the National Telecommunication Institute (NTI).

## Course Overview

The program bridges the gap between raw data analysis and intelligent decision-making by covering full data pipelines, machine learning models, thorough evaluations, and production-ready deployments.

## Project Objectives

The core focus of this project is to build a professional, interactive web application using **Streamlit** to visualize and analyze the Titanic dataset. 

Key features include:
- **Interactive Filtering:** Filter passenger data dynamically by Sex, Passenger Class, and Age range.
- **Key Performance Indicators (KPIs):** High-level metrics such as Total Passengers, Overall Survival Rate, and Average Fare.
- **Rich Visualizations:** 
  - Survival distributions across passenger classes.
  - Age demographics and survival correlation.
  - Fare analysis via box plots.
- **Raw Data Exploration:** Direct access to the raw underlying dataset for verification and granular inspection.

## Installation & Setup

To reproduce the analysis locally and run the dashboard, ensure you have Python 3.10+ installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yousefelgohary/titanic.git
   cd titanic
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Dashboard:**
   ```bash
   streamlit run app.py
   ```

## Environment & Tools

- **App Framework:** Streamlit
- **Data Manipulation:** Pandas, NumPy
- **Visualizations:** Plotly
- **Core Language:** Python 3.10+

## Repository Structure

```text
titanic/
├── .venv/                 # Virtual environment (ignored in git)
├── .gitignore             # Git ignore configuration
├── requirements.txt       # Project dependencies
├── README.md              # Comprehensive technical overview
├── app.py                 # Main Streamlit dashboard application
└── titanic.csv            # Core operational passenger records dataset
```
