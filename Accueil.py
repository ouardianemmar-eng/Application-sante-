import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# CONFIGURATION DE LA PAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Projet Data Analyst – Homepage",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("Certification RNCP3727BC01")
st.subheader("Analyse, automatisation et visualisation de données")

st.markdown(
    """
Bienvenue sur le tableau de bord interactif réalisé dans le cadre du projet de Data analyst.  
Ce site présente l’ensemble des analyses, visualisations autour d'un jeu de données sélectionné.

---
"""
)

# ---------------------------------------------------------
# OBJECTIFS DU PROJET
# ---------------------------------------------------------
st.header("🎯 Objectifs du projet")

st.markdown(
    """
    
    📊Pipeline de gestion des données
    
    - 1. Collecte des données
    - 2. Préparation des données
    - 3. Stockage des données
    - 4. Analyse et visualisation des données
    - 5. Mise à disposition via une API sécurisée
    - 6. Déploiement de l’application Streamlit

"""
)

# ---------------------------------------------------------
# STRUCTURE DU TABLEAU DE BORD
# ---------------------------------------------------------
st.header("🗂️ Navigation dans l'application")

st.markdown(
    """


- **🏠 Accueil** : Présentation générale du projet.   
- **🤒 Pathologies** : Données relatives aux pathologies sur le territoire en 2015-2023



"""
)

# ---------------------------------------------------------
# METHODOLOGIE
# ---------------------------------------------------------
st.header("🧭 Méthodologie")

st.markdown(
    """
La démarche suivie repose sur les étapes classiques d’un projet data :

1. **Compréhension du besoin métier**  
2. **Collecte et exploration des données**  
3. **Nettoyage et préparation (ETL)**  
4. **Analyses statistiques et visualisations**  
5. **Modélisation (si applicable)**  
6. **Synthèse et recommandations**  
7. **Déploiement Streamlit**


"""
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("Projet réalisé dans le cadre de la certification Data Analyst – Streamlit App")