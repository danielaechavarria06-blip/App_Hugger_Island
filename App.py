# app.py
# AbraVenturas ✨
# Hugger Island inspired UI

import streamlit as st
from PIL import Image
import os
import random

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide"
)

# ---------------------------------------------------
# HISTORIAS PREDEFINIDAS
# ---------------------------------------------------

historias = [

    {
        "emocion": "Ansioso",
        "historia": """
        Manuel sentía muchas maripositas en la barriga antes de dormir.
        Entonces apareció Abrazador con una linterna mágica color verde.

        —Las emociones no son monstruos —dijo Abrazador—,
        son mensajes que quieren abrazos.

        Juntos caminaron por un bosque brillante donde cada árbol
        contaba una historia tranquila.

        Al final, Manuel respiró profundo y descubrió que podía
        sentirse valiente incluso cuando tenía miedo. 💛
        """
    },

    {
        "emocion": "Feliz",
        "historia": """
        Sofía despertó llena de energía y sonrisas.
        Abrazador llegó saltando entre estrellas amarillas.

        Juntos construyeron una ciudad de almohadas,
        dibujos y canciones mágicas.

        Cada risa hacía aparecer nuevas luces en el cielo.

        Antes de dormir, Sofía entendió que compartir su alegría
        hacía felices a los demás también. ✨
        """
    },

    {
        "emocion": "Tímido",
        "historia": """
        Lucas quería jugar,
        pero las palabras se escondían dentro de él.

        Entonces Abrazador le regaló una pequeña estrella morada.

        Cada vez que Lucas sonreía,
        la estrella brillaba más fuerte.

        Poco a poco comenzó a hablar,
        jugar y descubrir que ser tímido también puede ser hermoso. 🌈
        """
    },

    {
        "emocion": "Curioso",
        "historia": """
        Valentina tenía mil preguntas en su cabeza.

        Abrazador la llevó a un planeta lleno de libros flotantes,
        animales parlantes y puertas secretas.

        Allí descubrió que hacer preguntas
        era una forma mágica de explorar el mundo.

        Desde ese día,
        nunca dejó de imaginar aventuras nuevas. 🚀
        """
    }

]

# ---------------------------------------------------
# CSS WOW ✨
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: linear-gradient(
        180deg,
        #FFF9F4 0%,
        #FFFDFB 100%
    );
}

/* OCULTAR STREAMLIT */

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ---------------- BUBBLES ---------------- */

.bubbles {
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
    top: 0;
    left: 0;
}

.bubble {
    position: absolute;
    bottom: -120px;
    border-radius: 50%;
    opacity: 0.20;
    animation: rise 18s infinite ease-in;
}

.b1 {
    width: 120px;
    height: 120px;
    left: 10%;
    background: #F7D66B;
    animation-duration: 20s;
}

.b2 {
    width: 80px;
    height: 80px;
    left: 30%;
    background: #A8DAD5;
    animation-duration: 16s;
}

.b3 {
    width: 140px;
    height: 140px;
    left: 55%;
    background: #F7C5E0;
    animation-duration: 24s;
}

.b4 {
    width: 90px;
    height: 90px;
    left: 75%;
    background: #C7E59B;
    animation-duration: 17s;
}

.b5 {
    width: 100px;
    height: 100px;
    left: 88%;
    background: #BFA2DB;
    animation-duration: 21s;
}

@keyframes rise {
    0% {
        transform: translateY(0px);
        opacity: 0;
    }

    30% {
        opacity: 0.25;
    }

    100% {
        transform: translateY(-1200px);
        opacity: 0;
    }
}

/* ---------------- PORTADA ---------------- */

.portada-container img {
    border-radius: 0px 0px 40px 40px;
}

/* ---------------- FORM ---------------- */

.form-card {
    background: rgba(255,255,255,0.82);
    padding: 45px;
    border-radius: 40px;
    box-shadow: 0px 8px 35px rgba(0,0,0,0.05);
    backdrop-filter: blur(12px);
    margin-top: -40px;
}

/* ---------------- TITULOS ---------------- */

.section-title {
    font-size: 52px;
    font-weight: 800;
    color: #0F766E;
    text-align:center;
}

.section-sub {
    color: #52796F;
    font-size: 22px;
    margin-bottom: 35px;
    text-align:center;
}

/* ---------------- LABELS ---------------- */

label, .stMarkdown, p {
    color: #355070 !important;
    font-weight: 700 !important;
    font-size: 18px !important;
}

/* ---------------- INPUTS ---------------- */

