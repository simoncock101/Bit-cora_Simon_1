import streamlit as st


# =========================================================
# CONFIGURACIÓN DE LA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

    /* =========================
       FONDO GENERAL
       ========================= */

    .stApp {
        background: #0f172a;
        color: white;
    }

    /* Ocultar elementos de Streamlit */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #263244;
    }

    section[data-testid="stSidebar"] h2 {
        color: white;
    }

    section[data-testid="stSidebar"] h3 {
        color: #60a5fa;
    }

    section[data-testid="stSidebar"] p {
        color: #cbd5e1;
    }


    /* =========================
       TÍTULO PRINCIPAL
       ========================= */

    .titulo {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 8px;
        color: white;
    }

    .titulo span {
        color: #60a5fa;
    }

    .subtitulo {
        text-align: center;
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 35px;
    }


    /* =========================
       CAJA DEL ENLACE
       ========================= */

    .enlace-principal {
        background: linear-gradient(
            135deg,
            #1d4ed8,
            #2563eb
        );

        padding: 30px;

        border-radius: 20px;

        text-align: center;

        margin-bottom: 40px;

        box-shadow:
            0px 10px 30px rgba(37, 99, 235, 0.25);
    }

    .enlace-principal h3 {
        color: white;
        font-size: 24px;
        margin-bottom: 8px;
    }

    .enlace-principal p {
        color: #dbeafe;
        font-size: 15px;
    }

    .boton-principal {
        display: inline-block;

        background: white;

        color: #1d4ed8 !important;

        padding: 11px 28px;

        border-radius: 10px;

        text-decoration: none !important;

        font-weight: bold;

        margin-top: 8px;
    }

    .boton-principal:hover {
        background: #dbeafe;
    }


    /* =========================
       TÍTULO DE SECCIÓN
       ========================= */

    .seccion {
        color: white;

        font-size: 29px;

        font-weight: 700;

        margin-bottom: 20px;
    }


    /* =========================
       TARJETAS
       ========================= */

    .tarjeta {
        background: #1e293b;

        border: 1px solid #334155;

        border-radius: 20px;

        padding: 25px;

        margin-bottom: 25px;

        min-height: 330px;

        box-shadow:
            0px 8px 20px rgba(0, 0, 0, 0.20);

        transition: all 0.3s ease;
    }

    .tarjeta:hover {
        border-color: #60a5fa;

        transform: translateY(-5px);

        box-shadow:
            0px 15px 30px rgba(37, 99, 235, 0.20);
    }


    /* =========================
       EMOJIS
       ========================= */

    .emoji {
        font-size: 58px;

        text-align: center;

        margin-bottom: 15px;
    }


    /* =========================
       CATEGORÍA
       ========================= */

    .categoria {
        display: block;

        width: fit-content;

        margin: 0 auto 15px auto;

        background: #172554;

        color: #93c5fd;

        padding: 5px 12px;

        border-radius: 20px;

        font-size: 12px;
    }


    /* =========================
       TÍTULO DE TARJETA
       ========================= */

    .tarjeta h3 {
        color: white;

        font-size: 21px;

        text-align: center;

        margin-bottom: 12px;
    }


    /* =========================
       DESCRIPCIÓN
       ========================= */

    .descripcion {
        color: #cbd5e1;

        font-size: 15px;

        line-height: 1.6;

        text-align: center;

        min-height: 75px;
    }


    /* =========================
       BOTONES
       ========================= */

    .boton {
        display: block;

        text-align: center;

        background: #2563eb;

        color: white !important;

        padding: 11px;

        border-radius: 10px;

        text-decoration: none !important;

        font-weight: bold;

        margin-top: 15px;

        transition: 0.2s;
    }

    .boton:hover {
        background: #3b82f6;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;

        color: #64748b;

        padding: 30px;

        margin-top: 30px;

        border-top: 1px solid #1e293b;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Aplicaciones de IA")

    st.markdown("---")

    st.markdown("### Sobre este proyecto")

    st.markdown("""
    La inteligencia artificial permite mejorar la toma de
    decisiones mediante el uso de datos, automatizar tareas
    y desarrollar herramientas capaces de analizar
    información de diferentes maneras.
    """)

    st.markdown("---")

    st.markdown("### 🧠 Aplicaciones")

    st.markdown("""
    👁️ Reconocimiento de objetos

    📷 Análisis de fotos

    🤖 Mi primera app

    ⚽ Fútbol colombiano

    🔊 Texto a voz

    💭 Análisis de sentimientos

    🧍 Análisis de personas
    """)

    st.markdown("---")

    st.markdown("### 📚 Proyecto académico")

    st.write("Diseño Interactivo")

    st.markdown("---")

    st.caption("Explorando las posibilidades de la Inteligencia Artificial.")


# =========================================================
# ENCABEZADO PRINCIPAL
# =========================================================

st.markdown(
    """
    <div class="titulo">
        Aplicaciones de <span>Inteligencia Artificial</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitulo">
        Explora diferentes aplicaciones y experimentos desarrollados con IA
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# ENLACE PRINCIPAL
# =========================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    f"""
    <div class="enlace-principal">

        <h3>🌐 Páginas y ejercicios prácticos</h3>

        <p>
            Encuentra más páginas, ejercicios y proyectos
            relacionados con Inteligencia Artificial.
        </p>

        <a
            href="{url_ia}"
            target="_blank"
            class="boton-principal"
        >
            Explorar página →
        </a>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TÍTULO DE LAS APLICACIONES
# =========================================================

st.markdown(
    """
    <div class="seccion">
        🚀 Mis aplicaciones
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FUNCIÓN PARA CREAR LAS TARJETAS
# =========================================================

def crear_tarjeta(
    emoji,
    titulo,
    categoria,
    descripcion,
    url
):

    st.markdown(
        f"""
        <div class="tarjeta">

            <div class="emoji">
                {emoji}
            </div>

            <div class="categoria">
                {categoria}
            </div>

            <h3>
                {titulo}
            </h3>

            <div class="descripcion">
                {descripcion}
            </div>

            <a
                href="{url}"
                target="_blank"
                class="boton"
            >
                Abrir aplicación →
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CREACIÓN DE LAS COLUMNAS
# =========================================================

col1, col2, col3 = st.columns(
    3,
    gap="large"
)


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    crear_tarjeta(
        "👁️",
        "Reconocimiento de objetos",
        "Visión artificial",
        "Detecta y reconoce diferentes objetos dentro de imágenes utilizando inteligencia artificial.",
        "https://yoloscg.streamlit.app"
    )

    crear_tarjeta(
        "📷",
        "Análisis de fotos",
        "Análisis de imágenes",
        "Permite analizar fotografías utilizando modelos de inteligencia artificial.",
        "https://photoan.streamlit.app"
    )


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    crear_tarjeta(
        "🤖",
        "Mi primera app",
        "Proyecto inicial",
        "La primera aplicación que desarrollé durante la materia utilizando herramientas de inteligencia artificial.",
        "https://app1simon.streamlit.app"
    )

    crear_tarjeta(
        "⚽",
        "Análisis del fútbol colombiano",
        "Datos e IA",
        "Una aplicación que permite interactuar con información relacionada con el fútbol profesional colombiano.",
        "https://chatfpc.streamlit.app"
    )

    crear_tarjeta(
        "🔊",
        "Texto a voz",
        "Voz y audio",
        "Convierte texto escrito en audio utilizando herramientas de inteligencia artificial.",
        "https://imm1profesor01.streamlit.app"
    )


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    crear_tarjeta(
        "💭",
        "Analiza tus sentimientos",
        "Análisis de texto",
        "Analiza textos para identificar información relacionada con sentimientos y emociones.",
        "https://chatpdf-cc.streamlit.app/"
    )

    crear_tarjeta(
        "🧍",
        "Análisis de personas",
        "Visión artificial",
        "Analiza imágenes para identificar si aparecen personas.",
        "https://vision2-gpt4o.streamlit.app/"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        🤖 <b>Aplicaciones de Inteligencia Artificial</b>

        <br><br>

        Proyecto académico · Diseño Interactivo

        <br><br>

        Explorando diferentes posibilidades de la Inteligencia Artificial.

    </div>
    """,
    unsafe_allow_html=True
)


