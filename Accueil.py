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



 - Collecte des données (C1)
   - Mettre en place un flux automatisé pour récupérer les données depuis différentes sources  
     - Fichiers
   - Gérer les erreurs et assurer la fiabilité de la collecte

 - Préparation des données (C2 & C3)
   - Nettoyer les données:
     - Valeurs manquantes
     - Formats incorrects
     - Appliquer des règles d’agrégation pour combiner les données
     - Transformer les données pour les rendre exploitables

 - Stockage des données (C4)
   - Créer une base de données
   - Définir un schéma (MCD / MLD)
   - Choisir la technologie et l'outillage adaptée
   - Mettre en place les tables et la structure

 - Mise à disposition des données (C5)
   - Exposer les données via une API
   - Sécuriser l’accès à l'API
   - Vérifier que les données sont accessibles et utilisables

"""
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("Projet réalisé dans le cadre de la certification RNCP3727BC01")