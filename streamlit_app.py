import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuración de la pestaña
st.set_page_config(page_title="Sorpresa", page_icon="🎁")

# Función para cargar la animación desde internet
def cargar_lottie(url):
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        return None
    return respuesta.json()

# Enlace a un archivo JSON de animación (puedes cambiarlo después)
url_animacion = "https://lottie.host/4b9a8ad7-204f-4f37-82e9-763145543601/x5kQU0nePB.json"
animacion_json = cargar_lottie(url_animacion)

st.title("🎁 Tienes un paquete esperando")

# El botón detona la sorpresa
if st.button("Abrir regalo", type="primary", use_container_width=True):
    st.balloons()
    st.markdown("<h2 style='text-align: center;'>¡Feliz Cumpleaños! 🎉</h2>", unsafe_allow_html=True)
    
    # Columnas para centrar la animación perfectamente
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st_lottie(animacion_json, height=300, key="animacion_cumple")
        
    st.markdown("<p style='text-align: center;'>¡Espero que la pases increíble hoy!</p>", unsafe_allow_html=True)