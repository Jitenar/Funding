import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Startup Funding Analysis Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 40px;
    font-weight: bold;
    color: #1E3A8A;
}
.sub-header {
    font-size: 20px;
    color: #6B7280;
}
.metric-card {
    background-color: #F3F4F6;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📊 Navigation")
st.sidebar.info(
    """
    Use the pages in the sidebar to explore:
    
    • Data Overview  
    • Funding Trends  
    • Industry Analysis  
    • City Analysis  
    • Investor Analysis  
    • Insights
    """
)

# Main Page
st.markdown(
    '<p class="main-header">🚀 Startup Funding Analysis Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-header">Analyze funding trends, top startups, industries, cities, and investors in India.</p>',
    unsafe_allow_html=True
)

# Banner Image
try:
    st.image("assets/banner.png", use_container_width=True)
except:
    st.warning("Banner image not found. Add banner.png inside assets folder.")

st.divider()

# Dashboard Overview
st.header("📌 Project Overview")

st.write("""
This dashboard provides an interactive analysis of startup funding in India.

### Features:
- 📂 Data Exploration
- 📈 Funding Trend Analysis
- 🏭 Industry-wise Analysis
- 🌍 City-wise Funding Analysis
- 💰 Investor Analysis
- 📊 Business Insights and Recommendations

Use the sidebar to navigate through different sections.
""")

st.divider()

# Quick Statistics Section
st.header("📊 Dashboard Sections")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 📂 Data Overview
    Explore dataset structure, missing values, and summary statistics.
    """)

with col2:
    st.success("""
    ### 📈 Funding Trends
    Analyze yearly and monthly funding trends.
    """)

with col3:
    st.warning("""
    ### 🏭 Industry Analysis
    Discover the most funded startup sectors.
    """)

col4, col5, col6 = st.columns(3)

with col4:
    st.info("""
    ### 🌍 City Analysis
    Identify India's leading startup hubs.
    """)

with col5:
    st.success("""
    ### 💰 Investor Analysis
    Explore top investors and funding networks.
    """)

with col6:
    st.warning("""
    ### 💡 Insights
    Key findings and recommendations.
    """)

st.divider()

st.markdown("""
### 🚀 Getting Started

1. Open the sidebar.
2. Select a page.
3. Explore interactive charts and insights.

Happy Analyzing! 📊
""")

# Footer
st.markdown("---")
st.caption("Startup Funding Analysis Dashboard | Developed using Streamlit")
