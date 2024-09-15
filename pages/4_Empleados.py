import streamlit as st
st.title("Empleados")


popover = st.popover("Tiene alergias?")
tiene_alergias = popover.text_input("Describa las alergias")

if tiene_alergias != "" :
    st.write(tiene_alergias)
else :
    st.write("No tiene alergias")