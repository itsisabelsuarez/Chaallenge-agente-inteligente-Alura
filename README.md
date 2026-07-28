# 🤖 BimBam Buy AI Assistant

Agente inteligente desarrollado para el **Challenge Alura Agente**.

Este proyecto consiste en un asistente de inteligencia artificial capaz de responder preguntas sobre documentación interna de una empresa utilizando procesamiento de documentos y modelos de lenguaje.

El objetivo es facilitar el acceso a información empresarial, permitiendo que las personas colaboradoras consulten documentos mediante preguntas en lenguaje natural sin necesidad de revisar manualmente archivos extensos.

---

# 📌 Descripción del proyecto

**BimBam Buy** es una plataforma de comercio electrónico enfocada en brindar una experiencia de compra digital ágil y segura.

Para este desafío se desarrolló un agente inteligente capaz de consultar la **Política de Reembolsos y Devoluciones de BimBam Buy** y responder preguntas relacionadas con procesos de postventa, devoluciones, garantías y atención al cliente.

El agente permite obtener respuestas rápidas basadas únicamente en la información contenida dentro del documento PDF proporcionado.

---

# 🏗️ Arquitectura de la solución

El flujo general de la aplicación es:

```
Usuario
   │
   ▼
Interfaz web desarrollada con Streamlit
   │
   ▼
Carga y procesamiento del documento PDF
   │
   ▼
LangChain
   │
   ▼
Modelo de lenguaje Llama mediante Groq API
   │
   ▼
Respuesta generada basada en la documentación
```

---

# 🛠️ Tecnologías utilizadas

- **Python** - Lenguaje principal de desarrollo.
- **Streamlit** - Creación de la interfaz web interactiva.
- **LangChain** - Framework para integración con modelos de lenguaje.
- **LangChain Community** - Herramientas para carga y procesamiento de documentos.
- **LangChain Groq** - Conexión con modelos de inteligencia artificial.
- **PyPDF** - Lectura y procesamiento de archivos PDF.
- **Groq API** - Proveedor del modelo de lenguaje.
- **Git y GitHub** - Control de versiones y almacenamiento del proyecto.

---

# 📂 Estructura del proyecto

```
Chaallenge-agente-inteligente-Alura/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── documentos/
    └── bimbam_buy.pdf
```

---

# 🚀 Instalación y ejecución local

## 1. Clonar el repositorio

```bash
git clone https://github.com/itsisabelsuarez/Chaallenge-agente-inteligente-Alura
```

## 2. Entrar al proyecto

```bash
cd Chaallenge-agente-inteligente-Alura
```

## 3. Crear entorno virtual

```bash
python3 -m venv .venv
```

## 4. Activar entorno virtual

En Linux:

```bash
source .venv/bin/activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 6. Configurar variables de entorno

Crear un archivo llamado:

```
.env
```

Agregar la API Key:

```env
GROQ_API_KEY=tu_api_key
```

## 7. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```
http://localhost:8501
```

---

# 💬 Ejemplos de preguntas que puede responder el agente

## Pregunta:

¿Cuánto tiempo tarda un reembolso aprobado?

## Respuesta:

Los reembolsos aprobados se procesan en un plazo de entre **5 y 10 días hábiles**, dependiendo del método de pago y del país de origen de la compra.

---

## Pregunta:

¿Qué evidencia se requiere para un producto dañado?

## Respuesta:

El soporte puede solicitar:

- Foto del producto.
- Video del funcionamiento o daño.
- Foto del empaque.
- Foto de la etiqueta de envío.
- Comprobante de recepción.
- Número de serie.
- Descripción detallada del incidente.
- Captura del error o mensaje del sistema.

La evidencia debe ser legible, reciente y consistente con el caso reportado.

---

## Pregunta:

¿Cuáles son los canales oficiales de atención?

## Respuesta:

Las solicitudes se gestionan mediante:

- Centro de ayuda en la web.
- Formulario de postventa.
- Chat de soporte.
- Correo de atención al cliente.

---

# 🚀  Deploy

La aplicación será desplegada en la nube utilizando **Streamlit Cloud**, permitiendo acceder al agente mediante una URL pública.

La evidencia del despliegue será incluida mediante captura de pantalla y enlace público de la aplicación.

🔗 Enlace:
https://chaallenge-agente-inteligente-alura-drgpnskywktgh2htz2kbcu.streamlit.app/

## 📸 Evidencia de funcionamiento

El agente puede responder preguntas relacionadas con las políticas de BimBam Buy utilizando el documento PDF como fuente de conocimiento.

Ejemplo:

**Pregunta:**
¿Cuánto tiempo tarda un reembolso aprobado?

**Respuesta:**
Según el documento, un reembolso aprobado se procesa en un plazo de entre 5 y 10 días hábiles, dependiendo del método de pago y del país de origen de la compra.

<img width="1366" height="447" alt="Screenshot 2026-07-28 1 57 40 AM" src="https://github.com/user-attachments/assets/8e5c7b22-4f6b-47a1-87f9-18bd94f746f3" />

---

# 🎯 Objetivos alcanzados

✅ Procesamiento de un documento PDF empresarial.  
✅ Creación de un agente inteligente basado en IA.  
✅ Integración con un modelo de lenguaje.  
✅ Desarrollo de una interfaz web interactiva.  
✅ Documentación completa del proyecto.  
✅ Preparación para despliegue en la nube.

---

# 👩‍💻 Autora

**Isabel Suarez**

Proyecto realizado como parte del **Challenge Alura Agente Inteligente**.
