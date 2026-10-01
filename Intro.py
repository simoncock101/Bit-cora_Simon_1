import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 


 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yoloscg.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Analisis de fotos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como analizar fotos con IA.") 
 url = "https://photoan.streamlit.app"
 st.write(f"Analisis: [Enlace]({url})")

with col2: 
 st.subheader("Mi primera app")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos la primer app que hice en la materia") 
 url = "https://app1simon.streamlit.app"
 st.write(f"Primera app: [Enlace]({url})")

 st.subheader("Análisis del futbol colombiano")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos una IA que te habla del futbol colombiano.") 
 url = "https://chatfpc.streamlit.app"
 st.write(f"FPC: [Enlace]({url})")

 st.subheader("Texto a voz")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una app que pasa el texto a audio.") 
 url = "https://imm1profesor01.streamlit.app"
 st.write(f"Texto a voz: [Enlace]({url})")


with col3: 
 st.subheader("Analiza tus sentimientos")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación analiza como te sientes") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"Sentimientos: [Enlace]({url})")

 st.subheader("Análisis de personas")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos si en tus imagenes hay o no personas") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Personas: [Enlace]({url})")
 



