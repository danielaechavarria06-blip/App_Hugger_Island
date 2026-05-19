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

/* ---------------- FLOATING BUBBLES ---------------- */

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
    opacity: 0.25;
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

/* ---------------- HERO ---------------- */

.hero {
    background: rgba(255,255,255,0.72);
    border-radius: 35px;
    padding: 30px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 10px 40px rgba(0,0,0,0.05);
    margin-bottom: 30px;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    color: #0F766E;
    line-height: 1;
}

.hero-sub {
    font-size: 28px;
    color: #52796F;
    margin-top: 10px;
}

/* ---------------- FORM ---------------- */

.form-card {
    background: rgba(255,255,255,0.75);
    padding: 35px;
    border-radius: 35px;
    box-shadow: 0px 8px 35px rgba(0,0,0,0.05);
    backdrop-filter: blur(12px);
}

.section-title {
    font-size: 42px;
    font-weight: 800;
    color: #0F766E;
}

.section-sub {
    color: #6B9080;
    font-size: 20px;
    margin-bottom: 30px;
}

/* ---------------- BUTTON ---------------- */

.stButton button {
    background: linear-gradient(
        90deg,
        #0F766E,
        #1D9A8C
    ) !important;

    color: white !important;
    border-radius: 18px !important;
    padding: 18px 30px !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    border: none !important;
    width: 100%;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* ---------------- INPUTS ---------------- */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 18px !important;
}

/* ---------------- STORY ---------------- */

.story-box {
    background: white;
    border-radius: 30px;
    padding: 40px;
    margin-top: 30px;
    border: 4px solid #F7D66B;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.04);
}

.story-title {
    color: #0F766E;
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 20px;
}

.story-text {
    color: #4A5759;
    font-size: 22px;
    line-height: 1.8;
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
# HERO
# ---------------------------------------------------

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if os.path.exists("images/Abrazador_Imagen1.png"):
        st.image("images/Abrazador_Imagen1.png")

with col2:
    st.markdown("""
    <div class="hero">
        <div class="hero-title">
            💛 AbraVenturas
        </div>

        <div class="hero-sub">
            Historias que abrazan la imaginación ✨
        </div>

        <br>

        <div style="
            background:#FFFFFF;
            padding:20px;
            border-radius:20px;
            color:#52796F;
            font-size:22px;
            line-height:1.6;
        ">
            🌈 Cada historia fortalece vínculos,
            acompaña emociones y transforma
            la lectura en un momento mágico.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    if os.path.exists("images/Abrazador_Imagen2.png"):
        st.image("images/Abrazador_Imagen2.png")

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

    Tu color favorito es {color_favorito},
    amas {", ".join(intereses) if intereses else "imaginar cosas mágicas"}
    y disfrutas mucho {tipo_actividad.lower()}.

    {historia_base}

    🌈 Fin de la AbraVentura.
    """

    st.markdown(f"""
    <div class="story-box">

        <div class="story-title">
        📖 Tu AbraVentura
        </div>

        <div class="story-text">
        {historia_final}
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

