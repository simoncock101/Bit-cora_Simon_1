
import streamlit as st


# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Mis aplicaciones y proyectos",
    page_icon="💻",
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
    min-height: 350px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.20);
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


/* ADAPTACIÓN A MÓVILES */

@media (max-width: 768px) {
    .titulo {
        font-size: 32px;
    }

    .nombre {
        font-size: 19px;
    }

    .subtitulo {
        font-size: 16px;
    }

    .caja-principal {
        padding: 22px;
    }

    .tarjeta {
        min-height: auto;
        padding: 20px;
    }

    .tarjeta-emoji {
        font-size: 48px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LISTA DE APLICACIONES
# =========================================================

aplicaciones = [

    {
        "emoji": "👁️",
        "titulo": "Reconocimiento de objetos",
        "categoria": "Visión artificial",
        "descripcion": (
            "Detecta y reconoce diferentes objetos dentro de imágenes "
            "utilizando modelos de reconocimiento visual."
        ),
        "url": "https://yoloscg.streamlit.app"
    },

    {
        "emoji": "📷",
        "titulo": "Análisis de fotos",
        "categoria": "Análisis de imágenes",
        "descripcion": (
            "Permite analizar fotografías utilizando herramientas "
            "de procesamiento e interpretación de imágenes."
        ),
        "url": "https://photoan.streamlit.app"
    },

    {
        "emoji": "🤖",
        "titulo": "Mi primera app",
        "categoria": "Proyecto inicial",
        "descripcion": (
            "La primera aplicación que desarrollé durante la materia, "
            "como parte de mi exploración de herramientas digitales."
        ),
        "url": "https://app1simon.streamlit.app"
    },

    {
        "emoji": "⚽",
        "titulo": "Análisis del fútbol colombiano",
        "categoria": "Deportes y datos",
        "descripcion": (
            "Una aplicación para interactuar con información "
            "relacionada con el fútbol profesional colombiano."
        ),
        "url": "https://chatfpc.streamlit.app"
    },

    {
        "emoji": "🔊",
        "titulo": "Texto a voz",
        "categoria": "Voz y audio",
        "descripcion": (
            "Convierte texto escrito en audio mediante herramientas "
            "de síntesis de voz."
        ),
        "url": "https://imm1profesor01.streamlit.app"
    },

    {
        "emoji": "💭",
        "titulo": "Analiza tus sentimientos",
        "categoria": "Análisis de texto",
        "descripcion": (
            "Analiza textos para identificar información relacionada "
            "con sentimientos y emociones."
        ),
        "url": "https://sentimentascg.streamlit.app/"
    },

    {
        "emoji": "🧍",
        "titulo": "Análisis de personas",
        "categoria": "Visión artificial",
        "descripcion": (
            "Analiza imágenes para identificar la presencia de personas."
        ),
        "url": "https://editablereconocimiento.streamlit.app/"
    },

    {
        "emoji": "🎨",
        "titulo": "Tablero de dibujos",
        "categoria": "Dibujo e interacción",
        "descripcion": (
            "Permite realizar dibujos en un tablero y explorar "
            "su interpretación y descripción mediante herramientas "
            "digitales."
        ),
        "url": "https://dibujosdescripcionscg.streamlit.app"
    },

    {
        "emoji": "🔐",
        "titulo": "Cerradura facial",
        "categoria": "Reconocimiento facial",
        "descripcion": (
            "Explora el reconocimiento facial como mecanismo "
            "de identificación dentro de una experiencia de acceso."
        ),
        "url": "https://cerradurafacial.streamlit.app"
    },

    {
        "emoji": "🔢",
        "titulo": "Detector de números escritos a mano",
        "categoria": "Reconocimiento de dígitos",
        "descripcion": (
            "Reconoce números dibujados a mano mediante un sistema "
            "de clasificación de dígitos."
        ),
        "url": "https://detectordigitosmanos.streamlit.app"
    },

    {
        "emoji": "🎙️",
        "titulo": "Control por voz",
        "categoria": "Interfaces multimodales",
        "descripcion": (
            "Permite dar instrucciones mediante la voz y transmitir "
            "los comandos a otro sistema a través de comunicación MQTT."
        ),
        "url": "https://controlvozscg.streamlit.app"
    },

    {
        "emoji": "🗂️",
        "titulo": "Aplicación multipáginas",
        "categoria": "Navegación web",
        "descripcion": (
            "Explora una aplicación estructurada en diferentes páginas "
            "para organizar contenidos y facilitar la navegación."
        ),
        "url": "https://multipaginas.streamlit.app"
    },

    {
        "emoji": "📑",
        "titulo": "Ejemplo 1 multipágina",
        "categoria": "Navegación web",
        "descripcion": (
            "Proyecto de ejemplo que demuestra la organización "
            "y navegación entre distintas páginas de una aplicación."
        ),
        "url": "https://ejemplo1multipagina.streamlit.app"
    },

    {
        "emoji": "🔊",
        "titulo": "Audio y botones",
        "categoria": "Interacción multimedia",
        "descripcion": (
            "Explora una interfaz con botones interactivos y funciones "
            "relacionadas con la reproducción o el control de audio."
        ),
        "url": "https://ejemploaudioybotones.streamlit.app"
    },

    {
        "emoji": "🖌️",
        "titulo": "Tablero de dibujo",
        "categoria": "Dibujo e interacción",
        "descripcion": (
            "Un espacio interactivo para realizar dibujos digitales "
            "y experimentar con herramientas de creación visual."
        ),
        "url": "https://tablerodedibujoscg.streamlit.app"
    }

]


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 💻 Mis proyectos")

    st.markdown("---")

    st.markdown("### Sobre este portafolio")

    st.write(
        "Este espacio reúne aplicaciones, experimentos y proyectos "
        "interactivos desarrollados durante mi formación en Diseño "
        "Interactivo. Explora herramientas, experiencias digitales "
        "y soluciones creadas con diferentes tecnologías."
    )

    st.markdown("---")

    st.markdown("### 🚀 Proyectos")

    for app in aplicaciones:
        st.write(f'{app["emoji"]} {app["titulo"]}')

    st.markdown("---")

    st.markdown("### 🎓 Formación")

    st.write("Diseño Interactivo · Universidad EAFIT")

    st.markdown("---")

    st.caption(
        "Diseño, experimentación y desarrollo de experiencias digitales."
    )


# =========================================================
# ENCABEZADO
# =========================================================

st.markdown(
    '<div class="titulo">Mis aplicaciones y '
    '<span class="azul">proyectos interactivos</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nombre">Simon Cock García</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Explora aplicaciones, experimentos y experiencias digitales '
    'desarrolladas durante mi formación.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# ENLACE PRINCIPAL
# =========================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    '<div class="caja-principal">'
    '<div class="caja-titulo">🌐 Recursos y proyectos</div>'
    '<div class="caja-texto">'
    'Descubre más ejercicios, herramientas y proyectos digitales.'
    '</div>'
    '<a href="' + url_ia + '" target="_blank" '
    'rel="noopener noreferrer" class="boton-principal">'
    'Explorar página →'
    '</a>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# TÍTULO Y CONTADOR DE PROYECTOS
# =========================================================

st.markdown(
    '<div class="titulo-seccion">🚀 Mis proyectos</div>',
    unsafe_allow_html=True
)

st.caption(
    f"Explora los {len(aplicaciones)} proyectos y accede a cada aplicación."
)


# =========================================================
# FUNCIÓN PARA CREAR TARJETAS
# =========================================================

def crear_tarjeta(app):

    html = (
        '<div class="tarjeta">'
        '<div class="tarjeta-emoji">' + app["emoji"] + '</div>'
        '<div class="tarjeta-categoria">' + app["categoria"] + '</div>'
        '<div class="tarjeta-titulo">' + app["titulo"] + '</div>'
        '<div class="tarjeta-texto">' + app["descripcion"] + '</div>'
        '<a href="' + app["url"] + '" target="_blank" '
        'rel="noopener noreferrer" class="boton">'
        'Abrir proyecto →'
        '</a>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# =========================================================
# DISTRIBUCIÓN AUTOMÁTICA EN TRES COLUMNAS
# =========================================================

columnas = st.columns(3, gap="large")

for indice, app in enumerate(aplicaciones):

    with columnas[indice % 3]:
        crear_tarjeta(app)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    '💻 <b>Aplicaciones y proyectos interactivos</b>'
    '<br><br>'
    'Simon Cock García · Diseño Interactivo'
    '<br><br>'
    'Diseñando y desarrollando experiencias digitales.'
    '</div>',
    unsafe_allow_html=True
)

