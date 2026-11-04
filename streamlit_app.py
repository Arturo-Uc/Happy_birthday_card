import streamlit as st
import time

# Configuramos la pestaña para que parezca un sistema de seguridad
st.set_page_config(page_title="Acceso Restringido", page_icon="🔒")

# Memoria para saber si ya lograron hackear el regalo
if 'desbloqueado' not in st.session_state:
    st.session_state.desbloqueado = False

# PANTALLA 1: SISTEMA BLOQUEADO
if not st.session_state.desbloqueado:
    st.error("⚠️ PAQUETE ENCRIPTADO. Se requiere autenticación para acceder al regalo.")
    
    st.write("Responde la pregunta de seguridad para desactivar el candado:")
    # Convertimos la respuesta a minúsculas para que no importe si usan mayúsculas
    respuesta = st.text_input("¿Cuál es el peor oso que pasamos juntos en la universidad?").lower()
    
    if st.button("Intentar desencriptar", type="primary"):
        # Validamos si la respuesta incluye la palabra clave
        if "karaoke" in respuesta:
            # Creamos un efecto visual de "carga" falso de 2 segundos
            with st.spinner("Desencriptando archivos del sistema..."):
                time.sleep(2.5) 
            
            # Cambiamos el estado y recargamos
            st.session_state.desbloqueado = True
            st.rerun()
        elif respuesta != "":
            st.warning("Contraseña incorrecta. El intento ha sido registrado y bloqueado.")

# PANTALLA 2: REGALO LIBERADO
if st.session_state.desbloqueado:
    st.balloons()
    st.success("🔓 Protocolo de seguridad desactivado. Acceso concedido.")
    
    st.markdown("<h1 style='text-align: center;'>¡Feliz Cumpleaños! 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>¡Sobreviviste a mi sistema de seguridad! Que la pases increíble.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
         st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGg5M3lva2F1NWN4dDN0NXhrcGE1endwbDk2b29hYTFqcDlqaHozeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/66dLOWrLqrgxWHSeVR/giphy.gif", use_container_width=True)