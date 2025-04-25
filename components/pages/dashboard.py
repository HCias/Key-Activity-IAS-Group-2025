import streamlit as st
import pandas as pd

def dashboard_page(df_key, df_kpi, df_ytd):
    """Display Dashboard page with all data tables"""
    st.write("## Data Key Activity")
    st.dataframe(df_key)
    
    st.write("## Data KPI")
    st.dataframe(df_kpi)
    
    st.write("## Data YTD")
    st.dataframe(df_ytd)
