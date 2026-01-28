import streamlit as st
st.title("Calculadora de Propinas")
st.sidebar.header("Registre los datos de la cuenta")
Total = st.sidebar.number_input("Monto total de la cuenta", min_value=0.0, step=0.01)
Porcentaje = st.sidebar.number_input("Porcentaje de la propina (%)", min_value=0, step=1)
if st.sidebar.button("Calcular Propina"): 
    Propina = Total * (Porcentaje / 100)
    st.metric(label="Propina sugerida", value=f"₡{Propina:,.2f}")