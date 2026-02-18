import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Mansour Diop",
    page_icon="📄",
    layout="wide"
)

# ====== HEADER ======
st.title("📄 Curriculum Vitae")
st.header("Mansour DIOP")

col1, col2 = st.columns([1,2])


with col2:
    st.write("📍 Dakar, Sénégal")
    st.write("📧 mansour.diop@email.com")
    st.write("🎯 Objectif : Ingénieur en géomatique / aéronautique")

st.divider()

# ====== PROFIL ======
st.subheader("🧑‍💼 Profil")
st.write("""
Technicien en géomatique passionné par l’aéronautique et les systèmes d’information géographique.
Expérience dans la cartographie aéronautique et l’analyse spatiale.
""")

# ====== COMPÉTENCES ======
st.subheader("🛠️ Compétences")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
* SIG (QGIS, ArcGIS)
* Power BI
* Cartographie VAC
* UMAP
    """)

with col2:
    st.markdown("""
* Python (bases)
* Streamlit
* Adobe Illustrator + MAPublisher
* Analyse spatiale
    """)

# ====== EXPÉRIENCE ======
st.subheader("💼 Expérience professionnelle")

st.markdown("""
*Cartographe Stagiaire — ASECNA*  
2024

* Réalisation de cartes VAC
* Analyse des données aéronautiques
* Mise à jour des bases cartographiques
""")

# ====== FORMATION ======
st.subheader("🎓 Formation")

st.markdown("""
**BTS Géomatique