.stTextInput input {
    border-radius: 18px !important;
    background: #DFF6FF !important;
    color: #355070 !important;
    border: 2px solid #BEE9F7 !important;
    font-size: 18px !important;
}

/* ---------------- SELECTBOX ---------------- */

.stSelectbox div[data-baseweb="select"] {
    background: #DFF6FF !important;
    border-radius: 18px !important;
    border: 2px solid #BEE9F7 !important;
    color: #355070 !important;
}

.stSelectbox span {
    color: #355070 !important;
    font-weight: 700 !important;
}

/* ---------------- MULTISELECT ---------------- */

.stMultiSelect div[data-baseweb="select"] {
    background: #DFF6FF !important;
    border-radius: 18px !important;
    border: 2px solid #BEE9F7 !important;
}

.stMultiSelect span {
    color: #355070 !important;
    font-weight: 700 !important;
}

/* ---------------- BUTTON ---------------- */

.stButton button {
    background: linear-gradient(
        90deg,
        #0F766E,
        #1D9A8C
    ) !important;

    color: white !important;
    border-radius: 22px !important;
    padding: 18px 30px !important;
    font-size: 24px !important;
    font-weight: 700 !important;
    border: none !important;
    width: 100%;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* ---------------- STORY ---------------- */

.story-box {
    background: white !important;
    border-radius: 35px;
    padding: 45px;
    margin-top: 35px;
    border: 4px solid #F7D66B;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.04);
}

.story-title {
    color: #0F766E !important;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 25px;
    text-align:center;
}

.story-text {
    color: #355070 !important;
    font-size: 24px;
    line-height: 1.9;
    white-space: pre-line;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    margin-top: 60px;
    color: #52796F;
    font-size: 18px;
    padding-bottom: 30px;
}

</style>

<div class="bubbles">
    <div class="bubble b1"></div>
    <div class="bubble b2"></div>
    <div class="bubble b3"></div>
    <div class="bubble b4"></div>
    <div class="bubble b5"></div>
</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------
# PORTADA
# ---------------------------------------------------

if os.path.exists("portada.png"):
    st.markdown('<div class="portada-container">', unsafe_allow_html=True)
    st.image("portada.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------
# FORM
# ---------------------------------------------------

st.markdown("""
<div class="form-card">
<div class="section-title">
✨ Personalicemos la aventura
</div>

<div class="section-sub">
Cuéntanos un poco sobre tu pequeño lector 💛
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:

    nombre = st.text_input("👦 Nombre del niño")

    edad = st.selectbox(
        "🎂 Edad",
        ["3 años", "4 años", "5 años", "6 años", "7 años", "8 años"]
    )

    color_favorito = st.selectbox(
        "🎨 Color favorito",
        ["Amarillo", "Azul", "Verde", "Rosado", "Morado", "Naranja"]
    )

    animal_favorito = st.selectbox(
        "🦊 Animal favorito",
        [
            "Perro",
            "Gato",
            "Conejo",
            "Dinosaurio",
            "Panda",
            "León",
            "Delfín"
        ]
    )

with c2:

    emocion = st.selectbox(
        "💛 ¿Cómo se siente últimamente?",
        [
            "Feliz",
            "Tímido",
            "Ansioso",
            "Curioso"
        ]
    )

    tipo_actividad = st.selectbox(
        "🧩 Actividad favorita",
        [
            "Dibujar",
            "Jugar",
            "Contar historias",
            "Explorar"
        ]
    )

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    [
        "Animales",
        "Espacio",
        "Naturaleza",
        "Arte",
        "Música",
        "Aventuras"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# GENERAR
# ---------------------------------------------------

st.write("")
st.write("")

if st.button("⭐ Crear mi AbraVentura"):

    historia_base = next(
        (
            h["historia"]
            for h in historias
            if h["emocion"] == emocion
        ),
        random.choice(historias)["historia"]
    )

    historia_final = f"""
Hola {nombre} 💛

Hoy vivirás una aventura especial.

Tienes {edad},
tu color favorito es {color_favorito}
y tu animal favorito es {animal_favorito}.

También amas
{", ".join(intereses) if intereses else "imaginar aventuras mágicas"}.

Disfrutas mucho {tipo_actividad.lower()}.

{historia_base}

🌈 Fin de la AbraVentura.
"""

    st.markdown(f"""
    <div class="story-box">

        <div class="story-title">
        📖 Tu AbraVentura
        </div>

        <div class="story-text">
        {historia_final.replace('\\n', '<br>')}
        </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
💛 Hugger Island • Abraza • Conecta • Transforma
</div>
""", unsafe_allow_html=True)
