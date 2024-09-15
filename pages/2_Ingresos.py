import streamlit as st

st.title("Clientes")

import streamlit as st
from PIL import Image
from datetime import datetime

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import time
import json
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
from datetime import datetime



st.title('Sierras Y Equipos')
st.subheader('Registro de Proceso, Estación 1.')

orden_t = st.selectbox(
    'Selecciona la Orden',
    ('1234', '4567', '8910'),key=1)


proceso = st.selectbox(
    'Selecciona el proceso',
    ('Proceso 1', 'Proceso 2', 'Proceso 3'),key=2)

estado=st.selectbox(
    'Selecciona el Estado',
    ('Recibido', 'En Proceso', 'Terminado'),key=3)



bucket = "prueba1"
org = "tampa_cleaning"
token = "gY5PojXQ1zAbW2CwdUMFjG5l4PsmLYcx9WCSvJx3Jiq73PZUpRyGWALnB3WqaAUvMfjUo7GgCFph28zwcKHNUQ=="
# Store the URL of your InfluxDB instance
url="https://us-east-1-1.aws.cloud2.influxdata.com"
#cuando sea el local host 8086.....

if st.button('Registrar'):
   client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
   write_api = client.write_api(write_options=SYNCHRONOUS)
   p = influxdb_client.Point("Trazabilidad").tag("location", "Estación 1").field("Orden", orden_t)
   write_api.write(bucket=bucket, org=org, record=p)
   p = influxdb_client.Point("Trazabilidad").tag("location", "Estación 1").field("Proceso", proceso)
   write_api.write(bucket=bucket, org=org, record=p)
   p = influxdb_client.Point("Trazabilidad").tag("location", "Estación 1").field("Estado", estado)
   write_api.write(bucket=bucket, org=org, record=p)
