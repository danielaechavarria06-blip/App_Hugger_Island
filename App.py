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
# HISTORIAS — 3 variantes por emoción
# {nombre}, {animal}, {color}, {actividad}, {intereses}
# ---------------------------------------------------

historias = {

    "Ansioso": [
        """
{nombre} sentía muchas maripositas en la barriga antes de dormir.
Entonces apareció Abrazador con una linterna mágica color {color}.

—Las emociones no son monstruos —dijo Abrazador—,
son mensajes que quieren abrazos.

Juntos caminaron por un bosque brillante donde un {animal} mágico
les enseñó a respirar despacio.

Al final, {nombre} respiró profundo y descubrió que podía
sentirse valiente incluso cuando tenía miedo. 💛
        """,
        """
Una noche, {nombre} no podía dormir.
Su corazón latía muy rápido pensando en el día siguiente.

Abrazador apareció montado en un {animal} brillante
y le dijo: —Cada estrella del cielo es un abrazo esperándote.

Juntos contaron estrellas hasta que {nombre}
se quedó dormido sonriendo, soñando con {intereses}. ✨
        """,
        """
{nombre} amaba {actividad}, pero a veces el miedo llegaba sin avisar.

Abrazador llegó con un regalo especial: una piedrita color {color}.

—Cuando sientas nervios, aprieta esta piedrita —dijo Abrazador—.
Ella guardará toda tu valentía.

Desde ese día, {nombre} supo que era más valiente de lo que creía. 🌟
        """
    ],

    "Feliz": [
        """
{nombre} despertó lleno de energía y sonrisas.
Abrazador llegó saltando entre estrellas color {color}.

Juntos construyeron una ciudad de almohadas,
dibujos y canciones mágicas con un {animal} bailarín.

Cada risa hacía aparecer nuevas luces en el cielo.

Antes de dormir, {nombre} entendió que compartir su alegría
hacía felices a los demás también. ✨
        """,
        """
Hoy era un día especial para {nombre}.

Todo lo que tocaba se volvía magia: los colores brillaban más,
los sonidos eran música y hasta su {animal} favorito parecía bailar.

Abrazador le susurró: —La felicidad que sientes es un regalo,
compártela con alguien hoy.

Y {nombre} lo hizo, disfrutando de {actividad} con sus amigos. 🌈
        """,
        """
{nombre} descubrió algo increíble mientras hacía {actividad}:
que cuando uno está feliz, todo parece más fácil.

Abrazador apareció con un {animal} de color {color}
y juntos exploraron un mundo lleno de {intereses}.

Al final del día, {nombre} guardó ese momento en su corazón
como un tesoro para siempre. 💛
        """
    ],

    "Tímido": [
        """
{nombre} quería jugar,
pero las palabras se escondían dentro de él.

Entonces Abrazador le regaló una pequeña estrella color {color}.

Cada vez que {nombre} sonreía,
la estrella brillaba más fuerte.

Poco a poco comenzó a hablar, jugar con su {animal} favorito
y descubrir que ser tímido también puede ser hermoso. 🌈
        """,
        """
En el jardín de {nombre} había un lugar secreto
donde solo iba cuando quería estar solo.

Un día, Abrazador llegó con un {animal} muy curioso
que amaba {intereses} igual que {nombre}.

—No necesitas hablar mucho para conectar —dijo Abrazador—.
A veces una sonrisa lo dice todo. 💛
        """,
        """
{nombre} era experto en {actividad}, pero nunca lo mostraba.

Abrazador llegó una tarde con pintura color {color}
y le dijo: —Tu forma de ver el mundo es única.

Ese día, {nombre} mostró su talento por primera vez
y descubrió que había personas que lo admiraban mucho. ✨
        """
    ],

    "Curioso": [
        """
{nombre} tenía mil preguntas en su cabeza.

Abrazador lo llevó a un planeta lleno de {intereses},
animales parlantes como su {animal} favorito y puertas secretas.

Allí descubrió que hacer preguntas
era una forma mágica de explorar el mundo.

Desde ese día, {nombre} nunca dejó de imaginar aventuras nuevas. 🚀
        """,
        """
Un día, {nombre} encontró una puerta color {color}
que nadie más podía ver.

Abrazador estaba del otro lado con un mapa lleno de {intereses}.

Juntos viajaron por mundos donde {actividad} era la llave
para abrir todos los secretos del universo.

{nombre} regresó a casa con el corazón lleno de maravillas. 🌟
        """,
        """
{nombre} siempre se preguntaba cómo funcionaban las cosas.

Un {animal} muy sabio y amigo de Abrazador
le enseñó que cada pregunta es una aventura nueva.

Juntos exploraron montañas de {intereses}
y {nombre} aprendió que la curiosidad es el superpoder más grande. 💛
        """
    ]

}

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #FFF9F4 0%, #FFFDFB 100%);
}

