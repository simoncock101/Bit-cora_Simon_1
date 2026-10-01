import streamlit as st


# =========================================================
# CONFIGURACIÓN
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

.stApp {
    background-color: #0f172a;
    color: white;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #111827;
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


/* TÍTULO PRINCIPAL */

.titulo {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 5px;
    color: white;
}

.azul {
    color: #60a5fa;
}


/* NOMBRE */

.nombre {
    text-align: center;
    color: #e2e8f0;
    font-size: 22px;
    font-weight: 600;
    margin-top: 5px;
    margin-bottom: 8px;
}


/* SUBTÍTULO */

.subtitulo {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 35px;
}


/* CAJA PRINCIPAL */

.caja-principal {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
}

.caja-titulo {
    color: white;
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 12px;
}

.caja-texto {
    color: #dbeafe;
    font-size: 16px;
    margin-bottom: 20px;
}

.boton-principal {
    display: inline-block;
    background-color: white;
    color: #1d4ed8 !important;
    padding: 11px 25px;
    border-radius: 10px;
    text-decoration: none !important;
    font-weight: bold;
}

.boton-principal:hover {
    background-color: #dbeafe;
}


/* TÍTULO DE SECCIÓN */

.titulo-seccion {
    color: white;
    font-size: 29px;
    font-weight: bold;
    margin-bottom: 20px;
}


/* TARJETAS */

.tarjeta {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 25px;
    min-height: 330px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.20);
    transition: all 0.3s ease;
}

.tarjeta:hover {
    border-color: #60a5fa;
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(37, 99, 235, 0.20);
}


/* EMOJI */

.tarjeta-emoji {
    font-size: 60px;
    margin-bottom: 12px;
}


/* CATEGORÍA */

.tarjeta-categoria {
    display: inline-block;
    background-color: #172554;
    color: #93c5fd;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    margin-bottom: 12px;
}


/* TÍTULO TARJETA */

.tarjeta-titulo {
    color: white;
    font-size: 21px;
    font-weight: bold;
    margin-bottom: 12px;
}


/* DESCRIPCIÓN */

.tarjeta-texto {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.6;
    min-height: 75px;
}


/* BOTÓN */

.boton {
    display: block;
    background-color: #2563eb;
    color: white !important;
    padding: 11px;
    border-radius: 10px;
    text-decoration: none !important;
    font-weight: bold;
    margin-top: 18px;
    transition: 0.2s;
}

.boton:hover {
    background-color: #3b82f6;
}


/* FOOTER */

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
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🤖 Aplicaciones de IA")

    st.markdown("---")

    st.markdown("### Sobre este proyecto")

    st.write(
        "La inteligencia artificial permite mejorar la toma "
        "de decisiones mediante el uso de datos, automatizar "
        "tareas y desarrollar herramientas capaces de analizar "
        "información de diferentes maneras."
    )

    st.markdown("---")

    st.markdown("### 🧠 Aplicaciones")

    st.write("👁️ Reconocimiento de objetos")
    st.write("📷 Análisis de fotos")
    st.write("🤖 Mi primera app")
    st.write("⚽ Fútbol colombiano")
    st.write("🔊 Texto a voz")
    st.write("💭 Análisis de sentimientos")
    st.write("🧍 Análisis de personas")

    st.markdown("---")

    st.markdown("### 📚 Proyecto académico")

    st.write("Diseño Interactivo")

    st.markdown("---")

    st.caption("Explorando las posibilidades de la Inteligencia Artificial.")


# =========================================================
# ENCABEZADO
# =========================================================

st.markdown(
    '<div class="titulo">Aplicaciones de <span class="azul">Inteligencia Artificial</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nombre">Simon Cock García</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Explora diferentes aplicaciones y experimentos desarrollados con IA</div>',
    unsafe_allow_html=True
)


# =========================================================
# ENLACE PRINCIPAL
# =========================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    '<div class="caja-principal">'
    '<div class="caja-titulo">🌐 Páginas y ejercicios prácticos</div>'
    '<div class="caja-texto">'
    'Encuentra más páginas, ejercicios y proyectos relacionados '
    'con Inteligencia Artificial.'
    '</div>'
    '<a href="' + url_ia + '" target="_blank" class="boton-principal">'
    'Explorar página →'
    '</a>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# TÍTULO DE LAS APLICACIONES
# =========================================================

st.markdown(
    '<div class="titulo-seccion">🚀 Mis aplicaciones</div>',
    unsafe_allow_html=True
)


# =========================================================
# FUNCIÓN PARA CREAR TARJETAS
# =========================================================

def crear_tarjeta(emoji, titulo, categoria, descripcion, url):

    html = (
        '<div class="tarjeta">'
        '<div class="tarjeta-emoji">' + emoji + '</div>'
        '<div class="tarjeta-categoria">' + categoria + '</div>'
        '<div class="tarjeta-titulo">' + titulo + '</div>'
        '<div class="tarjeta-texto">' + descripcion + '</div>'
        '<a href="' + url + '" target="_blank" class="boton">'
        'Abrir aplicación →'
        '</a>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# =========================================================
# COLUMNAS
# =========================================================

col1, col2, col3 = st.columns(3, gap="large")


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
    '<div class="footer">'
    '🤖 <b>Aplicaciones de Inteligencia Artificial</b>'
    '<br><br>'
    'Simon Cock García · Diseño Interactivo'
    '<br><br>'
    'Explorando diferentes posibilidades de la Inteligencia Artificial.'
    '</div>',
    unsafe_allow_html=True
)
