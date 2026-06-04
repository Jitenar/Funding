# 🚀 Startup Funding Analysis Dashboard

An interactive Streamlit dashboard for analyzing startup funding trends in India. This project provides insights into funding patterns, startup ecosystems, investor activity, industry performance, and geographic distribution of investments.

---

## 📌 Project Overview

The Startup Funding Analysis Dashboard helps users explore and understand:

- Total funding trends over time
- Top funded startups
- Most active investors
- Industry-wise funding distribution
- City-wise startup ecosystem analysis
- Key business insights and recommendations

The dashboard is built using **Python**, **Streamlit**, **Pandas**, and **Plotly**.

---

## 📂 Project Structure

```text
startup-funding-analysis-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── startup_funding.csv
│
├── pages/
│   ├── 1_Data_Overview.py
│   ├── 2_Funding_Trends.py
│   ├── 3_Industry_Analysis.py
│   ├── 4_City_Analysis.py
│   ├── 5_Investor_Analysis.py
│   └── 6_Insights.py
│
├── utils/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── charts.py
│   └── helpers.py
│
├── assets/
│   ├── banner.png
│   └── startup_funding.jpg
│
└── outputs/
    ├── reports/
    └── visualizations/
```

---

## 📊 Features

### 📂 Data Overview
- Dataset dimensions
- Missing values analysis
- Data types inspection
- Statistical summary

### 📈 Funding Trends
- Year-wise funding trends
- Month-wise funding trends
- Funding growth analysis

### 🏭 Industry Analysis
- Top funded sectors
- Industry distribution
- Funding comparison across industries

### 🌍 City Analysis
- Top startup cities
- Regional funding distribution
- Startup ecosystem hotspots

### 💰 Investor Analysis
- Most active investors
- Investor participation trends
- Top funding rounds

### 💡 Insights
- Key findings
- Business recommendations
- Future opportunities

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- Scikit-learn

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/startup-funding-analysis-dashboard.git
cd startup-funding-analysis-dashboard
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📁 Dataset

The dataset contains information about startup funding in India, including:

- Startup Name
- Industry Vertical
- City Location
- Investors
- Funding Amount
- Funding Date
- Investment Type

---

## 📈 Sample Visualizations

- Funding Trend Line Charts
- Industry-wise Bar Charts
- Investor Analysis Charts
- City-wise Funding Maps
- Interactive Plotly Dashboards

---

## 🎯 Business Objectives

- Identify top-performing startup sectors
- Understand investment patterns
- Discover emerging startup hubs
- Analyze investor behavior
- Support data-driven decision making

---

## 🔮 Future Enhancements

- Funding prediction models
- Investor recommendation system
- Startup success prediction
- Interactive maps
- Real-time startup funding data integration

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