header { visibility: hidden; }
footer { visibility: hidden; }

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

.b1 { width: 120px; height: 120px; left: 10%; background: #F7D66B; animation-duration: 20s; }
.b2 { width: 90px;  height: 90px;  left: 30%; background: #A8DAD5; animation-duration: 17s; }
.b3 { width: 140px; height: 140px; left: 55%; background: #F7C5E0; animation-duration: 24s; }
.b4 { width: 100px; height: 100px; left: 75%; background: #C7E59B; animation-duration: 19s; }
.b5 { width: 110px; height: 110px; left: 88%; background: #BFA2DB; animation-duration: 21s; }

@keyframes rise {
    0%   { transform: translateY(0px);     opacity: 0;    }
    30%  {                                 opacity: 0.18; }
    100% { transform: translateY(-1400px); opacity: 0;    }
}

.portada-container img {
    border-radius: 0px 0px 40px 40px;
}

.form-card {
    background: rgba(255,255,255,0.82);
    padding: 45px;
    border-radius: 40px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.05);
    backdrop-filter: blur(12px);
    margin-top: -40px;
}

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

label, p, span {
    color: #1F2937 !important;
    font-weight: 700 !important;
}

.stTextInput input {
    background: #DFF4FF !important;
    color: #1F2937 !important;
    border-radius: 18px !important;
    border: none !important;
    padding: 12px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #DFF4FF !important;
    color: #1F2937 !important;
    border-radius: 18px !important;
    border: none !important;
}

.stMultiSelect div[data-baseweb="select"] > div {
    background: #DFF4FF !important;
    color: #1F2937 !important;
    border-radius: 18px !important;
    border: none !important;
}

.stButton button {
    background: linear-gradient(90deg, #56CFE1, #72DDF7) !important;
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

.story-box {
    background: white;
    border-radius: 35px;
    padding: 45px;
    margin-top: 35px;
    border: 4px solid #F7D66B;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.04);
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

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# FORM
# ---------------------------------------------------

st.markdown("""
<div class="form-card">
<div class="section-title">✨ Personalicemos la aventura</div>
<div class="section-sub">Cuéntanos un poco sobre tu pequeño lector 💛</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    nombre = st.text_input("👦 Nombre del niño")
    edad = st.selectbox("🎂 Edad", ["3 años","4 años","5 años","6 años","7 años","8 años"])
    color_favorito = st.selectbox("🎨 Color favorito", ["Amarillo","Azul","Verde","Rosado","Morado","Naranja"])
    animal_favorito = st.selectbox("🐻 Animal favorito", ["Perro","Gato","Conejo","Delfín","León","Panda","Tortuga","Dragón"])

with c2:
    emocion = st.selectbox("💛 ¿Cómo se siente últimamente?", ["Feliz","Tímido","Ansioso","Curioso"])
    tipo_actividad = st.selectbox("🧩 Actividad favorita", ["Dibujar","Jugar","Contar historias","Explorar"])

intereses = st.multiselect(
    "🌟 Intereses favoritos",
    ["Animales","Espacio","Naturaleza","Arte","Música","Aventuras"]
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
        # Elegir una variante aleatoria según emoción
        variantes = historias.get(emocion, historias["Feliz"])
        plantilla = random.choice(variantes)

        intereses_texto = ", ".join(intereses) if intereses else "aventuras mágicas"

        # Rellenar plantilla con los datos del niño
        historia_final = plantilla.format(
            nombre=nombre.strip(),
            edad=edad,
            color=color_favorito.lower(),
            animal=animal_favorito.lower(),
            actividad=tipo_actividad.lower(),
            intereses=intereses_texto.lower()
        )

        introduccion = (
            f"Hola {nombre.strip()} 💛\n\n"
            f"Hoy vivirás una aventura muy especial.\n\n"
        )

        texto_completo = introduccion + historia_final.strip() + "\n\n🌈 Fin de la AbraVentura."

        # Guardar en session_state para el audiolibro
        st.session_state["historia_texto"] = texto_completo
        st.session_state["historia_nombre"] = nombre.strip()

# ---------------------------------------------------
# MOSTRAR HISTORIA + AUDIOLIBRO
# ---------------------------------------------------

if "historia_texto" in st.session_state:

    texto = st.session_state["historia_texto"]
    nombre_nino = st.session_state["historia_nombre"]

    # Mostrar historia en tarjeta limpia (solo texto, sin HTML)
    st.markdown('<div class="story-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="story-title">📖 La AbraVentura de {html_module.escape(nombre_nino)}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Usar st.write para el texto — sin riesgo de HTML injection
    st.markdown('<div class="story-box">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="story-title">📖 La AbraVentura de {html_module.escape(nombre_nino)}</div>',
        unsafe_allow_html=True
    )
    # Texto con st.write para renderizado limpio
    for parrafo in texto.split("\n"):
        if parrafo.strip():
            st.markdown(
                f'<p class="story-text">{html_module.escape(parrafo)}</p>',
                unsafe_allow_html=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------------------------------------------
    # AUDIOLIBRO con Web Speech API
    # ---------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎧 Escuchar la historia")

    # Pasar el texto al componente JS de forma segura
    import json
    texto_js = json.dumps(texto)

    audio_html = f"""
    <div style="
        background: white;
        border-radius: 30px;
        padding: 30px 40px;
        border: 3px solid #A8DAD5;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
        text-align: center;
        font-family: 'Nunito', sans-serif;
    ">
        <p style="font-size: 20px; color: #0F766E; font-weight: 700; margin-bottom: 20px;">
            🔊 Audiolibro de {html_module.escape(nombre_nino)}
        </p>

        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">

            <button onclick="leerHistoria()" style="
                background: linear-gradient(90deg, #56CFE1, #72DDF7);
                color: white;
                border: none;
                border-radius: 20px;
                padding: 14px 28px;
                font-size: 18px;
                font-weight: 700;
                cursor: pointer;
                font-family: 'Nunito', sans-serif;
            ">▶️ Reproducir</button>

            <button onclick="pausarHistoria()" style="
                background: #F7D66B;
                color: #374151;
                border: none;
                border-radius: 20px;
                padding: 14px 28px;
                font-size: 18px;
                font-weight: 700;
                cursor: pointer;
                font-family: 'Nunito', sans-serif;
            ">⏸️ Pausar</button>

            <button onclick="detenerHistoria()" style="
                background: #F7C5E0;
                color: #374151;
                border: none;
                border-radius: 20px;
                padding: 14px 28px;
                font-size: 18px;
                font-weight: 700;
                cursor: pointer;
                font-family: 'Nunito', sans-serif;
            ">⏹️ Detener</button>

        </div>

        <p id="estado-audio" style="
            margin-top: 18px;
            font-size: 16px;
            color: #52796F;
            font-weight: 600;
            min-height: 24px;
        "></p>

    </div>

    <script>
        const textoHistoria = {texto_js};
        let utterance = null;
        let sintetizador = window.speechSynthesis;

        function obtenerVozEspanol() {{
            const voces = sintetizador.getVoices();
            return (
                voces.find(v => v.lang === 'es-CO') ||
                voces.find(v => v.lang === 'es-MX') ||
                voces.find(v => v.lang === 'es-ES') ||
                voces.find(v => v.lang.startsWith('es'))
            );
        }}

        function leerHistoria() {{
            if (sintetizador.speaking) {{
                if (sintetizador.paused) {{
                    sintetizador.resume();
                    document.getElementById('estado-audio').innerText = '▶️ Reproduciendo...';
                }}
                return;
            }}

            utterance = new SpeechSynthesisUtterance(textoHistoria);
            utterance.rate = 0.88;
            utterance.pitch = 1.1;
            utterance.volume = 1;

            const voz = obtenerVozEspanol();
            if (voz) utterance.voice = voz;

            utterance.onstart = () => {{
                document.getElementById('estado-audio').innerText = '▶️ Reproduciendo...';
            }};

            utterance.onend = () => {{
                document.getElementById('estado-audio').innerText = '✅ Historia terminada 💛';
            }};

            utterance.onerror = (e) => {{
                document.getElementById('estado-audio').innerText = '⚠️ Error al reproducir';
            }};

            sintetizador.speak(utterance);
        }}

        function pausarHistoria() {{
            if (sintetizador.speaking && !sintetizador.paused) {{
                sintetizador.pause();
                document.getElementById('estado-audio').innerText = '⏸️ Pausado';
            }}
        }}

        function detenerHistoria() {{
            sintetizador.cancel();
            document.getElementById('estado-audio').innerText = '⏹️ Detenido';
        }}

        // Cargar voces (necesario en algunos navegadores)
        if (sintetizador.onvoiceschanged !== undefined) {{
            sintetizador.onvoiceschanged = obtenerVozEspanol;
        }}
    </script>
    """

    st.components.v1.html(audio_html, height=220)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
💛 Hugger Island • Abraza • Conecta • Transforma
</div>
""", unsafe_allow_html=True)

