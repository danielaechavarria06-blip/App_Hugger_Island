# app.py
# 🌈 AbraVenturas — Hugger Island Edition
# Interfaz emocional + historias personalizadas

# ---------------- LIBRERÍAS ----------------
import streamlit as st
from openai import OpenAI
import os
import base64
import random

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- FONDO + ESTILO WOW ----------------
st.markdown("""
<style>

/* -------- FONDO GENERAL -------- */

.stApp {
    background: linear-gradient(
        180deg,
        #F8F6F2 0%,
        #FFF6EC 35%,
        #F3F8F7 100%
    );
    overflow-x: hidden;
}

/* -------- BOMBAS FLOTANTES -------- */

.bubble {
    position: fixed;
    border-radius: 50%;
    opacity: 0.25;
    animation: floatBubble linear infinite;
    z-index: 0;
}

.b1 {
    width: 120px;
    height: 120px;
    background: #BFE7E3;
    left: 5%;
    animation-duration: 18s;
    top: 100%;
}

.b2 {
    width: 80px;
    height: 80px;
    background: #FFD27F;
    left: 20%;
    animation-duration: 15s;
    top: 110%;
}

.b3 {
    width: 150px;
    height: 150px;
    background: #D8C4F1;
    left: 50%;
    animation-duration: 22s;
    top: 120%;
}

.b4 {
    width: 90px;
    height: 90px;
    background: #BDE37E;
    left: 75%;
    animation-duration: 17s;
    top: 115%;
}

.b5 {
    width: 70px;
    height: 70px;
    background: #FFB58C;
    left: 90%;
    animation-duration: 14s;
    top: 100%;
}

@keyframes floatBubble {
    0% {
        transform: translateY(0px) translateX(0px);
    }
    50% {
        transform: translateY(-50vh) translateX(25px);
    }
    100% {
        transform: translateY(-120vh) translateX(-10px);
    }
}

/* -------- CONTENEDOR PRINCIPAL -------- */

.main-container {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(12px);
    border-radius: 35px;
    padding: 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
    position: relative;
    z-index: 2;
}

/* -------- TITULOS -------- */

.big-title {
    font-size: 68px;
    font-weight: 800;
    color: #2F7A7A;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 24px;
    color: #6D7B7B;
    margin-top: -10px;
}

/* -------- CARDS -------- */

.soft-card {
    background: rgba(255,255,255,0.72);
    padding: 20px;
    border-radius: 25px;
    border: 2px solid rgba(255,255,255,0.4);
    box-shadow: 0 6px 25px rgba(0,0,0,0.05);
}

/* -------- INPUTS -------- */

.stTextInput input {
    border-radius: 18px !important;
    border: 2px solid #BFE7E3 !important;
    padding: 12px !important;
    background: white !important;
}

.stSelectbox > div {
    border-radius: 18px !important;
}

.stMultiSelect > div {
    border-radius: 18px !important;
}

/* -------- BOTONES -------- */

.stButton button {
    background: linear-gradient(
        135deg,
        #FFCF6E 0%,
        #FF9D76 100%
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 18px !important;

    padding: 15px 28px !important;

    font-size: 20px !important;
    font-weight: 700 !important;

    transition: 0.3s;
    box-shadow: 0 8px 20px rgba(255,157,118,0.35);
}

.stButton button:hover {
    transform: translateY(-3px) scale(1.02);
}

/* -------- STORY BOX -------- */

.story-box {
    background: linear-gradient(
        180deg,
        rgba(255,255,255,0.92),
        rgba(255,248,240,0.96)
    );

    padding: 35px;
    border-radius: 30px;
    border: 3px solid #FFE0A8;

    color: #425466;
    font-size: 20px;
    line-height: 1.9;

    box-shadow: 0 12px 35px rgba(0,0,0,0.06);

    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* -------- FOOTER -------- */

.footer {
    text-align: center;
    color: #7B8B8B;
    padding: 30px;
    font-size: 17px;
}

/* -------- ESCONDER MENU -------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>

<!-- Bombitas -->
<div class="bubble b1"></div>
<div class="bubble b2"></div>
<div class="bubble b3"></div>
<div class="bubble b4"></div>
<div class="bubble b5"></div>

""", unsafe_allow_html=True)

