import streamlit as st
import time

st.set_page_config(page_title="Laboratorio de Cumpleaños", page_icon="🎂")

st.title("👨‍🍳 Taller de Cumpleaños")
st.write("Antes de darte tu regalo, tienes que diseñar tu propio pastel.")

# 1. Widgets interactivos de diseño
st.subheader("Paso 1: Diseño")
col1, col2 = st.columns(2)

with col1:
    sabor = st.selectbox("Base del pastel:", ["Chocolate", "Tres Leches", "Red Velvet", "Zanahoria"])
    color_betun = st.color_picker("Color del betún:", "#FF69B4")

with col2:
    velas = st.slider("¿Cuántas velas le ponemos?", 1, 100, 25)
    chisporroteo = st.toggle("¿Agregar chispas explosivas?")

st.info(f"📝 **Tu pedido en tiempo real:** Pastel de {sabor} con betún color {color_betun} y {velas} velas. {'(Con chispas)' if chisporroteo else ''}")
st.divider()

# 2. Firma Digital interactiva
st.subheader("Paso 2: Firma de Autorización")
st.write("Para liberar el regalo, necesito tu firma digital de que aceptas los términos.")

firma = st.text_input("Ingresa tu nombre o apodo para firmar:")
# Casilla de verificación requerida
acepta_terminos = st.checkbox("Acepto que por ser mi cumpleaños no me va a importar la dieta, las calorías ni contar los macros de este pastel.")

# 3. Lógica de validación cruzada
# El botón solo existe si la persona ya escribió su nombre Y marcó la casilla
if firma and acepta_terminos:
    if st.button("Hornear pastel y abrir regalo", type="primary", use_container_width=True):
        
        # 4. Barra de progreso animada con Python puro
        barra_progreso = st.progress(0)
        texto_estado = st.empty()
        
        # Un ciclo 'for' que actualiza la pantalla 100 veces seguidas
        for porcentaje in range(100):
            time.sleep(0.02) # Pausa de milisegundos para que sea visible
            barra_progreso.progress(porcentaje + 1)
            texto_estado.text(f"Horneando a 220°C... {porcentaje + 1}%")
            
        texto_estado.text("¡Pastel listo para sacar del horno!")
        time.sleep(0.5)
        
        # 5. Revelación
        st.balloons()
        st.header(f"¡Feliz Cumpleaños, {firma}! 🎉")
        st.write("¡Aquí tienes tu sorpresa! Que pases un día increíble.")
        st.image("https://media.giphy.com/media/26FPpSuhgFd1hJHMQ/giphy.gif")