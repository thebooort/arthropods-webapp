#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   contacto.py
@Time    :   2023/06/28 13:55:20
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

st.set_page_config(page_title="Contacto", page_icon="📧")

logo_image = "images/logov3.png"
st.sidebar.markdown("# Proyecto A.T.L.A.S.")
st.sidebar.image(logo_image, use_column_width=True)

st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.image("images/ugritai.png", use_column_width=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.image("images/ugrlogo.png", use_column_width=True)

st.title("Proyecto A.T.L.A.S. - Arthropod Textual Language Analysis System")
st.markdown(" #### Sistema de análisis textual de descripciones de artrópodos")




image_url = "https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/images/logov3.png" 
image_width = 400
centered_image_html = f"""
<div style="display: flex; justify-content: center;">
<img src="{image_url}" style="width: {image_width}px;">
</div>
"""

st.markdown(centered_image_html, unsafe_allow_html=True)
# Add a title and description for the contact page
st.title("Contacto")
st.write("Dudas o sugerencias? ¡Escribenos!")
# add the logo small

# Add contact information
st.header("Informacion de contacto")
st.write("Bartolome Ortiz-Viso")
st.write("Centro de investigacion de Tecnologias de la Informacion y Comunicaciones (CITIC) - Universidad de Granada")
st.write("Email: bortiz@ugr.es")

# Add a form for users to enter their contact details and message
st.header("Formulario de contacto")
name = st.text_input("Nombre")
email = st.text_input("Email")
message = st.text_area("Mensaje")
submit_button = st.button("Enviar")

# Process the form submission
if submit_button:
    # Validate form inputs
    if name.strip() == "":
        st.error("Please enter your name.")
    elif email.strip() == "":
        st.error("Please enter your email.")
    elif message.strip() == "":
        st.error("Please enter your message.")
    else:
        key_dict = json.loads(st.secrets["textkey"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        db = firestore.Client(credentials=creds, project="arthropods-webapp")
        # generate a random id using uuid
        id = str(uuid.uuid4())
        doc_ref = db.collection("mensajes").document(id)
        doc_ref.set({
        'email': email,
        'mensaje': message,
        'nombre': name
        })
        # Process the form data (send email, save to database, etc.)
        st.success("Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.")