# ---------------- API KEY ----------------
# OPCIÓN 1 → STREAMLIT CLOUD SECRETS
# crea .streamlit/secrets.toml

# OPENAI_API_KEY = "TU_API"

# Luego:
api_key = st.secrets.get("OPENAI_API_KEY", None)

# Si NO hay API:
modo_demo = False

if api_key:
    client = OpenAI(api_key=api_key)
else:
    modo_demo = True

# ---------------- HEADER ----------------

st.markdown('<div class="main-container">', unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:

    if os.path.exists("images/Abrazador_Imagen1.png"):
        st.image("images/Abrazador_Imagen1.png", width=320)

with col2:

    st.markdown(
        """
        <div class="big-title">
        💛 AbraVenturas
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Historias que abrazan la imaginación ✨
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="soft-card">
        🌈 Cada historia está diseñada para fortalecer vínculos,
        fomentar la lectura y crear momentos mágicos
        entre niños y familias.
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- FORM ----------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("## ✨ Personalicemos la aventura")

c1, c2 = st.columns(2)

with c1:

    nombre = st.text_input("👦 Nombre del niño")

    edad = st.selectbox(
        "🎂 Edad",
        ["3 años","4 años","5 años","6 años","7 años","8 años"]
    )

    color_favorito = st.selectbox(
        "🎨 Color favorito",
        ["Amarillo","Azul","Verde","Rosado","Morado","Naranja"]
    )

with c2:

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
            "Explorar",
            "Contar historias",
            "Manualidades"
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
        "Robots",
        "Naturaleza",
        "Carros"
    ]
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BOTÓN ----------------

if st.button("✨ Crear mi AbraVentura"):

    with st.spinner("Creando magia emocional... 🌈"):

        # ---------------- MODO IA ----------------

        if not modo_demo:

            prompt = f"""
            Crea una historia infantil emocional y mágica.

            El protagonista es un niño llamado {nombre}.

            Edad: {edad}

            Intereses:
            {intereses}

            Color favorito:
            {color_favorito}

            Emoción actual:
            {emocion}

            Actividad favorita:
            {tipo_actividad}

            Debe aparecer un personaje llamado
            "Abrazador".

            La historia debe:
            - ser tierna
            - emocional
            - divertida
            - fomentar imaginación
            - tener aprendizaje emocional
            - durar 3 minutos
            - tener lenguaje infantil
            """

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en cuentos emocionales infantiles."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.9
            )

            resultado = response.choices[0].message.content

        # ---------------- MODO DEMO SIN API ----------------

        else:

            historias_demo = [

f"""
Había una vez un pequeño llamado {nombre}
que soñaba con explorar un bosque mágico lleno de luces.

Una noche apareció Abrazador 💛,
quien le enseñó que incluso cuando sentimos miedo,
nuestro corazón puede encontrar valentía.

Juntos descubrieron árboles que brillaban
con el color {color_favorito.lower()}
y animales mágicos que amaban {intereses[0] if intereses else "la imaginación"}.

Al final,
{name} descubrió que dentro de él siempre había luz.
""",

f"""
{name} encontró una puerta secreta debajo de su cama.

Al abrirla,
conoció a Abrazador ✨.

Viajaron juntos a una isla flotante donde todos
aprendían a transformar emociones en estrellas.

Cuando {nombre} se sintió {emocion.lower()},
Abrazador le recordó algo importante:

"Las emociones no son malas,
son mensajes de tu corazón."
"""
            ]

            resultado = random.choice(historias_demo)

        # ---------------- RESULTADO ----------------

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown("## 📖 Tu AbraVentura")

        st.markdown(
            f"""
            <div class="story-box">
            {resultado}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- GALERÍA ----------------

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown("## 🌈 Mundo Hugger")

        g1, g2, g3 = st.columns(3)

        with g1:
            if os.path.exists("images/Abrazador_Imagen1.png"):
                st.image("images/Abrazador_Imagen1.png")

        with g2:
            if os.path.exists("images/Abrazador_Imagen2.png"):
                st.image("images/Abrazador_Imagen2.png")

        with g3:
            if os.path.exists("images/Abrazador_Imagen3.png"):
                st.image("images/Abrazador_Imagen3.png")

# ---------------- FOOTER ----------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
    💛 AbraVenturas transforma la lectura
    en momentos de conexión emocional,
    imaginación y amor compartido.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
