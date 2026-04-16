# Santé et Territoires

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
git clone https://github.com/ouardianemmar-eng/Application-sante-.git
cd Application-sante-

# Créer l'environnement virtuel
pyenv virtualenv 3.11.8 Application-sante-
# L'activation sera automatique grâce au .python-version

# Installer les dépendances
pip install -r requirements.txt

# Vérifier que tout fonctionne
python -c "import pandas, geopandas; print('✅ Prêt !')"
```

### Setup avec venv standard

```bash
# Cloner le projet
git clone https://github.com/ouardianemmar-eng/Application-sante-.git
cd Application-sante-

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
Application-sante-/
├── data/                   # Données
│   ├── raw/                # Données brutes téléchargées
│       └── pathologie.csv
│
│   ├── processed/         # Données nettoyées et transformées
│       └── pathologie_clean.csv
│
├── processing/             # Jupyter notebooks d'exploration, d'analyse et du nettoyage des données
│   └── projet_sante.ipynb
│
├── Accueil.py                   # Code source Python de l'application
│
├── pages/               # Résultats (non versionnés)
│   └── Pathologies.py # Chargement, analyse et visualiation des données en Python
│
├── .python-version        # Version Python pour pyenv (auto-activation)
├── .gitignore            # Fichiers à ignorer par Git
├── README.md             # Ce fichier
└── requirements.txt      # Dépendances Python
```

---

## 📊 Données

### Sources de données utilisées


#### Données sur les pathologies
- **Données Caisse nationale de l'Assurance Maladie** : effectif de patients par pathologie, sexe, classe d'âge et territoire (département, région)

### Emplacement des données

- Les données brutes sont stockées dans `data/raw/`
- Les données transformées dans `data/processed/`

---

## 🚀 Usage

### Analyse et nettoyage des données

```bash
# Lancer Jupyter Notebook
jupyter notebook processing/projet_sante.ipynb
```

### Dashboard interactif 

```bash
# Lancer le dashboard Streamlit
streamlit run Accueil.py
```

### Visualisation

Les scripts de visualisation se trouvent dans le dossier `pages/Pathologies.py`

---

## 📚 Ressources

### Contexte du projet
- [Défi Open Data University - Santé et territoires](https://defis.data.gouv.fr/datasets/62b31f7b128643f46ea1f848)

### Documentation technique
- [GeoPandas Documentation](https://geopandas.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)