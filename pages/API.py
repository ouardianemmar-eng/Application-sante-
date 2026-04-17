
import streamlit as st
import requests
import pandas as pd


headers = {"X-API-Key": "motdepasse"}
donnees = requests.get("http://127.0.0.1:8000", headers=headers).json()

st.title("Top 5 pathologies – Haute-Garonne")
st.dataframe(pd.DataFrame(donnees))
    