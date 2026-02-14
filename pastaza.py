import streamlit as st

st.set_page_config(page_title="Visualizador Pastaza Datos Abiertos", layout="wide", initial_sidebar_state="expanded")

st.title("🌿 Visualizador Fácil - Datos Abiertos Pastaza")
st.markdown("""
Esta app facilita la navegación y visualización del Portal de Gobierno Abierto del Gobierno Provincial de Pastaza.
Selecciona una sección en el menú lateral para verla en pantalla completa.
""")

st.sidebar.header("Navegación Rápida")

seccion = st.sidebar.selectbox(
    "Elige una sección",
    [
        "Inicio - Gobierno Abierto",
        "Obras Públicas",
        "Gestión Ambiental",
        "Desarrollo Sustentable",
        "Visor Geográfico (ArcGIS)",
        "Sistema de Información Local (SIL)",
        "Descargas - Plan de Acción"
    ]
)

# URLs directas
urls = {
    "Inicio - Gobierno Abierto": "https://datos.pastaza.gob.ec/",
    "Obras Públicas": "https://datos.pastaza.gob.ec/obras-publicas",
    "Gestión Ambiental": "https://datos.pastaza.gob.ec/gestion-ambiental",
    "Desarrollo Sustentable": "https://datos.pastaza.gob.ec/desarrollo-sustentable",
    "Visor Geográfico (ArcGIS)": "https://sil-pastaza-gadppz.hub.arcgis.com/",  # Hub principal ArcGIS de Pastaza
    "Sistema de Información Local (SIL)": "https://sil.pastaza.gob.ec/",
    "Descargas - Plan de Acción": "https://datos.pastaza.gob.ec/descargas/"
}

if seccion != "Descargas - Plan de Acción":
    st.components.v1.iframe(urls[seccion], height=800, scrolling=True)
else:
    st.markdown("### Descargas directas del Plan de Acción de Gobierno Abierto")
    st.markdown("- [Plan.pdf](https://datos.pastaza.gob.ec/descargas/Plan.pdf)")
    st.markdown("- [Matriz.pdf](https://datos.pastaza.gob.ec/descargas/Matriz.pdf)")
    st.markdown("- [Imagen.pdf](https://datos.pastaza.gob.ec/descargas/Imagen.pdf)")
    st.markdown("Más recursos en el portal principal.")

st.sidebar.markdown("---")
st.sidebar.markdown("App creada para el Gobierno Provincial de Pastaza 👏")
st.sidebar.markdown("Desarrollada con ❤️ por Grok - Feb 2026")