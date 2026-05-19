# app.py
# 💛 AbraVenturas - Hugger Island Edition

import streamlit as st
import random
import os

# ---------------- CONFIG ----------------

st.set_page_config(
    page_title="AbraVenturas",
    page_icon="💛",
    layout="wide",
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* ---------- FONDO ---------- */

.stApp {
    background: linear-gradient(
        180deg,
        #FFF9F3 0%,
        #FFFDFB 100%
    );
}

/* ---------- ESCONDER MENU ---------- */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ---------- BURBUJAS ---------- */

.bubble {
    position: fixed;
    border-radius: 50%;
    opacity: 0.18;
    z-index: -1;
    animation: float 9s ease-in-out infinite;
}

.b1 {
    width: 200px;
    height: 200px;
    background: #FFD166;
    top: 5%;
    left: 3%;
}

.b2 {
    width: 260px;
    height: 260px;
    background: #B8E1DD;
    top: 55%;
    left: 70%;
}

.b3 {
    width: 180px;
    height: 180px;
    background: #CDB4DB;
    top: 18%;
    right: 5%;
}

.b4 {
    width: 120px;
    height: 120px;
    background: #FFD6A5;
    bottom: 12%;
    left: 18%;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-25px); }
    100% { transform: translateY(0px); }
}

/* ---------- TITULO ---------- */

.main-title {
    font-size: 74px;
    font-weight: 800;
    color: #2A7C76;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 28px;
    color: #6A7B7B;
    margin-top: -10px;
}

/* ---------- HERO ---------- */

.hero-box {
    background: rgba(255,255,255,0.72);
    border-radius: 30px;
    padding: 30px;
    backdrop-filter: blur(12px);
    border: 2px solid rgba(255,255,255,0.5);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.04);
    margin-top: 20px;
    margin-bottom: 40px;
    color: #557070;
    font-size: 20px;
    line-height: 1.7;
}

/* ---------- FORM ---------- */

.section-title {
    color: #5C3D99;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 20px;
}

label {
    color: #557070 !important;
    font-weight: 600 !important;
}

/* ---------- INPUTS ---------- */

.stTextInput input {
    background: white !important;
    border-radius: 18px !important;
    border: 2px solid #E9E4DD !important;
    color: #557070 !important;
    height: 3.2rem;
}

.stSelectbox div[data-baseweb="select"] {
    background: white !important;
    border-radius: 18px !important;
    border: 2px solid #E9E4DD !important;
    color: #557070 !important;
}

.stMultiSelect div[data-baseweb="select"] {
    background: white !important;
    border-radius: 18px !important;
    border: 2px solid #E9E4DD !important;
    color: #557070 !important;
}

/* ---------- BOTON ---------- */

.stButton button {
    background: linear-gradient(
        135deg,
        #FFD166 0%,
        #FFB86B 100%
    );
    color: white;
    border: none;
    border-radius: 20px;
    padding: 16px 30px;
    font-size: 22px;
    font-weight: 700;
    box-shadow: 0px 10px 25px rgba(255,185,100,0.35);
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
}

/* ---------- STORY ---------- */

.story-card {
    background: white;
    border-radius: 30px;
    padding: 40px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.05);
    border: 3px solid #FFE3A3;
    margin-top: 30px;
}

.story-text {
    color: #5B6B6B;
    font-size: 22px;
    line-height: 1.9;
}

/* ---------- PREGUNTAS ---------- */

.question-box {
    background: #FFF7E8;
    padding: 20px;
    border-radius: 20px;
    margin-top: 15px;
    color: #557070;
    font-size: 18px;
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #8B8B8B;
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
        st.image("images/Abrazador_Imagen1.png", width=300)

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
<div class='hero-box'>
🌈 Cada AbraVentura está diseñada para fortalecer vínculos,
acompañar emociones y transformar la lectura en un momento
de conexión entre niños y familias.
</div>
""", unsafe_allow_html=True)

# ---------------- FORMULARIO ----------------

st.markdown(
    "<div class='section-title'>✨ Personalicemos la aventura</div>",
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

# ---------------- GENERADOR ----------------

def generar_historia():

    intereses_txt = ", ".join(intereses) if intereses else "aventuras mágicas"

    introducciones = [
        f"Una tarde brillante, {nombre} encontró un pequeño Abrazador escondido detrás de una nube dorada.",
        f"En una isla llena de estrellas suaves, {nombre} conoció a un Abrazador muy especial.",
        f"Mientras exploraba un bosque de colores, {nombre} escuchó una vocecita mágica diciendo: 'Hola amigo 💛'."
    ]

    aprendizajes = {
        "Feliz": "descubrió que compartir la felicidad la hace crecer aún más.",
        "Tímido": "aprendió que su voz también merece ser escuchada.",
        "Ansioso": "aprendió a respirar profundo y sentir calma.",
        "Curioso": "descubrió que hacer preguntas puede abrir puertas mágicas.",
        "Tranquilo": "entendió que la calma también tiene poder.",
        "Inseguro": "descubrió que dentro de sí ya existía valentía."
    }

    final = aprendizajes.get(emocion)

    historia = f"""
    {random.choice(introducciones)}

    Ese día comenzaron una aventura llena de {intereses_txt}.
    
    Mientras jugaban a {tipo_actividad.lower()},
    el cielo empezó a brillar de color {color_favorito.lower()}.

    El Abrazador tomó la mano de {nombre} y le recordó
    que todas las emociones son importantes 💛

    Al final del viaje, {nombre} {final}
    """

    return historia

# ---------------- BOTON ----------------

if st.button("✨ Crear mi AbraVentura"):

    if nombre == "":
        st.warning("Por favor escribe el nombre del niño 💛")

    else:

        historia = generar_historia()

        st.markdown("## 📖 Tu AbraVentura")

        st.markdown(
            f"""
            <div class='story-card'>
                <div class='story-text'>
                    {historia}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 💬 Preguntas para conectar")

        st.markdown("""
        <div class='question-box'>
        🌈 ¿Qué fue lo que más te gustó de la aventura?
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='question-box'>
        💛 ¿Cómo ayudó el Abrazador al personaje?
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='question-box'>
        ✨ ¿Qué otra aventura te gustaría vivir?
        </div>
        """, unsafe_allow_html=True)

        # -------- GALERIA --------

        st.markdown("## 🌈 Tus amigos abrazadores")

        c1, c2, c3 = st.columns(3)

        with c1:
            if os.path.exists("images/Abrazador_Imagen1.png"):
                st.image("images/Abrazador_Imagen1.png")

        with c2:
            if os.path.exists("images/Abrazador_Imagen2.png"):
                st.image("images/Abrazador_Imagen2.png")

        with c3:
            if os.path.exists("images/Abrazador_Imagen3.png"):
                st.image("images/Abrazador_Imagen3.png")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<div class='footer'>
💛 AbraVenturas transforma historias en momentos de conexión,
imaginación y amor compartido.
</div>
""", unsafe_allow_html=True)

