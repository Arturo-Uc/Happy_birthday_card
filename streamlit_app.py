import streamlit as st

st.set_page_config(page_title="Sorpresa", page_icon="🎁")

st.title("🎁 ¡Alguien te mandó un regalo!")

col1, col2, col3 = st.columns(3)

with col2:
    regalo_abierto = st.button("Tocar para abrir", type="primary", use_container_width=True)

if regalo_abierto:
    st.balloons()
    st.markdown("<h2 style='text-align: center;'>¡Feliz Cumpleaños! 🎂🥳</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Que pases un día increíble. ¡Un abrazo fuerte!</p>", unsafe_allow_html=True)
    img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
    with img_col2:
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZkeWF4NTd5ZnRwa3I0Zzl3ZDYzbDh1aWViMnU4cGhwa2Uxcml0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/66dLOWrLqrgxWHSeVR/giphy.gif", use_container_width=True)