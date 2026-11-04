import streamlit as st

st.set_page_config(page_title="Sorpresa", page_icon="🎁")

st.title("🎁 ¡Alguien te mandó un regalo!")

if st.button("Tocar para abrir", type="primary"):
    st.balloons()
    st.header("¡Feliz Cumpleaños! 🎂🥳")
    st.write("Que pases un día increíble. ¡Un abrazo fuerte!")
    
    # Puedes cambiar este link por cualquier GIF o imagen de internet
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZkeWF4NTd5ZnRwa3I0Zzl3ZDYzbDh1aWViMnU4cGhwa2Uxcml0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/66dLOWrLqrgxWHSeVR/giphy.gif")