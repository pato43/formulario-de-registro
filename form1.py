import streamlit as st
from fpdf import FPDF
import base64
import os

# Configuración de página con modo oscuro forzado
st.set_page_config(page_title="Registro Curso Python - Microsoft & Santander", layout="centered")

# Estilos para modo oscuro
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px 20px;
    }
    header, .css-18ni7ap, .css-1d391kg, .css-hxt7ib {
        background-color: #0e1117;
    }
</style>
<div class="main">
""", unsafe_allow_html=True)

# Logos
st.image("images/Banco_Santander_Logotipo.svg.png", width=120)
st.image("images/msoft.png", width=120)
st.image("images/ChatGPT Image 9 abr 2025, 04_36_04 p.m..png", width=120)

st.markdown("""
### Formulario de Inscripción - Curso Ciencia de Datos con Python
**Curso certificado por Microsoft y Santander**  
Tessena, como empresa partner, gestionará la emisión de certificados oficiales con QR verificable
---
""")

# Formulario de inscripción
nombre = st.text_input("👤 Nombre completo")
curp = st.text_input("🆔 CURP")
motivo = st.text_area("✍️ ¿Por qué decidiste tomar este curso?")
pagos = st.selectbox("💳 ¿Cuántos meses has pagado?", ["Selecciona", "1 mes", "2 meses", "3 meses"])

# Aceptación del uso de datos
uso_datos = st.checkbox("✅ Autorizo el uso de mis datos para la gestión de certificados por parte de Microsoft y Santander a través de Tessena")

# Botón de generar documento
if st.button("📄 Generar constancia de registro"):
    if nombre and curp and motivo and pagos != "Selecciona" and uso_datos:

        # Crear PDF
        pdf = FPDF()
        pdf.add_page()

        # Agregar logos
        if os.path.exists("images/Banco_Santander_Logotipo.svg.png"):
            pdf.image("images/Banco_Santander_Logotipo.svg.png", x=10, y=8, w=40)
        if os.path.exists("images/msoft.png"):
            pdf.image("images/msoft.png", x=80, y=8, w=40)
        if os.path.exists("images/ChatGPT Image 9 abr 2025, 04_36_04 p.m..png"):
            pdf.image("images/ChatGPT Image 9 abr 2025, 04_36_04 p.m..png", x=150, y=8, w=40)

        pdf.ln(30)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "Constancia de Registro - Curso Ciencia de Datos con Python", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"""
Se deja constancia de que:

Nombre completo: {nombre}
CURP: {curp}

Ha decidido inscribirse al curso de Ciencia de Datos con Python, gestionado por Tessena, empresa partner de Microsoft y Santander.

Motivo de inscripción:
{motivo}

Estado del pago: {pagos}

El participante autoriza expresamente el uso de sus datos para la gestión de certificados oficiales con QR emitidos directamente desde los dominios oficiales aka.ms, validando su acreditación en:

1. Python para manejo de datos
2. Modelos de regresión
3. Agrupamiento y clustering
4. Análisis de datos

Esta constancia avala su preinscripción al curso que dará inicio el día 21 de abril, con duración de 3 meses.

Firma digital: ___________________________

Fecha: _________________________________
        """)

        # Guardar PDF en memoria
        pdf_output = pdf.output(dest='S').encode('latin1')
        b64_pdf = base64.b64encode(pdf_output).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="constancia_registro_{nombre}.pdf">📥 Descargar constancia en PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Por favor completa todos los campos y acepta el uso de datos.")

st.markdown("""</div>""", unsafe_allow_html=True)
