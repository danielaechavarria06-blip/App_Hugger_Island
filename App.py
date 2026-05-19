import streamlit as st
from openai import OpenAI
import os

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide"
)

# ---------------- ESTILOS ----------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
    background-color: #F8F5F2;
}

.main {
    background-color: #F8F5F2;
}

.block-container {
    padding-top: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* PORTADA */

.portada-container img {
    border-radius: 30px;
    margin-bottom: 20px;
}

/* CARD */

.form-card {
    background: white;
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
    margin-top: -30px;
}

/* TITULOS */

h1 {
    color: #0B7A75;
    font-size: 55px !important;
    font-weight: 800;
}

h2 {
    color: #0B7A75;
    font-size: 42px !important;
    font-weight: 700;
}

p {
    color: #6B8F8B;
    font-size: 20px;
}

/* INPUTS */

.stTextInput input {
    border-radius: 15px;
    border: 2px solid #EAEAEA;
    padding: 14px;
    background-color: white;
    color: #333333;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 15px;
}

/* BOTON */

.stButton button {
    background: linear-gradient(90deg,#0B7A75,#12A39D);
    color: white;
    border-radius: 18px;
    border: none;
    padding: 16px 30px;
    font-size: 22px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* HISTORIA */

.story-box {
    background: white;
    padding: 35px;
    border-radius: 30px;
    margin-top: 30px;
    border: 2px solid #F1E6D6;
    color: #444444;
    font-size: 20px;
    line-height: 1.8;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
}

/* BURBUJAS */

.bubble {
    position: fixed;
    bottom: -100px;
    background: rgba(255,255,255,0.5);
    border-radius: 50%;
    animation: rise 15s infinite ease-in;
    z-index: 0;
}

.bubble:nth-child(1){
    width:40px;
    height:40px;
    left:10%;
    animation-duration:12s;
}

.bubble:nth-child(2){
    width:25px;
    height:25px;
    left:30%;
    animation-duration:16s;
}

.bubble:nth-child(3){
    width:60px;
    height:60px;
    left:50%;
    animation-duration:18s;
}

.bubble:nth-child(4){
    width:20px;
    height:20px;
    left:70%;
    animation-duration:14s;
}

.bubble:nth-child(5){
    width:50px;
    height:50px;
    left:90%;
    animation-duration:20s;
}

@keyframes rise {
    0%{
        transform:translateY(0);
        opacity:0;
    }

    50%{
        opacity:0.5;
    }

    100%{
        transform:translateY(-1200px);
        opacity:0;
    }
}

</style>

<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>

""", unsafe_allow_html=True)

# ---------------- OPENAI ----------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ---------------- PORTADA ----------------

if os.path.exists("portada.png"):
    st.image("portada.png", use_container_width=True)

# ---------------- FORMULARIO ----------------

st.markdown("""
<div class="form-card">
<h2>✨ Personalicemos la aventura</h2>
<p>Cuéntanos un poco sobre tu pequeño lector 💛</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- CAMPOS ----------------

col1, col2 = st.columns(2)

with col1:

    nombre = st.text_input(
        "👦 Nombre del niño"
    )

    edad = st.selectbox(
        "🎂 Edad",
        [
            "3 años",
            "4 años",
            "5 años",
            "6 años",
            "7 años",
            "8 años"
        ]
    )

    color_favorito = st.selectbox(
        "🎨 Color favorito",
        [
            "Amarillo",
            "Azul",
            "Verde",
            "Rosado",
            "Morado",
            "Naranja"
        ]
    )

with col2:

    emocion = st.selectbox(
        "💛 ¿Cómo se siente últimamente?",
        [
            "Feliz",
            "Ansioso",
            "Curioso",
            "Tranquilo",
            "Tímido"
        ]
    )

    actividad = st.selectbox(
        "🧩 Actividad favorita",
        [
            "Dibujar",
            "Explorar",
            "Jugar",
            "Leer",
            "Contar historias"
        ]
    )

# ---------------- INTERESES ----------------

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    [
        "Animales",
        "Espacio",
        "Naturaleza",
        "Arte",
        "Música",
        "Aventuras",
        "Ciencia"
    ]
)

st.write("")

# ---------------- BOTON ----------------

if st.button("⭐ Crear mi AbraVentura"):

    with st.spinner("Creando una aventura mágica... ✨"):

        prompt = f"""
        Crea una historia infantil MUY corta y tierna.

        Niño: {nombre}
        Edad: {edad}
        Color favorito: {color_favorito}
        Emoción: {emocion}
        Actividad favorita: {actividad}
        Intereses: {intereses}

        Debe aparecer un personaje llamado Abrazador.

        La historia debe:
        - durar menos de 1 minuto
        - ser emocional
        - ser muy tierna
        - fomentar la imaginación
        - tener final feliz
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role":"system",
                    "content":"Eres un experto creando historias infantiles tiernas."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.9
        )

        historia = response.choices[0].message.content

        st.markdown(f"""
        <div class="story-box">
        {historia}
        </div>
        """, unsafe_allow_html=True)
