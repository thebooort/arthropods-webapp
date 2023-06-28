#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   streamlit_app.py
@Time    :   2023/06/26 18:41:37
@Author  :   Bart Ortiz 
@Version :   1.0
@Contact :   bortiz@ugr.es
@License :   CC-BY-SA or GPL3
@Desc    :   None
'''

import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import pandas as pd
import wikipedia
import requests
import json
from PIL import Image
import requests
from io import BytesIO
import uuid

st.set_page_config(page_title="Inicio", page_icon="🌞")

logo_image = "images/logov3.png"
st.sidebar.success("Selecciona una pestaña arriba.")
st.title("Proyecto A.T.L.A.S. - Arthropod Textual Language Analysis System")
st.markdown(" #### Sistema de análisis textual de descripciones de artrópodos")

st.sidebar.markdown("# Proyecto A.T.L.A.S.")
st.sidebar.image(logo_image, use_column_width=True)
# Add a logo or image to the sidebar
  # Replace with the path to your logo image
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
# Add tabs to the sidebar
st.sidebar.image("images/ugritai.png", use_column_width=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.image("images/ugrlogo.png", use_column_width=True)


# add the logo small
image_url = "https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/images/logov3.png" 
image_width = 400
centered_image_html = f"""
<div style="display: flex; justify-content: center;">
<img src="{image_url}" style="width: {image_width}px;">
</div>
"""

st.markdown(centered_image_html, unsafe_allow_html=True)
st.subheader("A.T.L.A.S. es un proyecto de UGRITAI (Universidad de Granada).")
st.markdown("## ¿Cuál es nuestro objetivo?")
st.markdown("El objetivo de este proyecto es desarrollar una aplicación que permita identificar especies de artrópodos a partir de una descripción en lenguaje natural. Para ello, se ha creado una base de datos con información de 1.000 especies de artrópodos de la Península Ibérica. Esta base de datos se ha creado a partir de la información disponible en la plataforma [iNaturalist](https://www.inaturalist.org/).")
st.markdown("## ¿Cómo funciona?")
st.markdown("Clica en la pestaña App he introduce tu nivel de conocimientos. Tras unos segundos de carga, te aparecera una imagen de un artrópodo. A su lados tendrás su nombre y una descripción generalista para que puedas saber más sobre él. Finalmente escribe en el cuadro de texto tus descripción detallada del animal que estás viendo. ¡Cuantos más detalles mejor! Luego pulsa enviar. ¡Puedes repetirlo tantas veces como quieras!")
st.markdown("## Historia del logo")
st.markdown("El logo muestra el contorno de un escarabajo atlas, con nombre científico *Chalcosoma atlas*, lo cual conecta la temática del proyecto con nuestras siglas ATLAS. Este escarabajo es una especie de coleóptero de la familia Scarabaeidae. Es una de las especies de escarabajos más grandes del mundo, y se encuentra en el sudeste asiático, en particular en Indonesia. El nombre de la especie proviene del titán griego Atlas, que fue condenado a sostener el cielo sobre sus hombros. El nombre común se deriva de la semejanza de los cuernos del macho con los del titán Atlas. ")
st.markdown("## ¿Dudas, fallos, propuestas de colaboración?")
st.markdown("Dirígete a contacto y allí te podrás poner en contacto con nosotros :)")




