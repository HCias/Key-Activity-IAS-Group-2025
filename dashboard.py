import streamlit as st
import pandas as pd
from data_processor import get_key_data, get_kpi_data, get_ytd_data

# Import components
from components.sidebar import apply_sidebar_css, sidebar
from components.pages.dashboard import dashboard_page
from components.pages.detail import detail_page
from components.pages.capaian_deskriptif import capaian_deskriptif_page

# ============== CONFIGURATION ==============
st.set_page_config(
    page_title="IAS Group 2025",
    layout="wide"
)

# Apply sidebar CSS
apply_sidebar_css()

# ============== MAIN APP ==============
# Display title
st.title("Dashboard Human Capital Projects 2025")

# Load data using functions from data_processor.py
df_key = get_key_data()
df_kpi = get_kpi_data()
df_ytd = get_ytd_data()

# Display sidebar and get selected menu
selected = sidebar()

# Display content based on selected menu
if selected == "Dashboard":
    dashboard_page(df_key, df_kpi, df_ytd)
elif selected == "Detail":
    detail_page()
elif selected == "Capaian Deskriptif":
    capaian_deskriptif_page()
