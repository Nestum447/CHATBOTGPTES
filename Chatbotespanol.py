import streamlit as st
from transformers import pipeline

# Cargar GPT-2 entrenado en español
modelo = pipeline("text-generation", model="DeepESP/gpt2-spanish")

# Crear la interfaz en Streamlit
st.title("📚 Chatbot con  CARPIO GPT en Español")
st.write("Hazme una pregunta y te responderé.")

# Entrada del usuario
pregunta = st.text_input("Pregunta:")

if st.button("Responder"):
    respuesta = modelo(pregunta, max_length=50, do_sample=True)
    st.write("🤖 **Asistente:**", respuesta[0]["generated_text"])

