# app.py
# 🌈 AbraVenturas - Hugger Island

import streamlit as st
import random
import os

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* -------- Fondo principal -------- */

.stApp {
    background: linear-gradient(
        180deg,
        #FFF8F1 0%,
        #FFFDF8 100%
    );
    overflow-x: hidden;
}

/* -------- Burbujas flotantes -------- */

.bubble {
    position: fixed;
    border-radius: 50%;
    opacity: 0.18;
    animation: float 14s infinite ease-in-out;
    z-index: -1;
}

.b1 {
    width: 180px;
    height: 180px;
    background: #FFD166;
    top: 10%;
    left: 5%;
}

.b2 {
    width: 250px;
    height: 250px;
    background: #B8E1DD;
    top: 55%;
    left: 70%;
}

.b3 {
    width: 140px;
    height: 140px;
    background: #CDB4DB;
    top: 20%;
    right: 10%;
}

.b4 {
    width: 120px;
    height: 120px;
    background: #FFD6A5;
    bottom: 10%;
    left: 20%;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-25px);}
    100% {transform: translateY(0px);}
}

/* -------- TITULOS -------- */

.main-title {
    font-size: 72px;
    font-weight: 800;
    color: #2A7C76;
    text-align: center;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #5B6B6B;
    font-size: 28px;
    margin-top: -10px;
    margin-bottom: 30px;
}

/* -------- CARD HERO -------- */

.hero-card {
    background: rgba(255,255,255,0.7);
    padding: 30px;
    border-radius: 30px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
    border: 2px solid rgba(255,255,255,0.5);
    margin-bottom: 40px;
}

/* -------- FORM -------- */

.form-title {
    font-size: 42px;
    color: #5C3D99;
    font-weight: 700;
    margin-bottom: 20px;
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    border-radius: 18px !important;
}

/* -------- BOTON -------- */

.stButton button {
    background: linear-gradient(
        135deg,
        #FFD166 0%,
        #FF9F68 100%
    );
    color: white;
    border: none;
    border-radius: 18px;
    padding: 16px 28px;
    font-size: 22px;
    font-weight: 700;
    box-shadow: 0px 10px 25px rgba(255,160,90,0.35);
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
}

/* -------- STORY -------- */

.story-box {
    background: white;
    padding: 35px;
    border-radius: 28px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.05);
    border: 3px solid #FFE3A3;
    color: #444;
    font-size: 21px;
    line-height: 1.8;
    margin-top: 25px;
}

/* -------- FOOTER -------- */

.footer {
    text-align: center;
    color: #6B6B6B;
    margin-top: 60px;
    font-size: 18px;
}

</style>

<div class="bubble b1"></div>
<div class="bubble b2"></div>
<div class="bubble b3"></div>
<div class="bubble b4"></div>

""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

col1, col2 = st.columns([1,2])

with col1:
    if os.path.exists("images/Abrazador_Imagen1.png"):
        st.image("images/Abrazador_Imagen1.png", width=320)

with col2:
    st.markdown(
        "<div class='main-title'>💛 AbraVenturas</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Historias que abrazan la imaginación ✨</div>",
        unsafe_allow_html=True
    )

# ---------------- HERO ----------------

st.markdown("""
<div class='hero-card'>
🌈 Cada historia está diseñada para fortalecer vínculos,
crear conversaciones emocionales y hacer que los niños
se enamoren de la lectura.
</div>
""", unsafe_allow_html=True)

# ---------------- FORMULARIO ----------------

st.markdown(
    "<div class='form-title'>✨ Personalicemos la aventura</div>",
    unsafe_allow_html=True
)

colA, colB = st.columns(2)

with colA:

    nombre = st.text_input("👦 Nombre del niño")

    edad = st.selectbox(
        "🎂 Edad",
        ["3 años", "4 años", "5 años", "6 años", "7 años", "8 años"]
    )

    color_favorito = st.selectbox(
        "🎨 Color favorito",
        ["Amarillo", "Azul", "Verde", "Rosado", "Morado", "Naranja"]
    )

with colB:

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
        "🧩 Actividad favorita",
        [
            "Dibujar",
            "Jugar",
            "Contar historias",
            "Manualidades",
            "Explorar",
            "Movimiento"
        ]
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

# ---------------- HISTORIAS DEMO ----------------

historias_inicio = [
    "Una noche brillante",
    "En una montaña llena de estrellas",
    "En el bosque de los abrazos mágicos",
    "En una isla flotante de colores",
]

mensajes = [
    "descubrió que sentir emociones está bien",
    "aprendió que siempre puede pedir ayuda",
    "entendió que la imaginación puede sanar el corazón",
    "descubrió que nunca está solo"
]

# ---------------- BOTON ----------------

if st.button("✨ Crear mi AbraVentura"):

    if nombre == "":
        st.warning("Por favor escribe el nombre del niño 💛")

    else:

        inicio = random.choice(historias_inicio)
        mensaje = random.choice(mensajes)

        intereses_texto = ", ".join(intereses) if intereses else "aventuras mágicas"

        historia = f"""
        {inicio}, {nombre} de {edad} salió junto a su Abrazador
        favorito a explorar un mundo lleno de {intereses_texto}.

        Aunque últimamente se sentía {emocion.lower()},
        el Abrazador le enseñó que cada emoción tiene algo
        importante que decirnos.

        Durante la aventura jugaron a {tipo_actividad.lower()}
        mientras todo brillaba de color {color_favorito.lower()}.

        Al final del día, {nombre} {mensaje} 💛
        """

        st.markdown("## 📖 Tu AbraVentura")

        st.markdown(
            f"""
            <div class='story-box'>
            {historia}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 💬 Preguntas para conectar")

        st.write("🌈 ¿Qué fue lo que más te gustó de la aventura?")
        st.write("💛 ¿Qué emoción sintió el Abrazador?")
        st.write("✨ ¿Qué lugar te gustaría visitar después?")

        st.markdown("### 🎨 Actividades")

        st.write("🖍️ Dibujar al Abrazador")
        st.write("📚 Inventar un nuevo final")
        st.write("💌 Crear una carta para el personaje")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<div class='footer'>
💛 AbraVenturas busca transformar la lectura
en un momento de conexión, imaginación y amor.
</div>
""", unsafe_allow_html=True)
