import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe

st.title("Dashboard Key Activity IAS Group 2025")

# IAS : https://docs.google.com/spreadsheets/d/1968Ztq01lDeAICTIq_t_QWWqVGFlNtYB/edit?usp=sharing&ouid=112510443691221764804&rtpof=true&sd=true

sheet_id_ias = '1968Ztq01lDeAICTIq_t_QWWqVGFlNtYB'

# Metode alternatif menggunakan pandas dengan parameter sheet_name
try:
    # Mencoba mengakses sheet db_key dengan parameter dalam URL
    df_ias = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id_ias}/gviz/tq?tqx=out:csv&sheet=db_key")
    
    # Menampilkan dataframe dengan st.dataframe
    st.header("Data IAS Group - Sheet db_key")
    st.dataframe(df_ias)
    
    # Menampilkan statistik dasar
    st.header("Statistik Data")
    st.write(df_ias.describe())
    
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca sheet db_key: {e}")
    
    # Coba mengakses sheet default (jika db_key tidak ada)
    try:
        df_ias = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id_ias}/export?format=csv")
        st.success("Berhasil membaca sheet default")
        st.header("Data IAS Group - Sheet Default")
        st.dataframe(df_ias)
    except:
        st.error("Tidak dapat membaca sheet default juga.")