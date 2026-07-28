import streamlit as st
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq


# Cargar variables de entorno
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


# Configurar modelo de IA
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=api_key,
    temperature=0.3
)


# Cargar documento PDF
loader = PyPDFLoader("documentos/bimbam_buy.pdf")

documents = loader.load()

texto_documento = "\n".join(
    [document.page_content for document in documents]
)


# Interfaz de Streamlit
st.title("🤖 BimBam Buy AI Assistant")

st.write(
    "Asistente inteligente para responder preguntas sobre la política de reembolsos y devoluciones de BimBam Buy."
)


pregunta = st.text_input(
    "Escribe tu pregunta:"
)


if pregunta:

    prompt = f"""
    Eres un asistente experto de BimBam Buy.

    Responde únicamente utilizando la información del documento proporcionado.

    Si la respuesta no aparece en el documento, indica:
    "No encontré esa información en la documentación disponible."

    Documento:
    {texto_documento}

    Pregunta:
    {pregunta}
    """

    respuesta = llm.invoke(prompt)

    st.subheader("Respuesta:")
    st.write(respuesta.content)
