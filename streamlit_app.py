import streamlit as st

st.set_page_config(page_title="Sorpresa", page_icon="🎁")

# 1. Creamos la "memoria" de la aplicación
# Esto recuerda si el usuario ya abrió el regalo o no
if 'regalo_abierto' not in st.session_state:
    st.session_state.regalo_abierto = False

# 2. Creamos "espacios vacíos" que podemos limpiar más adelante
espacio_animacion = st.empty()
espacio_boton = st.empty()

# 3. Si el regalo NO se ha abierto, mostramos el empaque y el botón
if not st.session_state.regalo_abierto:
    
    with espacio_animacion.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # GIF de un empaque de regalo animado/vibrando
            st.image("https://media.giphy.com/media/3o6Zt6qJcO4F4B3Cww/giphy.gif", use_container_width=True)
            
    with espacio_boton.container():
        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b2:
            if st.button("Abrir sorpresa", type="primary", use_container_width=True):
                # Cambiamos la memoria a "abierto" y recargamos la página al instante
                st.session_state.regalo_abierto = True
                st.rerun()

# 4. Si el regalo YA se abrió, ejecutamos la sorpresa
if st.session_state.regalo_abierto:
    # Vaciamos los contenedores anteriores para que el botón desaparezca
    espacio_animacion.empty()
    espacio_boton.empty()
    
    st.balloons()
    
    st.markdown("<h2 style='text-align: center;'>¡Feliz Cumpleaños! 🎂🥳</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Que pases un día increíble. ¡Un abrazo fuerte!</p>", unsafe_allow_html=True)
    
    img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
    with img_col2:
        st.image("https://media.giphy.com/media/26FPpSuhgFd1hJHMQ/giphy.gif", use_container_width=True)