# app.py
# 💛 AbraVenturas — Hugger Island Demo

import streamlit as st
import os
import random

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# CSS BONITO
# ---------------------------------------------------

st.markdown("""
<style>

/* ---------- FONDO ---------- */

.stApp {
    background: linear-gradient(
        180deg,
        #FFF9F3 0%,
        #F9F8F4 100%
    );
}

/* ---------- ESCONDER STREAMLIT ---------- */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* ---------- BOLITAS ---------- */

.ball {
    position: fixed;
    border-radius: 50%;
    opacity: 0.22;
    z-index: 0;
    animation: float 16s infinite ease-in-out;
}

.ball1 {
    width: 180px;
    height: 180px;
    background: #CDEBE7;
    top: 12%;
    left: 4%;
}

.ball2 {
    width: 140px;
    height: 140px;
    background: #F9D6C1;
    top: 70%;
    left: 80%;
}

.ball3 {
    width: 130px;
    height: 130px;
    background: #E4D7F5;
    top: 35%;
    left: 60%;
}

.ball4 {
    width: 100px;
    height: 100px;
    background: #FDE6A8;
    top: 75%;
    left: 18%;
}

@keyframes float {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-18px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* ---------- TITULO ---------- */

.title {
    text-align: center;
    color: #2D7C7C;
    font-size: 72px;
    font-weight: 800;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #6F7F7F;
    font-size: 28px;
    margin-top: -10px;
    margin-bottom: 40px;
}

/* ---------- CARD ---------- */

.main-card {
    background: rgba(255,255,255,0.75);
    padding: 40px;
    border-radius: 35px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.06);
    position: relative;
    z-index: 2;
}

/* ---------- LABELS ---------- */

label {
    color: #4E5F5F !important;
    font-weight: 700 !important;
}

/* ---------- INPUTS ---------- */

.stTextInput input {
    border-radius: 16px !important;
    border: 2px solid #D8ECE9 !important;
    padding: 12px !important;
    background-color: white !important;
    color: #444 !important;
}

.stSelectbox > div > div {
    border-radius: 16px !important;
}

/* ---------- MULTISELECT ---------- */

.stMultiSelect > div > div {
    border-radius: 16px !important;
}

/* ---------- BOTON ---------- */

.stButton button {
    background: linear-gradient(
        135deg,
        #FFD36E 0%,
        #FFB27A 100%
    ) !important;

    color: white !important;
    border: none !important;

    border-radius: 18px !important;

    padding: 15px 28px !important;

    font-size: 20px !important;
    font-weight: bold !important;

    box-shadow: 0 8px 20px rgba(255,178,122,0.35);

    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
}

/* ---------- STORY ---------- */

.story-box {

    background: white;

    padding: 35px;

    border-radius: 28px;

    border: 3px solid #FFE4A8;

    color: #425466;

    font-size: 20px;

    line-height: 1.9;

    margin-top: 30px;

    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #7A8888;
    margin-top: 50px;
    font-size: 16px;
}

</style>

<div class="ball ball1"></div>
<div class="ball ball2"></div>
<div class="ball ball3"></div>
<div class="ball ball4"></div>

""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="title">
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

# ---------------------------------------------------
# CONTENEDOR
# ---------------------------------------------------

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("## ✨ Personalicemos la aventura")

# ---------------------------------------------------
# FORMULARIO
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    nombre = st.text_input(
        "👦 Nombre del niño",
        placeholder="Ejemplo: Camila"
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
            "Morado",
            "Rosado",
            "Naranja"
        ]
    )

with col2:

    emocion = st.selectbox(
        "💛 ¿Cómo se siente últimamente?",
        [
            "Feliz",
            "Curioso",
            "Ansioso",
            "Tímido",
            "Tranquilo"
        ]
    )

    actividad = st.selectbox(
        "🧩 Actividad favorita",
        [
            "Dibujar",
            "Explorar",
            "Jugar",
            "Contar historias",
            "Manualidades"
        ]
    )

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    [
        "Espacio",
        "Dinosaurios",
        "Océano",
        "Animales",
        "Magia",
        "Robots",
        "Naturaleza"
    ]
)

# ---------------------------------------------------
# HISTORIAS DEMO
# ---------------------------------------------------

historias = {

    "Feliz": [
        """
        🌈 {nombre} y Abrazador encontraron una nube mágica
        de color {color}.

        Mientras jugaban a {actividad},
        descubrieron estrellas escondidas
        entre el cielo.

        Esa noche,
        {nombre} aprendió que compartir alegría
        hace que el corazón brille más fuerte. ✨
        """
    ],

    "Ansioso": [
        """
        🌙 {nombre} sentía muchas cosquillas
        en el pecho.

        Entonces apareció Abrazador 💛
        y juntos respiraron lentamente
        mientras miraban el cielo {color}.

        Poco a poco,
        las preocupaciones se transformaron
        en pequeñas estrellas tranquilas.
        """
    ],

    "Curioso": [
        """
        🚀 {nombre} abrió una puerta secreta
        que llevaba a un mundo lleno de {interes}.

        Allí conoció a Abrazador,
        quien le enseñó que hacer preguntas
        puede abrir aventuras increíbles. ✨
        """
    ],

    "Tímido": [
        """
        🦋 {nombre} encontró un jardín escondido.

        Abrazador 💛 le explicó que incluso
        las flores más pequeñas
        pueden llenar el mundo de colores.

        Desde ese día,
        {nombre} comenzó a mostrar
        su luz poquito a poquito.
        """
    ],

    "Tranquilo": [
        """
        ☁️ Una tarde suave,
        {nombre} caminó junto a Abrazador
        por un bosque silencioso.

        Mientras observaban árboles {color},
        aprendieron que la calma
        también es una forma de magia. ✨
        """
    ]
}

# ---------------------------------------------------
# BOTON
# ---------------------------------------------------

if st.button("✨ Crear mi AbraVentura"):

    if nombre == "":
        st.warning("Por favor escribe el nombre del niño 💛")

    else:

        lista = historias.get(emocion, [])

        historia = random.choice(lista)

        interes = (
            intereses[0]
            if len(intereses) > 0
            else "aventuras mágicas"
        )

        resultado = historia.format(
            nombre=nombre,
            color=color_favorito.lower(),
            actividad=actividad.lower(),
            interes=interes.lower()
        )

        # ---------------------------------------------------
        # RESULTADO
        # ---------------------------------------------------

        st.markdown("## 📖 Tu historia")

        st.markdown(
            f"""
            <div class="story-box">
            {resultado}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
    💛 AbraVenturas transforma la lectura
    en momentos de conexión emocional.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
