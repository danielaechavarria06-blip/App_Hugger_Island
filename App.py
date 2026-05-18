# app.py
# AbraVenturas ✨
# App prototipo para generación de historias personalizadas y momentos de conexión
# Streamlit + OpenAI

# ---------------- LIBRERÍAS ----------------
import streamlit as st
from openai import OpenAI
from PIL import Image
import requests

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="AbraVenturas",
    page_icon="🌈",
    layout="wide"
)

# ---------------- ESTILOS ----------------
st.markdown("""
<style>

.main {
    background-color: #FFF9F2;
}

h1 {
    color: #FF8A00;
    font-size: 52px !important;
}

h2, h3 {
    color: #5C3D99;
}

.stButton button {
    background-color: #FFB703;
    color: black;
    border-radius: 15px;
    padding: 10px 20px;
    border: none;
    font-weight: bold;
}

.stTextInput > div > div > input {
    border-radius: 12px;
}

.stSelectbox > div > div {
    border-radius: 12px;
}

.story-box {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    border: 3px solid #FFD166;
    margin-top: 20px;
}

.activity-box {
    background-color: #D9F8FF;
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- API KEY ----------------
# Reemplazar con tu key
client = OpenAI(api_key="TU_API_KEY")

# ---------------- HEADER ----------------

col1, col2 = st.columns([1,2])

with col1:
    st.image("images/abrazador.png", width=250)  # reemplaza esta imagen

with col2:
    st.title("🌈 AbraVenturas")
    st.subheader("Historias personalizadas que abrazan la imaginación")

# ---------------- FORMULARIO ----------------

st.markdown("---")

st.header("✨ Cuéntanos sobre tu pequeño lector")

nombre = st.text_input("👦 Nombre del niño")

edad = st.selectbox(
    "🎂 Edad",
    ["3 años", "4 años", "5 años", "6 años", "7 años", "8 años"]
)

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    [
        "Dinosaurios",
        "Espacio",
        "Animales",
        "Princesas",
        "Superhéroes",
        "Océano",
        "Magia",
        "Carros",
        "Naturaleza",
        "Robots"
    ]
)

color_favorito = st.selectbox(
    "🎨 Color favorito",
    ["Amarillo", "Azul", "Verde", "Rosado", "Morado", "Naranja"]
)

emocion = st.selectbox(
    "💛 ¿Cómo se siente últimamente?",
    [
        "Feliz",
        "Tímido",
        "Ansioso",
        "Curioso",
        "Tranquilo",
        "Inseguro"
    ]
)

tipo_actividad = st.selectbox(
    "🧩 Tipo de actividad favorita",
    [
        "Dibujar",
        "Jugar",
        "Contar historias",
        "Manualidades",
        "Explorar",
        "Movimiento"
    ]
)

# ---------------- BOTÓN ----------------

if st.button("✨ Crear mi AbraVentura"):

    with st.spinner("Creando una experiencia mágica... 🌈"):

        # ---------------- PROMPT IA ----------------

        prompt = f"""
        Crea una historia infantil corta y emocional.

        El protagonista debe ser un niño llamado {nombre}.

        Edad: {edad}

        Intereses: {intereses}

        Color favorito: {color_favorito}

        Emoción actual: {emocion}

        Debe aparecer un personaje llamado "Abrazador"
        que acompaña emocionalmente al niño.

        La historia debe:
        - ser tierna
        - fomentar la imaginación
        - incluir aprendizaje emocional
        - durar aproximadamente 3 minutos de lectura
        - tener lenguaje infantil
        - incluir una pequeña aventura

        Luego de la historia, crea:
        1. 3 preguntas para conectar emocionalmente con el niño
        2. 3 actividades para hacer juntos después de leer
        3. 2 momentos de conexión entre padre e hijo durante la lectura
        """

        # ---------------- IA ----------------

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un creador experto de historias infantiles emocionalmente significativas."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.9
        )

        resultado = response.choices[0].message.content

        # ---------------- RESULTADO ----------------

        st.markdown("## 📖 Tu AbraVentura")

        st.markdown(
            f"""
            <div class="story-box">
            {resultado}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- IMAGENES ----------------

        st.markdown("---")
        st.header("🌈 Inspiración visual")

        col3, col4, col5 = st.columns(3)

        with col3:
            st.image("images/story1.png")  # reemplazar manualmente

        with col4:
            st.image("images/story2.png")

        with col5:
            st.image("images/story3.png")

# ---------------- FOOTER ----------------

st.markdown("---")
st.markdown(
    """
    💛 AbraVenturas busca transformar la lectura en un momento de conexión,
    imaginación y aprendizaje compartido.
    """
)
