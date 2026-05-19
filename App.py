import streamlit as st
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
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

/* FONDO */
.stApp {
    background: #F8F5F2;
}

/* OCULTAR HEADER STREAMLIT */
header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* BURBUJAS */

.bubbles{
    position:fixed;
    width:100%;
    height:100%;
    z-index:-1;
    top:0;
    left:0;
    overflow:hidden;
}

.bubble{
    position:absolute;
    bottom:-100px;
    border-radius:50%;
    opacity:0.18;
    animation:float 18s infinite ease-in;
}

.b1{
    width:120px;
    height:120px;
    left:10%;
    background:#FFD166;
}

.b2{
    width:80px;
    height:80px;
    left:30%;
    background:#B8F2E6;
    animation-duration:14s;
}

.b3{
    width:150px;
    height:150px;
    left:55%;
    background:#F7C5E0;
    animation-duration:20s;
}

.b4{
    width:90px;
    height:90px;
    left:75%;
    background:#CDEAC0;
    animation-duration:16s;
}

.b5{
    width:110px;
    height:110px;
    left:90%;
    background:#CDB4DB;
    animation-duration:22s;
}

@keyframes float{
    0%{
        transform:translateY(0);
        opacity:0;
    }

    30%{
        opacity:0.18;
    }

    100%{
        transform:translateY(-1200px);
        opacity:0;
    }
}

/* PORTADA */

.hero-img img{
    border-radius:30px;
}

/* FORMULARIO */

.block-container{
    padding-top:1rem;
    max-width:1200px;
}

.form-box{
    background:rgba(255,255,255,0.88);
    padding:35px;
    border-radius:35px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.05);
    backdrop-filter:blur(10px);
    margin-top:-80px;
    position:relative;
}

/* INPUTS */

.stTextInput input{
    border-radius:18px;
    border:2px solid #EAEAEA;
    padding:14px;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:18px;
}

/* BUTTON */

.stButton button{
    width:100%;
    background:linear-gradient(
        90deg,
        #0F766E,
        #1D9A8C
    ) !important;

    color:white !important;
    border:none !important;
    border-radius:20px !important;
    padding:18px !important;
    font-size:22px !important;
    font-weight:800 !important;
}

/* HISTORIA */

.story-box{
    background:white;
    padding:35px;
    border-radius:30px;
    margin-top:30px;
    border:4px solid #FFD166;
    color:#4A5759;
    font-size:22px;
    line-height:1.8;
    box-shadow:0px 10px 30px rgba(0,0,0,0.05);
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

st.markdown('<div class="hero-img">', unsafe_allow_html=True)
st.image("images/portada.png", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# FORMULARIO
# ---------------------------------------------------

st.markdown('<div class="form-box">', unsafe_allow_html=True)

st.markdown("## ✨ Personalicemos la aventura")

col1, col2 = st.columns(2)

with col1:

    nombre = st.text_input("👦 Nombre del niño")

    edad = st.selectbox(
        "🎂 Edad",
        ["3 años", "4 años", "5 años", "6 años", "7 años"]
    )

    color = st.selectbox(
        "🎨 Color favorito",
        ["Amarillo", "Azul", "Verde", "Rosado"]
    )

with col2:

    emocion = st.selectbox(
        "💛 ¿Cómo se siente?",
        ["Feliz", "Ansioso", "Curioso", "Tímido"]
    )

    actividad = st.selectbox(
        "🧩 Actividad favorita",
        ["Dibujar", "Explorar", "Contar historias"]
    )

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    [
        "Animales",
        "Espacio",
        "Arte",
        "Música",
        "Naturaleza"
    ]
)

# ---------------------------------------------------
# HISTORIAS
# ---------------------------------------------------

historias = {

    "Feliz":
    f"""
    {nombre} despertó sonriendo mientras el Abrazador
    preparaba una aventura llena de colores {color.lower()}.

    Juntos construyeron un mundo mágico donde podían
    {actividad.lower()} rodeados de {", ".join(intereses)}.

    Al final descubrieron que compartir alegría
    hace que los abrazos brillen más fuerte 💛
    """,

    "Ansioso":
    f"""
    {nombre} sentía muchas maripositas en el corazón.

    Entonces apareció Abrazador con una luz mágica color {color.lower()}.

    Mientras caminaban juntos por un bosque tranquilo,
    aprendieron a respirar lento y escuchar sus emociones.

    Poco a poco todo volvió a sentirse seguro ✨
    """,

    "Curioso":
    f"""
    {nombre} tenía mil preguntas sobre el universo.

    Abrazador abrió una puerta secreta hacia un planeta
    lleno de {", ".join(intereses)}.

    Allí descubrieron que imaginar también es una forma
    de aprender y crecer 🚀
    """,

    "Tímido":
    f"""
    {nombre} hablaba muy bajito.

    Entonces Abrazador le regaló una pequeña estrella {color.lower()}.

    Cada vez que sonreía,
    la estrella brillaba más fuerte.

    Y así descubrió que su voz también podía iluminar el mundo 🌈
    """
}

# ---------------------------------------------------
# BOTÓN
# ---------------------------------------------------

if st.button("⭐ Crear mi AbraVentura"):

    historia = historias.get(
        emocion,
        random.choice(list(historias.values()))
    )

    st.markdown(f"""
    <div class="story-box">
    <h2 style="color:#0F766E;">
    📖 Tu AbraVentura
    </h2>

    {historia}
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

