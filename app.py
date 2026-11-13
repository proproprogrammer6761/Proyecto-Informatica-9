import streamlit as st

# --- Saludo ---
st.title("Mi primera pagina web")
st.write("Proyecto de Informatica - 9.º")

nombre = st.text_input("¿Como te llamas?")

if st.button("Saludar"):
    if nombre.strip():
        st.success(f"¡Hola, {nombre}!")
    else:
        st.warning("Primero escribi tu nombre.")

st.divider()

# --- Calculadora ---
st.title("🧮 Mi calculadora")
st.write("Realiza operaciones matemáticas.")

num1 = st.number_input("Primer número", value=0.0)
num2 = st.number_input("Segundo número", value=0.0)

operacion = st.selectbox(
    "Selecciona una operación",
    ["Sumar (+)", "Restar (-)", "Multiplicar (×)", "Dividir (÷)"]
)

if st.button("Calcular"):
    resultado = None

    if operacion == "Sumar (+)":
        resultado = num1 + num2

    elif operacion == "Restar (-)":
        resultado = num1 - num2

    elif operacion == "Multiplicar (×)":
        resultado = num1 * num2

    elif operacion == "Dividir (÷)":
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("No se puede dividir entre cero.")

    if resultado is not None:
        st.success(f"Resultado: {resultado}")
