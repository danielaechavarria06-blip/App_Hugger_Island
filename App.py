# app.py
# AbraVenturas ✨
# Hugger Island inspired UI

import streamlit as st
import html as html_module
import json
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
# HISTORIAS — 3 variantes por emoción, coherentes
# Plantillas: {nombre}, {animal}, {color}, {actividad}, {intereses}
# ---------------------------------------------------

historias = {

    "Ansioso": [
        (
            "{nombre} sentía muchas maripositas en la barriga antes de dormir.\n"
            "Entonces apareció Abrazador con una linterna mágica color {color}.\n\n"
            "—Las emociones no son monstruos —dijo Abrazador—,\n"
            "son mensajes que quieren abrazos.\n\n"
            "Juntos caminaron por un bosque brillante donde un {animal} mágico\n"
            "les enseñó a respirar despacio.\n\n"
            "Al final, {nombre} respiró profundo y descubrió que podía\n"
            "sentirse valiente incluso cuando tenía miedo. 💛"
        ),
        (
            "Una noche, {nombre} no podía dormir.\n"
            "Su corazón latía muy rápido pensando en el día siguiente.\n\n"
            "Abrazador apareció montado en un {animal} brillante\n"
            "y le dijo: —Cada estrella del cielo es un abrazo esperándote.\n\n"
            "Juntos contaron estrellas de color {color}\n"
            "hasta que {nombre} se quedó dormido sonriendo,\n"
            "soñando con {intereses}. ✨"
        ),
        (
            "{nombre} amaba {actividad}, pero a veces el miedo llegaba sin avisar.\n\n"
            "Abrazador llegó una tarde con un regalo especial:\n"
            "una piedrita mágica color {color}.\n\n"
            "—Cuando sientas nervios, apriétala fuerte —dijo Abrazador—.\n"
            "Ella guardará toda tu valentía.\n\n"
            "Desde ese día, {nombre} supo que era más valiente de lo que creía. 🌟"
        ),
    ],

    "Feliz": [
        (
            "{nombre} despertó lleno de energía y sonrisas.\n"
            "Abrazador llegó saltando entre estrellas color {color}.\n\n"
            "Juntos construyeron una ciudad de almohadas\n"
            "con la ayuda de un {animal} muy juguetón.\n\n"
            "Cada risa hacía aparecer nuevas luces en el cielo.\n\n"
            "Antes de dormir, {nombre} entendió que compartir su alegría\n"
            "hace felices a los demás también. ✨"
        ),
        (
            "Hoy {nombre} se despertó cantando.\n"
            "Todo brillaba más: el sol, los colores y hasta su {animal} favorito.\n\n"
            "Abrazador llegó con una mochila llena de {intereses}\n"
            "y juntos pasaron el día disfrutando de {actividad}.\n\n"
            "Al caer la tarde, {nombre} guardó ese momento en su corazón\n"
            "como el más bonito del año. 🌈"
        ),
        (
            "{nombre} descubrió algo increíble mientras hacía {actividad}:\n"
            "que cuando uno está feliz, todo parece más fácil.\n\n"
            "Abrazador apareció con un {animal} color {color}\n"
            "y juntos exploraron un mundo lleno de {intereses}.\n\n"
            "Al final del día, {nombre} supo que la felicidad\n"
            "es el mejor superpoder del mundo. 💛"
        ),
    ],

    "Tímido": [
        (
            "{nombre} quería jugar,\n"
            "pero las palabras se escondían dentro de él.\n\n"
            "Entonces Abrazador le regaló una pequeña estrella color {color}.\n\n"
            "Cada vez que {nombre} sonreía,\n"
            "la estrella brillaba más fuerte.\n\n"
            "Poco a poco comenzó a hablar y a jugar con un {animal} muy amigable,\n"
            "descubriendo que ser tímido también puede ser hermoso. 🌈"
        ),
        (
            "{nombre} era experto en {actividad}, pero nunca lo mostraba.\n\n"
            "Un día, Abrazador llegó con pinturas color {color}\n"
            "y le dijo: —Tu forma de ver el mundo es única y especial.\n\n"
            "Ese día, {nombre} mostró su talento por primera vez\n"
            "y descubrió que había muchas personas que lo admiraban. ✨"
        ),
        (
            "En el mundo de {nombre} había cosas que amaba en silencio:\n"
            "{intereses} y pasar horas haciendo {actividad}.\n\n"
            "Un día, un {animal} muy curioso se sentó a su lado\n"
            "y Abrazador susurró: —No necesitas muchas palabras\n"
            "para conectar con alguien, {nombre}.\n\n"
            "A veces una sonrisa lo dice todo. 💛"
        ),
    ],

    "Curioso": [
        (
            "{nombre} tenía mil preguntas en su cabeza.\n\n"
            "Abrazador lo llevó a un planeta lleno de {intereses},\n"
            "con puertas secretas y un {animal} que hablaba.\n\n"
            "Allí {nombre} descubrió que hacer preguntas\n"
            "es la forma más mágica de explorar el mundo.\n\n"
            "Desde ese día, nunca dejó de imaginar aventuras nuevas. 🚀"
        ),
        (
            "Un día, {nombre} encontró una puerta color {color}\n"
            "que nadie más podía ver.\n\n"
            "Abrazador estaba del otro lado con un mapa lleno de {intereses}.\n\n"
            "Juntos descubrieron que {actividad} era la llave\n"
            "para abrir todos los secretos del universo.\n\n"
            "{nombre} regresó a casa con el corazón lleno de maravillas. 🌟"
        ),
        (
            "{nombre} siempre se preguntaba cómo funcionaban las cosas.\n\n"
            "Un {animal} muy sabio, amigo de Abrazador,\n"
            "le enseñó que cada pregunta abre una puerta nueva.\n\n"
            "Juntos exploraron montañas de {intereses}\n"
            "y {nombre} aprendió que la curiosidad\n"
            "es el superpoder más grande de todos. 💛"
        ),
    ],

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
    background: #FFF9F4;
}

