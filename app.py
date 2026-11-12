import streamlit as st

st.title("Mi primera pagina web")
st.write("Proyecto de Informatica - 9.º")

nombre = st.text_input("¿Como te llamas?")

if st.button("Saludar"):
    if nombre.strip():
        st.success(f"¡Hola, {nombre}!")
    else:
        st.warning("Primero escribi tu nombre.")
