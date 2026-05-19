st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

/* FONDO GENERAL */
.stApp {
    background: linear-gradient(
        180deg,
        #FFF9F4 0%,
        #FFFDFB 100%
    );
}

/* ------------------------------------------------ */
/* BURBUJAS FLOTANTES */
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
    bottom: -120px;
    border-radius: 50%;
    opacity: 0.18;
    animation: rise 20s infinite ease-in;
}

.b1 {
    width: 120px;
    height: 120px;
    left: 10%;
    background: #FFD166;
    animation-duration: 20s;
}

.b2 {
    width: 80px;
    height: 80px;
    left: 30%;
    background: #BDE0FE;
    animation-duration: 16s;
}

.b3 {
    width: 140px;
    height: 140px;
    left: 55%;
    background: #FFC8DD;
    animation-duration: 24s;
}

.b4 {
    width: 90px;
    height: 90px;
    left: 75%;
    background: #CDEAC0;
    animation-duration: 17s;
}

.b5 {
    width: 100px;
    height: 100px;
    left: 88%;
    background: #D0BDF4;
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
        transform: translateY(-1200px);
        opacity: 0;
    }
}

/* ------------------------------------------------ */
/* HERO */
/* ------------------------------------------------ */

.hero {
    background: rgba(255,255,255,0.75);
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

/* ------------------------------------------------ */
/* FORMULARIO */
/* ------------------------------------------------ */

.form-card {
    background: rgba(255,255,255,0.82);
    padding: 35px;
    border-radius: 35px;
    box-shadow: 0px 8px 35px rgba(0,0,0,0.05);
    backdrop-filter: blur(12px);
}

/* TITULOS */

.section-title {
    font-size: 42px;
    font-weight: 800;
    color: #0F766E;
}

.section-sub {
    color: #52796F;
    font-size: 20px;
    margin-bottom: 30px;
}

/* ------------------------------------------------ */
/* LABELS */
/* ------------------------------------------------ */

label,
.stSelectbox label,
.stMultiSelect label,
.stTextInput label {
    color: #0F766E !important;
    font-weight: 700 !important;
    font-size: 18px !important;
}

/* ------------------------------------------------ */
/* INPUTS */
/* ------------------------------------------------ */

.stTextInput input {
    background-color: #EAF6FF !important;
    color: #0F172A !important;
    border-radius: 18px !important;
    border: 2px solid #BDE0FE !important;
    padding: 12px !important;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #EAF6FF !important;
    border-radius: 18px !important;
    border: 2px solid #BDE0FE !important;
}

.stMultiSelect div[data-baseweb="select"] {
    background-color: #EAF6FF !important;
    border-radius: 18px !important;
    border: 2px solid #BDE0FE !important;
}

/* TEXTO DENTRO INPUTS */

input, textarea {
    color: #0F172A !important;
}

/* ------------------------------------------------ */
/* BOTÓN */
/* ------------------------------------------------ */

.stButton button {
    background: linear-gradient(
        90deg,
        #5EC8FF,
        #7ED7C1
    ) !important;

    color: white !important;
    border-radius: 20px !important;
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

/* ------------------------------------------------ */
/* STORY BOX */
/* ------------------------------------------------ */

.story-box {
    background: white;
    border-radius: 30px;
    padding: 40px;
    margin-top: 30px;
    border: 4px solid #FFD166;
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

