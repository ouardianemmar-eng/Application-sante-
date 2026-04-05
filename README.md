# Santé et Territoires
beige
Profil et analyse épidémiologique du territoire de la Haute-Garonne en 2023.

---

## 📋 Description

Ce projet vise à réaliser un profil et analyse épidémiologique du territoire de la Haute-Garonne en 2023 pour aider les collectivités locales dans la mise en place d'actions de prévention.

### Problématique

Comment aider les acteurs locaux à réaliser un diagnostic de santé publique sur leur territoire

### Objectifs

- Profil épidémiologique de la Haute-Garonne (2023)
- Dynamique pluriannuelle des 5 pathologies majeures
- Zoom sur les maladies respiratoire chroniques

---

## 🛠️ Installation

### Prérequis

- Python 3.11.8
- pyenv (recommandé) ou venv

### Setup avec pyenv (recommandé)

```bash
# Cloner le projet
git clone https://github.com/jjchabutDataCRM/sante-territoires.git
cd sante-territoires

# Créer l'environnement virtuel
pyenv virtualenv 3.11.8 sante-territoires
# L'activation sera automatique grâce au .python-version

# Installer les dépendances
pip install -r requirements.txt

# Vérifier que tout fonctionne
python -c "import pandas, geopandas; print('✅ Prêt !')"
```

### Setup avec venv standard

```bash
# Cloner le projet
git clone https://github.com/jjchabutDataCRM/sante-territoires.git
cd sante-territoires

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
source venv/bin/activate  # Mac/Linux
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
```

---

## 📁 Structure du projet

```
sante-territoires/
├── data/                   # Données (non versionnées)
│   ├── raw/               # Données brutes téléchargées
│   ├── processed/         # Données nettoyées et transformées
│
├── processing/             # Jupyter notebooks d'exploration, d'analyse et du nettoyage des données
│   └── projet_sante.ipynb
│
├── app.py                   # Code source Python de l'application
│
├── pages/               # Résultats (non versionnés)
│   └── 🤒 Pathologies.py # Chargement, analyse et visualiation des données en Python
│
├── .python-version        # Version Python pour pyenv (auto-activation)
├── .gitignore            # Fichiers à ignorer par Git
├── README.md             # Ce fichier
└── requirements.txt      # Dépendances Python
```

---

## 📊 Données

### Sources de données utilisées

#### Données géographiques
- **Contours IRIS** : Découpage infra-communal pour l'analyse géographique
- **Quartiers prioritaires (QPV)** : Zones d'intervention prioritaire

#### Données de santé
- **APL (Accessibilité Potentielle Localisée)** : Mesure de l'accessibilité aux médecins généralistes
- **Offre de soins** : Nombre et répartition des professionnels de santé

#### Données socio-démographiques
- **Données INSEE** : Population, âge, composition des ménages
- **Filosofi** : Revenus, taux de pauvreté
- **Recensement** : Catégories socio-professionnelles, niveau d'éducation

### Emplacement des données

- Les données brutes sont stockées dans `data/raw/`
- Les données transformées dans `data/processed/`

---

## 🚀 Usage

### Analyse et nettoyage des données

```bash
# Lancer Jupyter Notebook
jupyter notebook notebooks/projet_sante.ipynb
```

### Dashboard interactif 

```bash
# Lancer le dashboard Streamlit
streamlit run app.py
```

### Analyses

Les scripts d'analyse se trouvent dans le dossier `pages/🤒 Pathologies.py`

---

## 🎯 Livrables prévus

- [ ] Tableau de bord interactif sur l'offre de soin et de prévention
- [ ] Cartographie des populations vulnérables
- [ ] Analyse des déserts médicaux
- [ ] Score de vulnérabilité composite
- [ ] Rapport final avec recommandations


## 📚 Ressources

### Contexte du projet
- [Défi Open Data University - Santé et territoires](https://defis.data.gouv.fr/defis/)
- [Fondation Roche - Observatoire de l'accès au numérique en santé](https://www.fondationroche.org/)

### Documentation technique
- [GeoPandas Documentation](https://geopandas.org/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Données ouvertes
- [data.gouv.fr - Santé](https://www.data.gouv.fr/fr/pages/donnees-sante/)
- [INSEE - Données démographiques](https://www.insee.fr/)

---

## 📝 Licence

Ce projet est réalisé dans le cadre d'un projet pédagogique.

