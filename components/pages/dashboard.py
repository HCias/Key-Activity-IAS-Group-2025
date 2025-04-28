import streamlit as st
import pandas as pd

def dashboard_page(df_key, df_kpi, df_ytd):
    """Display Dashboard page with all data tables"""
    
    # Assuming "ENTITAS" is the column name for entities in all dataframes
    # Get unique entities from all dataframes
    entities_key = df_key["ENTITAS"].unique().tolist() if "ENTITAS" in df_key.columns else []
    entities_kpi = df_kpi["ENTITAS"].unique().tolist() if "ENTITAS" in df_kpi.columns else []
    entities_ytd = df_ytd["ENTITAS"].unique().tolist() if "ENTITAS" in df_ytd.columns else []
    
    # Combine unique entities from all dataframes
    all_entities = sorted(list(set(entities_key + entities_kpi + entities_ytd)))
    
    # Add "All" option at the beginning
    all_entities = ["All"] + all_entities
    
    # Create filter section in the main dashboard area
    st.subheader("Filter Data")
    
    # Create dropdown for entity selection
    selected_entity = st.selectbox(
        "Pilih Entitas:",
        all_entities
    )
    
    # Add some space after the filter
    st.markdown("---")
    
    # Filter dataframes based on selected entity
    if selected_entity != "All":
        filtered_df_key = df_key[df_key["ENTITAS"] == selected_entity] if "ENTITAS" in df_key.columns else df_key
        filtered_df_kpi = df_kpi[df_kpi["ENTITAS"] == selected_entity] if "ENTITAS" in df_kpi.columns else df_kpi
        filtered_df_ytd = df_ytd[df_ytd["ENTITAS"] == selected_entity] if "ENTITAS" in df_ytd.columns else df_ytd
    else:
        filtered_df_key = df_key
        filtered_df_kpi = df_kpi
        filtered_df_ytd = df_ytd
    
    # Display filtered data
    st.write("## Data Key Activity")
    st.dataframe(filtered_df_key)
    
    st.write("## Data KPI")
    st.dataframe(filtered_df_kpi)
    
    st.write("## Data YTD")
    st.dataframe(filtered_df_ytd)
