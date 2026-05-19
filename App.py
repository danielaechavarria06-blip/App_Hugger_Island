# ---------------- PORTADA ----------------

if os.path.exists("portada.png"):
    st.image("portada.png", use_container_width=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="hero-title">
💛 AbraVenturas
</div>

<div class="hero-sub">
Historias que abrazan la imaginación ✨
</div>
""", unsafe_allow_html=True)

# ---------------- FORMULARIO ----------------

st.markdown("""
<div class="form-card">
<h2>✨ Personalicemos la aventura</h2>
<p>Cuéntanos un poco sobre tu pequeño lector 💛</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CAMPOS ----------------

col1, col2 = st.columns(2)

with col1:

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

with col2:

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

# ---------------- INTERESES ----------------

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

# ---------------- BOTÓN ----------------

if st.button("⭐ Crear mi AbraVentura"):

    historia = f"""
    ## 🌈 La aventura de {nombre}

    Un día, {nombre} salió a explorar un mundo lleno de colores {color_favorito.lower()}.

    Mientras caminaba, apareció un personaje mágico llamado **Abrazador** 💛

    Juntos descubrieron un bosque encantado lleno de:
    {", ".join(intereses) if intereses else "aventuras increíbles"}.

    Aunque a veces {nombre} se sentía {emocion.lower()},
    aprendió que cada emoción tiene un superpoder especial ✨

    Después de jugar y {tipo_actividad.lower()},
    Abrazador le dio un abrazo gigante y le recordó:

    > "Tu imaginación puede crear mundos maravillosos."

    FIN 🌈
    """

    st.markdown(
        f"""
        <div class="story-box">
        {historia}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- GALERÍA ----------------

st.markdown("## 🌈 Tus abrazadores")

col3, col4, col5 = st.columns(3)

with col3:
    if os.path.exists("Abrazador_Imagen1.png"):
        st.image("Abrazador_Imagen1.png")

with col4:
    if os.path.exists("Abrazador_Imagen2.png"):
        st.image("Abrazador_Imagen2.png")

with col5:
    if os.path.exists("Abrazador_Imagen3.png"):
        st.image("Abrazador_Imagen3.png")
        
