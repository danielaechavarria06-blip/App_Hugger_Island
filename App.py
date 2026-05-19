# app.py
# AbraVenturas ✨
# Hugger Island inspired UI

import streamlit as st
import html as html_module
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

/* ------------------------------------------------ */
/* FONDO */
/* ------------------------------------------------ */

.stApp {
    background: linear-gradient(
        180deg,
        #FFF9F4 0%,
        #FFFDFB 100%
    );
}

/* ------------------------------------------------ */
/* OCULTAR STREAMLIT */
/* ------------------------------------------------ */

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ------------------------------------------------ */
/* BURBUJAS */
/* ------------------------------------------------ */

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
    bottom: -150px;
    border-radius: 50%;
    opacity: 0.18;
    animation: rise 22s infinite ease-in;
}

.b1 {
    width: 120px;
    height: 120px;
    left: 10%;
    background: #F7D66B;
    animation-duration: 20s;
}

.b2 {
    width: 90px;
    height: 90px;
    left: 30%;
    background: #A8DAD5;
    animation-duration: 17s;
}

.b3 {
    width: 140px;
    height: 140px;
    left: 55%;
    background: #F7C5E0;
    animation-duration: 24s;
}

.b4 {
    width: 100px;
    height: 100px;
    left: 75%;
    background: #C7E59B;
    animation-duration: 19s;
}

.b5 {
    width: 110px;
    height: 110px;
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
        opacity: 0.18;
    }

    100% {
        transform: translateY(-1400px);
        opacity: 0;
    }

}

/* ------------------------------------------------ */
/* PORTADA */
/* ------------------------------------------------ */

.portada-container img {
    border-radius: 0px 0px 40px 40px;
}

/* ------------------------------------------------ */
/* FORM CARD */
/* ------------------------------------------------ */

.form-card {

    background: rgba(255,255,255,0.82);
    padding: 45px;
    border-radius: 40px;

    box-shadow:
        0px 10px 40px rgba(0,0,0,0.05);

    backdrop-filter: blur(12px);

    margin-top: -40px;
}

/* ------------------------------------------------ */
/* TITULOS */
/* ------------------------------------------------ */

.section-title {

    font-size: 52px;
    font-weight: 800;
    color: #0F766E;

    text-align: center;
}

.section-sub {

    color: #4A5759;
    font-size: 22px;

    margin-bottom: 35px;

    text-align: center;
}

/* ------------------------------------------------ */
/* LABELS */
/* ------------------------------------------------ */

label,
p,
span {

    color: #1F2937 !important;
    font-weight: 700 !important;
}

/* ------------------------------------------------ */
/* INPUTS */
/* ------------------------------------------------ */

.stTextInput input {

    background: #DFF4FF !important;
    color: #1F2937 !important;

    border-radius: 18px !important;
    border: none !important;

    padding: 12px !important;
}

/* ------------------------------------------------ */
/* SELECTBOX */
/* ------------------------------------------------ */

.stSelectbox div[data-baseweb="select"] > div {

    background: #DFF4FF !important;
    color: #1F2937 !important;

    border-radius: 18px !important;
    border: none !important;
}

/* ------------------------------------------------ */
/* MULTISELECT */
/* ------------------------------------------------ */

.stMultiSelect div[data-baseweb="select"] > div {

    background: #DFF4FF !important;
    color: #1F2937 !important;

    border-radius: 18px !important;
    border: none !important;
}

/* ------------------------------------------------ */
/* BOTON */
/* ------------------------------------------------ */

.stButton button {

    background: linear-gradient(
        90deg,
        #56CFE1,
        #72DDF7
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

/* ------------------------------------------------ */
/* STORY */
/* ------------------------------------------------ */

.story-box {

    background: white;

    border-radius: 35px;

    padding: 45px;

    margin-top: 35px;

    border: 4px solid #F7D66B;

    box-shadow:
        0px 8px 30px rgba(0,0,0,0.04);
}

.story-title {

    color: #0F766E;

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 25px;

    text-align: center;
}

.story-text {

    color: #374151;

    font-size: 24px;

    line-height: 1.9;

    white-space: pre-line;
}

/* ------------------------------------------------ */
/* FOOTER */
/* ------------------------------------------------ */

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

    st.markdown(
        '<div class="portada-container">',
        unsafe_allow_html=True
    )

    st.image(
        "portada.png",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

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

    animal_favorito = st.selectbox(
        "🐻 Animal favorito",
        [
            "Perro",
            "Gato",
            "Conejo",
            "Delfín",
            "León",
            "Panda",
            "Tortuga",
            "Dragón"
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
# GENERAR HISTORIA
# ---------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button("⭐ Crear mi AbraVentura"):

    if not nombre.strip():
        st.warning("¡Por favor escribe el nombre del niño! 👦")

    else:

        # Buscar historia por emoción, con fallback seguro
        historia_encontrada = next(
            (h for h in historias if h["emocion"] == emocion),
            random.choice(historias)
        )
        historia_base = historia_encontrada["historia"]

        # Escapar entradas del usuario para evitar HTML injection
        nombre_safe = html_module.escape(nombre.strip())
        intereses_texto = html_module.escape(
            ", ".join(intereses) if intereses else "aventuras mágicas"
        )
        edad_safe = html_module.escape(edad)
        color_safe = html_module.escape(color_favorito)
        animal_safe = html_module.escape(animal_favorito)
        actividad_safe = html_module.escape(tipo_actividad.lower())

        historia_final = f"""
Hola {nombre_safe} 💛

Hoy vivirás una aventura muy especial.

Tienes {edad_safe},
tu color favorito es {color_safe}
y tu animal favorito es {animal_safe}.

También amas {intereses_texto}
y disfrutas mucho {actividad_safe}.

{historia_base}

🌈 Fin de la AbraVentura.
"""

        st.markdown(
            f"""
<div class="story-box">

    <div class="story-title">
        📖 Tu AbraVentura
    </div>

    <div class="story-text">
        {historia_final}
    </div>

</div>
""",
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
💛 Hugger Island • Abraza • Conecta • Transforma
</div>
""", unsafe_allow_html=True)
