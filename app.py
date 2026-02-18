import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Mansour Diop",
    page_icon="📄",
    layout="wide"
)

# ====== BARRE LATÉRALE (SIDEBAR) ======
with st.sidebar:
    st.header("👤 Profil")
    st.write("""
    Technicien en géomatique passionné par l’aéronautique et les systèmes d’information géographique.
    Expérience dans la cartographie aéronautique et l’analyse spatiale.
    """)
    
    st.divider()
    
    st.header("🌐 Langues")
    st.markdown("""
    * *Français* : Maternel
    * *Anglais* : Technique / Professionnel
    * *Wolof* : Courant
    """)
    
    st.divider()
    
    # Optionnel : Bouton de contact ou lien LinkedIn
    st.info("💡 Disponible pour de nouvelles opportunités en Géomatique.")

# ====== CONTENU PRINCIPAL ======
# Header
st.title("📄 Curriculum Vitae")
st.header("Mansour DIOP")

# Informations de contact sous le nom
col_info1, col_info2 = st.columns(2)
with col_info1:
    st.markdown("📍 *Localisation :* Dakar, Sénégal")
    st.markdown("📧 *Email :* mansour.diop@email.com")
with col_info2:
    st.markdown("🎯 *Objectif :* Ingénieur en géomatique / aéronautique")

st.divider()

# ====== COMPÉTENCES ======
st.subheader("🛠️ Compétences")

col_skill1, col_skill2 = st.columns(2)

with col_skill1:
    st.markdown("""
*Expertise SIG & Cartographie*
* SIG (QGIS, ArcGIS)
* Cartographie VAC (Visual Approach Chart)
* Adobe Illustrator + MAPublisher
* UMAP
    """)

with col_skill2:
    st.markdown("""
*Data & Développement*
* Python (Data Analysis)
* Streamlit (Dashboards)
* Power BI
* Analyse spatiale
    """)

st.divider()

# ====== EXPÉRIENCE ======
st.subheader("💼 Expérience professionnelle")

st.markdown("""
*Cartographe Stagiaire — ASECNA* Dakar, Sénégal | 2024

* Réalisation de cartes VAC (Visual Approach Chart).
* Analyse des données aéronautiques et intégration SIG.
* Mise à jour des bases de données cartographiques.
""")

st.divider()

# ====== FORMATION ======
st.subheader("🎓 Formation")

st.markdown("""
*BTS Géomatique* CEDT G15/Institut | Année

* Apprentissage des techniques de levés, de la cartographie numérique et de la gestion de bases de données spatiales.
""")
