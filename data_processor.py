import pandas as pd
import streamlit as st

# Data source
SHEET_ID_IAS = '1968Ztq01lDeAICTIq_t_QWWqVGFlNtYB'

def load_data_from_sheet(sheet_id, sheet_name):
    """
    Load data from a specific sheet in a Google Spreadsheet.
    
    Args:
        sheet_id (str): The ID of the Google Spreadsheet
        sheet_name (str): The name of the sheet to load
        
    Returns:
        pandas.DataFrame: The loaded data or None if an error occurred
    """
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data from sheet '{sheet_name}': {e}")
        return None

def get_key_data():
    """Load data from the db_key sheet"""
    return load_data_from_sheet(SHEET_ID_IAS, "db_key")

def get_kpi_data():
    """Load and process data from the db_kpi sheet"""
    df_kpi_original = load_data_from_sheet(SHEET_ID_IAS, "db_kpi")
    
    # Filter df_kpi to include columns only up to "SATUAN"
    if df_kpi_original is not None:
        # Get the column list
        columns = df_kpi_original.columns.tolist()
        # Find the index of "SATUAN" column
        try:
            satuan_index = columns.index("SATUAN")
            # Select columns up to and including "SATUAN"
            df_kpi = df_kpi_original.iloc[:, :satuan_index+1]
        except ValueError:
            # If "SATUAN" column doesn't exist, use the original dataframe
            st.warning("Column 'SATUAN' not found in KPI data. Using all available columns.")
            df_kpi = df_kpi_original
            
    return df_kpi

def get_ytd_data():
    """Load and process data from the db_ytd sheet"""
    df_ytd_original = load_data_from_sheet(SHEET_ID_IAS, "db_ytd")
    
    # Filter df_ytd to include columns only up to "SATUAN"
    if df_ytd_original is not None:
        # Get the column list
        columns = df_ytd_original.columns.tolist()
        # Find the index of "SATUAN" column
        try:
            satuan_index = columns.index("SATUAN")
            # Select columns up to and including "SATUAN"
            df_ytd = df_ytd_original.iloc[:, :satuan_index+1]
        except ValueError:
            # If "SATUAN" column doesn't exist, use the original dataframe
            st.warning("Column 'SATUAN' not found in YTD data. Using all available columns.")
            df_ytd = df_ytd_original
            
    return df_ytd
