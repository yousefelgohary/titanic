<div align="center">

# 🚢 Titanic EDA Dashboard

### An Interactive Exploratory Data Analysis Web Application

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_to_Explore-00C851?style=for-the-badge)](https://yousefelgohary-titanic-app-irccf8.streamlit.app/)
[![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Plotly](https://img.shields.io/badge/Visualizations-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

> Built as part of the **NTI — Machine Learning for Data Science (Creativa)** training program.

</div>

---

## 🌐 Try the Live Dashboard

> **No setup required.** Click the button below and start exploring the Titanic data instantly.

**👉 [https://yousefelgohary-titanic-app-irccf8.streamlit.app/](https://yousefelgohary-titanic-app-irccf8.streamlit.app/)**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://yousefelgohary-titanic-app-irccf8.streamlit.app/)

---

## 📊 About the Dataset

The **RMS Titanic Passenger Dataset** is one of the most iconic datasets in data science. It contains records of **891 passengers** from the tragic 1912 voyage, with rich demographic and ticket information that makes it ideal for survival analysis and pattern discovery.

### Feature Reference

| Feature | Type | Description |
|---|---|---|
| `PassengerId` | Integer | Unique passenger identifier |
| `Survived` | Binary | Survival outcome — **0 = Did Not Survive**, **1 = Survived** |
| `Pclass` | Categorical | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) — proxy for socioeconomic status |
| `Name` | String | Full passenger name |
| `Sex` | Categorical | Passenger gender (male / female) |
| `Age` | Float | Passenger age in years |
| `SibSp` | Integer | Number of siblings/spouses aboard |
| `Parch` | Integer | Number of parents/children aboard |
| `Ticket` | String | Ticket number |
| `Fare` | Float | Ticket fare paid in British pounds (£) |
| `Cabin` | String | Cabin number (sparse — many missing values) |
| `Embarked` | Categorical | Port of embarkation — **C** = Cherbourg, **Q** = Queenstown, **S** = Southampton |

### Key Dataset Statistics

| Metric | Value |
|---|---|
| 🧑‍🤝‍🧑 Total Passengers | 891 |
| 💀 Overall Survival Rate | ~38.4% |
| 🎫 Passenger Classes | 3 (1st, 2nd, 3rd) |
| 📅 Age Range | 0.42 — 80 years |
| 💰 Fare Range | £0 — £512.33 |
| 🧍 Gender Split | ~65% male, ~35% female |

---

## 🖥️ Dashboard Features

The dashboard transforms raw CSV data into a fully interactive story — every filter, chart, and metric responds in real time.

### 🎛️ Dynamic Sidebar Filters

Apply real-time filters that instantly update every chart and KPI on the page:

| Filter | Type | Options |
|---|---|---|
| **Sex** | Multi-select | male, female |
| **Passenger Class** | Multi-select | 1st, 2nd, 3rd |
| **Age Range** | Range Slider | 0.42 – 80 years |

### 📈 Key Performance Indicators (KPIs)

Three headline metrics update dynamically based on your active filters:

| KPI | Description |
|---|---|
| 🧳 **Total Passengers** | Count of all passengers matching current filters |
| ❤️ **Survival Rate** | Percentage of filtered passengers who survived |
| 💰 **Average Fare** | Mean ticket price (in £) for the filtered group |

### 📉 Interactive Visualizations

All charts are built with **Plotly** — fully interactive, zoomable, and hoverable with rich tooltips.

| Chart | Chart Type | Key Insight |
|---|---|---|
| **Survival by Passenger Class** | Grouped Bar Chart | Compares survivors vs. non-survivors across all three classes side-by-side — 1st class had drastically better odds |
| **Age Distribution by Survival** | Histogram + Marginal Box Plot | Reveals age demographics and how survival probability varied with age — children had higher survival rates |
| **Fare vs. Survival** | Box Plot (with all data points) | Exposes the strong correlation between higher ticket prices and survival — those who paid more fared better |

### 🗂️ Raw Data Explorer

A collapsible table at the bottom of the dashboard lets you inspect every row in the filtered dataset. Great for cross-referencing patterns seen in the charts against actual records.

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Web Framework** | [Streamlit](https://streamlit.io) | App UI, layout, widgets, caching |
| **Data Manipulation** | [Pandas](https://pandas.pydata.org) | Filtering, aggregation, groupby |
| **Numerical Computing** | [NumPy](https://numpy.org) | Array operations and statistics |
| **Visualizations** | [Plotly Express](https://plotly.com/python/plotly-express/) | All interactive charts |
| **Language** | Python 3.10+ | Core language |
| **Deployment** | Streamlit Community Cloud | Free, one-click cloud hosting |

---

## 🚀 Run Locally

Want to run the dashboard on your own machine? Follow these steps:

**Prerequisites:** Python 3.10+, Git

```bash
# 1. Clone the repository
git clone https://github.com/yousefelgohary/titanic.git
cd titanic

# 2. Create and activate a virtual environment
python -m venv .venv

# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the dashboard
streamlit run app.py
```

The app will open automatically at `http://localhost:8501` 🎉

---

## 📁 Repository Structure

```
titanic/
├── app.py              # Main Streamlit dashboard application
├── titanic.csv         # Titanic passenger dataset (891 records)
├── Recap.ipynb         # Jupyter notebook with EDA recap & analysis
├── requirements.txt    # Python dependencies (streamlit, pandas, plotly, numpy)
├── .gitignore          # Git ignore configuration
└── README.md           # This file
```

---

## 🎓 About the Program

This project was developed during **Session 1** of the **NTI Machine Learning for Data Science** course (Creativa track) at the **National Telecommunication Institute (NTI), Egypt**.

The course covers the full data science pipeline — from raw data exploration to production deployment:

- 🔍 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning Models & Evaluation
- 📊 Data Visualization & Storytelling
- 🚀 Production-Ready Deployment

---

<div align="center">

Made with ❤️ by **Yousef Elgohary**

[![GitHub](https://img.shields.io/badge/GitHub-yousefelgohary-181717?style=flat-square&logo=github)](https://github.com/yousefelgohary)

</div>