header { visibility: hidden; }
footer { visibility: hidden; }

/* ---------- BOLITAS FONDO ---------- */
.bubbles {
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: 0;
    overflow: hidden;
    top: 0;
    left: 0;
    pointer-events: none;
}

.bubble {
    position: absolute;
    bottom: -160px;
    border-radius: 50%;
    animation: rise linear infinite;
}

.b1  { width:80px;  height:80px;  left:5%;   background:#F7D66B; opacity:0.25; animation-duration:18s; animation-delay:0s;   }
.b2  { width:50px;  height:50px;  left:15%;  background:#A8DAD5; opacity:0.30; animation-duration:14s; animation-delay:3s;   }
.b3  { width:110px; height:110px; left:25%;  background:#F7C5E0; opacity:0.20; animation-duration:22s; animation-delay:1s;   }
.b4  { width:65px;  height:65px;  left:38%;  background:#C7E59B; opacity:0.28; animation-duration:16s; animation-delay:5s;   }
.b5  { width:90px;  height:90px;  left:50%;  background:#BFA2DB; opacity:0.22; animation-duration:20s; animation-delay:2s;   }
.b6  { width:55px;  height:55px;  left:62%;  background:#F7D66B; opacity:0.30; animation-duration:15s; animation-delay:7s;   }
.b7  { width:100px; height:100px; left:72%;  background:#A8DAD5; opacity:0.20; animation-duration:24s; animation-delay:0s;   }
.b8  { width:70px;  height:70px;  left:82%;  background:#F7C5E0; opacity:0.26; animation-duration:17s; animation-delay:4s;   }
.b9  { width:45px;  height:45px;  left:90%;  background:#C7E59B; opacity:0.32; animation-duration:13s; animation-delay:6s;   }
.b10 { width:85px;  height:85px;  left:95%;  background:#BFA2DB; opacity:0.22; animation-duration:21s; animation-delay:9s;   }

@keyframes rise {
    0%   { transform: translateY(0)        scale(1);    opacity: 0;    }
    10%  {                                              opacity: 0.28; }
    90%  {                                              opacity: 0.20; }
    100% { transform: translateY(-110vh)   scale(1.1); opacity: 0;    }
}

/* ---------- PORTADA ---------- */
.portada-container img {
    border-radius: 0px 0px 40px 40px;
}

/* ---------- FORM CARD ---------- */
.form-card {
    background: rgba(255,255,255,0.88);
    padding: 45px;
    border-radius: 40px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.06);
    backdrop-filter: blur(14px);
    position: relative;
    z-index: 1;
}

.section-title {
    font-size: 48px;
    font-weight: 800;
    color: #0F766E;
    text-align: center;
    margin-bottom: 8px;
}

.section-sub {
    color: #4A5759;
    font-size: 20px;
    margin-bottom: 30px;
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
    font-size: 22px !important;
    font-weight: 700 !important;
    border: none !important;
    width: 100%;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* ---------- STORY BOX ---------- */
.story-box {
    background: white;
    border-radius: 35px;
    padding: 45px 50px;
    margin-top: 30px;
    border: 4px solid #F7D66B;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.04);
    position: relative;
    z-index: 1;
}

.story-title {
    color: #0F766E;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 28px;
    text-align: center;
}

.story-paragraph {
    color: #374151;
    font-size: 22px;
    line-height: 1.9;
    margin-bottom: 14px;
    font-weight: 600;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    margin-top: 60px;
    color: #52796F;
    font-size: 18px;
    padding-bottom: 30px;
    position: relative;
    z-index: 1;
}

</style>

<div class="bubbles">
    <div class="bubble b1"></div>
    <div class="bubble b2"></div>
    <div class="bubble b3"></div>
    <div class="bubble b4"></div>
    <div class="bubble b5"></div>
    <div class="bubble b6"></div>
    <div class="bubble b7"></div>
    <div class="bubble b8"></div>
    <div class="bubble b9"></div>
    <div class="bubble b10"></div>
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
        variantes = historias.get(emocion, historias["Feliz"])
        plantilla = random.choice(variantes)

        intereses_texto = ", ".join(intereses) if intereses else "aventuras mágicas"

        historia_generada = plantilla.format(
            nombre=nombre.strip(),
            color=color_favorito.lower(),
            animal=animal_favorito.lower(),
            actividad=tipo_actividad.lower(),
            intereses=intereses_texto.lower()
        )

        introduccion = f"Hola {nombre.strip()} 💛\n\nHoy vivirás una aventura muy especial.\n\n"
        texto_completo = introduccion + historia_generada.strip() + "\n\n🌈 Fin de la AbraVentura."

        st.session_state["historia_texto"]  = texto_completo
        st.session_state["historia_nombre"] = nombre.strip()

# ---------------------------------------------------
# MOSTRAR HISTORIA
# ---------------------------------------------------

if "historia_texto" in st.session_state:

    texto        = st.session_state["historia_texto"]
    nombre_nino  = st.session_state["historia_nombre"]
    nombre_safe  = html_module.escape(nombre_nino)

    # --- Tarjeta única con título + párrafos ---
    parrafos_html = ""
    for linea in texto.split("\n"):
        if linea.strip():
            parrafos_html += f'<p class="story-paragraph">{html_module.escape(linea)}</p>\n'

    st.markdown(f"""
<div class="story-box">
    <div class="story-title">📖 La AbraVentura de {nombre_safe}</div>
    {parrafos_html}
</div>
""", unsafe_allow_html=True)

    # ---------------------------------------------------
    # AUDIOLIBRO
    # ---------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    texto_js = json.dumps(texto)

    audio_html = f"""
    <div style="
        background: white;
        border-radius: 30px;
        padding: 28px 40px;
        border: 3px solid #A8DAD5;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
        text-align: center;
        font-family: 'Nunito', sans-serif;
        position: relative;
        z-index: 1;
    ">
        <p style="font-size:20px; color:#0F766E; font-weight:800; margin-bottom:18px;">
            🎧 Escuchar la historia de {nombre_safe}
        </p>

        <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">

            <button onclick="leerHistoria()" style="
                background: linear-gradient(90deg,#56CFE1,#72DDF7);
                color: white; border: none; border-radius: 20px;
                padding: 12px 26px; font-size:17px; font-weight:700;
                cursor: pointer; font-family:'Nunito',sans-serif;
            ">▶️ Reproducir</button>

            <button onclick="pausarHistoria()" style="
                background: #F7D66B; color: #374151;
                border: none; border-radius: 20px;
                padding: 12px 26px; font-size:17px; font-weight:700;
                cursor: pointer; font-family:'Nunito',sans-serif;
            ">⏸️ Pausar</button>

            <button onclick="detenerHistoria()" style="
                background: #F7C5E0; color: #374151;
                border: none; border-radius: 20px;
                padding: 12px 26px; font-size:17px; font-weight:700;
                cursor: pointer; font-family:'Nunito',sans-serif;
            ">⏹️ Detener</button>

        </div>

        <p id="estado-audio" style="
            margin-top:16px; font-size:15px;
            color:#52796F; font-weight:700; min-height:22px;
        "></p>

    </div>

    <script>
        const textoHistoria = {texto_js};
        const sint = window.speechSynthesis;
        let utt = null;

        function vozEspanol() {{
            const voces = sint.getVoices();
            return (
                voces.find(v => v.lang === 'es-CO') ||
                voces.find(v => v.lang === 'es-MX') ||
                voces.find(v => v.lang === 'es-ES') ||
                voces.find(v => v.lang.startsWith('es'))
            );
        }}

        function leerHistoria() {{
            if (sint.speaking) {{
                if (sint.paused) {{ sint.resume(); estado('▶️ Reproduciendo...'); }}
                return;
            }}
            utt = new SpeechSynthesisUtterance(textoHistoria);
            utt.rate   = 0.88;
            utt.pitch  = 1.1;
            utt.volume = 1;
            const v = vozEspanol();
            if (v) utt.voice = v;
            utt.onstart = () => estado('▶️ Reproduciendo...');
            utt.onend   = () => estado('✅ Historia terminada 💛');
            utt.onerror = () => estado('⚠️ Error al reproducir');
            sint.speak(utt);
        }}

        function pausarHistoria() {{
            if (sint.speaking && !sint.paused) {{ sint.pause(); estado('⏸️ Pausado'); }}
        }}

        function detenerHistoria() {{
            sint.cancel(); estado('⏹️ Detenido');
        }}

        function estado(msg) {{
            document.getElementById('estado-audio').innerText = msg;
        }}

        if (sint.onvoiceschanged !== undefined) {{
            sint.onvoiceschanged = vozEspanol;
        }}
    </script>
    """

    st.components.v1.html(audio_html, height=200)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
💛 Hugger Island • Abraza • Conecta • Transforma
</div>
""", unsafe_allow_html=True)

