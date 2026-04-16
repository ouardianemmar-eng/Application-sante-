
import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns
import streamlit as st


data = pd.read_csv('data/processed/pathologie_clean.csv',sep=",")
data.head()
#---------------------- Création des onglets pour l'application Streamlit ----------------------
tab1, tab2, tab3 = st.tabs([
    " Profil épidémiologique du departement du Haute-Garonne (2023)",
    "Dynamique pluriannuelle des 5 pathologies majeures",
    "Zoom sur les maladies respiratoire chroniques"
])


###################vsiualisation des pathologies existantes et leur prevalence dans le departement Haute-Garonne (31)###########################


# Filtrer pour le département 31 et l'année 2023
df_31_2023 = data[(data['dept'] == 31)& 
                (data['annee'] == 2023)]
# Trier par prévalence pour un meilleur rendu visuel
df_31_2023 = df_31_2023.sort_values(by='prev_calculee', ascending=False)


with tab1:
    st.subheader("Fréquence des pathologies en Haute-Garonne (2023) ")

    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.barplot(data=df_31_2023,
            x='prev_calculee', 
            y='patho_niv1', 
           palette='viridis')
    
    plt.title('Prévalence des pathologies dans le département 31 (2023)')
    plt.xlabel('Prévalence (en %)')
    plt.ylabel('Pathologies')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()


    st.pyplot(fig)
    st.write("""

-->>>>Conclusion:

- Le diabète et les maladies respiratoires -> Un enjeu majeur de santé publique dans le département Haute-Garonne 
- Les maladies cardioneurovasculaires, les cancers, les maladies neurologiques et les maladies psychiatriques -> occupent une position intermédiaire              

""")

######################################Etude de l'evolution des 5 patologies frequentes dans le departement Haute-Garonne (31)##################

#Top 5 des pathologies par prévalence moyenne en 2023
top_5_names = (data[data['annee'] == 2023]
               .groupby('patho_niv1')['prev_calculee']
               .mean()
               .sort_values(ascending=False)
               .head(5).index)
df_31=data[(data['dept'] == 31)]
df_76= data


df_top5_31 = df_31[df_31['patho_niv1'].isin(top_5_names)]
df_top5_76 = df_76[df_76['patho_niv1'].isin(top_5_names)]

###Visualisation d'evolution sur le departement de Haute-Garonne (31) et la region d'Occitanie (76) des 5 pathologies les plus frequentes en 2023

with tab2:
    
### Dans le departement de Haute-Garonne (31)
    
    st.subheader("Évolution des 5 affections prépondérantes : 2015-2023")
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.lineplot(
        data=df_top5_31,
        x="annee",
        y="prev_calculee",
        hue="patho_niv1",
        errorbar=None,
        marker="o",
        ax=ax
    )
    ax.set_title("Évolution des 5 affections prépondérantes dans le departement (Haut Garonne)")
    ax.set_xlabel("Année")
    ax.set_ylabel("Prévalence calculée")
    ax.set_ylim(0, 10)
    ax.legend(title='Pathologies', bbox_to_anchor=(1.05, 1), loc='lower center')
    ax.grid(True, alpha=0.9)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)

### Dans la region d'Occitanie (76)

    st.set_page_config(layout="wide")
    #st.subheader("Évolution des 5 affections prépondérantes dans la region occitanie : 2015-2023")
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.lineplot(
        data=df_top5_76,
        x="annee",
        y="prev_calculee",
        hue="patho_niv1",
        errorbar=None,
        marker="o",
        ax=ax
    )
    ax.set_title("Etude de l'evolution des 5 pathologies prépondérantes dans la région d' Occitanie")
    ax.set_xlabel("Année")
    ax.set_ylabel("Prévalence calculée")
    ax.set_ylim(0, 10)
    #ax.legend(title="Pathologie")
    ax.legend(title='Pathologies', bbox_to_anchor=(1.05, 1), loc='lower center')
    ax.grid(True, alpha=0.9)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    
    st.write("""
-->>>>Conclusion:

-Une prédominance constante du diabète et des maladies respiratoires chroniques entre les deux territoires

    """)
    

###################visualiser les tranches d'ages des personnes plus vulnerables face aux maladies respiratoires sur les données du departement Haute-Garonne (31) pour l'année 2023 ###########
# 1.Filtrer sur la pathologie cible : "Maladies respiratoires chroniques (hors mucoviscidose)" et exclure categorie touts ages pour ne pas fausser la comparaison entre les tranches d'âge spécifiques

patho_cible = "Maladies respiratoires chroniques (hors mucoviscidose)"
df_respi_2023 = df_31_2023[(df_31_2023['patho_niv1'] == patho_cible)&(df_31_2023['libelle_classe_age'] != 'tous âges')]
path_cibe_H_prevalence="Maladies respiratoires chroniques (hors mucoviscidose)"

# 3. Trier les données par prévalence décroissante
df_respi_2023 = df_respi_2023.sort_values(by='prev_calculee', ascending=False)


with tab3:
    st.subheader("Sensibilité aux pathologies respiratoires : les tranches d'âge les plus exposées")

    sns.set_style("whitegrid")

    fig, ax =plt.subplots(figsize=(12, 8))

    sns.barplot(
        data=df_respi_2023,
        x='prev_calculee',
        y='libelle_classe_age',
        palette='Blues_r',
        ax=ax
    )
    
    # Ajout des étiquettes de données
    for i, val in enumerate(df_respi_2023['prev_calculee']):
        ax.text(val, i, f' {val:.2f}%', va='center', fontsize=10)

    ax.set_title(f'Prévalence par âge : {patho_cible}\n(Haute-Garonne - 2023)', fontsize=14)
    ax.set_xlabel('Prévalence (%)')
    ax.set_ylabel("Tranche d'âge")

    plt.tight_layout()

    st.pyplot(fig)
    st.write("""

-->>>>Conclusion:

-Les jeunes enfants (0-4 ans) présentent le taux le plus élevé (entre 13,6 %).
-Les personnes très âgées ont aussi des niveaux très élevés (entre 9 et 13 %).
    
-Une forte vulnérabilité aux extrêmes d'âge -> Cela traduit une fragilité accrue du système respiratoire de ces deux populations.
                                            
    """)
    
    
    
