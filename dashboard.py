import streamlit as st
import pandas as pd
from data_processor import get_key_data, get_kpi_data, get_ytd_data

# ============== CONFIGURATION ==============
st.set_page_config(
    page_title="Dashboard Key Activity IAS Group 2025",
    layout="wide"
)

st.title("Dashboard Key Activity IAS Group 2025")

# ============== DATA LOADING ============== 
# Load data using functions from data_processor.py
df_key = get_key_data()
df_kpi = get_kpi_data()
df_ytd = get_ytd_data()

# ============== DASHBOARD LAYOUT & VISUALIZATION ==============
st.write("## Data Key Activity")
st.dataframe(df_key)

st.write("## Data KPI")
st.dataframe(df_kpi)

st.write("## Data YTD")
st.dataframe(df_ytd)
