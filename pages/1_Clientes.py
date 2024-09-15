import streamlit as st
from datetime import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import time
import json
from influxdb_client import InfluxDBClient, Point, WritePrecision
import pandas as pd


#from streamlit_option_menu import option_menu

hide_st_style = """
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)  # Hide Streamlit's own CSS


st.title("Crear Clientes")
st.write(
    """
    Por favor ingrese la informacion del cliente y al final un describa un 
    perfil del cliente. 
    """
)

with st.form("formulario_ingreso_clientes", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input('Nombre', key="nombre")
    with col2:
        apellido = st.text_input('Apellido', key="apellido")  
    with col1:    
        estado_cliente = st.selectbox("Estado", ["", "Activo", "Por Cotizar", "Cancelado"], key="estado_cliente")
    with col2:
        medio_de_pago = st.selectbox("Medio de pago", [" ","Venmo", "Zelle", "Cheque", "Efectivo", "Transferencia", "Otro"], key="medio_de_pago")
    with col1: 
        telefono = st.text_input('Numero de telefono', key="telefono")
    with col2:
        email = st.text_input('Email', key="email")
    with col1:
        alergias = st.selectbox('Sufre de alergias:',['','No','Si'], key="alergias")
    with col2:
        descripcion_alergias = st.text_input('Especifique alergias:', key="descripcion_alergias")
    col1, col2, col3 = st.columns(3)
    with col1:
        tiene_hijos = st.selectbox("Tiene hijos:", ['','No','Si'], key="tiene_hijos")
    with col2:
        vive_con_hijos = st.selectbox('Viven con hijos:', ['','No','Si'], key="vive_con_hijos")
    with col3:
        tiene_mascotas = st.selectbox('Tiene mascotas:', ['','No','Si'], key="tiene_mascotas")
    with col1:
        fecha_vinculacion = st.date_input('Fecha de vinculacion', key="fecha_vinculacion")
    with col2:
        fecha_cumpleanos = st.date_input('Fecha de Cumpleaños', key="fecha_cumpleanos")
    with col3:
        fecha_terminacion = st.date_input('Fecha de terminacion', key="fecha_terminacion")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        rango_de_edad = st.selectbox("Rango de Edad:", ['','Menor de 30 años','31-50 años', 'Mayor de 50 años'], key="rango_de_edad")
    
    with col2:
        seguro_social = st.text_input('Seguro Social-ITN', key="seguro_social")
    
    perfil_cliente = st.text_area("Describa el perfil cliente", key="perfil_cliente")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"], key="priority")
    
    submitted = st.form_submit_button("Guardar")
    
    bucket = "prueba1"
    org = "tampa_cleaning"
    token = "gY5PojXQ1zAbW2CwdUMFjG5l4PsmLYcx9WCSvJx3Jiq73PZUpRyGWALnB3WqaAUvMfjUo7GgCFph28zwcKHNUQ=="
    # Store the URL of your InfluxDB instance
    url="https://us-east-1-1.aws.cloud2.influxdata.com"
    #cuando sea el local host 8086.....
    
    if submitted:
        client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        p = influxdb_client.Point("Cliente").tag("Nombre"=nombre, "Apellido"=apellido, "Estado"=estado_cliente).field("Estado", estado_cliente)
        write_api.write(bucket=bucket, org=org, record=p)

    # Haciendo pruebas coloque todo lo anterior en comentarios.   
        # p = influxdb_client.Point("Trazabilidad").tag("Nombre", "Apellido", "Estado").field(nombre, apellido, estado_cliente)
        # write_api.write(bucket=bucket, org=org, record=p)
        # p = influxdb_client.Point("Trazabilidad").tag("location", "Estación 1").field("Estado del cliente", estado_cliente)
        # write_api.write(bucket=bucket, org=org, record=p)
    


    
    #TODO:Insert data into Database
    if submitted:
        st.write(f"nombre: {nombre}")
        st.write(f"apellido: {apellido}")
        st.write(f"estado_cliente: {estado_cliente}")
        st.write(f"medio_de_pago: {medio_de_pago}")
        st.write(f"telefono: {telefono}")
        st.write(f"email: {email}")
        st.write(f"alergias: {alergias}")
        st.write(f"descripcion_alergias: {descripcion_alergias}")
        st.write(f"tiene_hijos: {tiene_hijos}")
        st.write(f"vive_con_hijos: {vive_con_hijos}")
        st.write(f"tiene_mascotas: {tiene_mascotas}")
        st.write(f"fecha_vinculacion: {fecha_vinculacion}")
        st.write(f"fecha_cumpleanos: {fecha_cumpleanos}")
        st.write(f"fecha_terminacion: {fecha_terminacion}")
        st.write(f"rango_de_edad: {rango_de_edad}")
        st.write(f"seguro_social: {seguro_social}")
        st.write(f"perfil_cliente: {perfil_cliente}")
        st.write(f"priority: {priority}")
        st.success("Cliente guardado exitosamente")




