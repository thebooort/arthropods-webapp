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


logo_image = "images/logobicho.png"

st.title("¡Descíbeme ese bichejo!")
st.sidebar.markdown('# ¡Descíbeme ese bichejo!')
st.sidebar.image(logo_image, use_column_width=True)
# Add a logo or image to the sidebar
st.sidebar.markdown('## Selecciona una pestaña')
  # Replace with the path to your logo image

# Add tabs to the sidebar
tabs = ["¿Cómo funciona?", "App", "Contacto"]
selected_tab = st.sidebar.radio("", tabs)
st.sidebar.image("images/ugrlogo.png", use_column_width=True)

if selected_tab == "¿Cómo funciona?":
    # add the logo small
    image_url = "https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/images/logobicho.png" 
    image_width = 200
    centered_image_html = f"""
<div style="display: flex; justify-content: center;">
    <img src="{image_url}" style="width: {image_width}px;">
</div>
"""

    st.markdown(centered_image_html, unsafe_allow_html=True)
    st.subheader("'Descíbeme ese bichejo' es un proyecto de UGRITAI (Universidad de Granada).")
    st.markdown("## ¿Cuál es nuestro objetivo?")
    st.markdown("El objetivo de este proyecto es desarrollar una aplicación que permita identificar especies de artrópodos a partir de una descripción en lenguaje natural. Para ello, se ha creado una base de datos con información de 1.000 especies de artrópodos de la Península Ibérica. Esta base de datos se ha creado a partir de la información disponible en la plataforma [iNaturalist](https://www.inaturalist.org/).")
    st.markdown("## ¿Cómo funciona?")
    st.markdown("Clica en la pestaña App he introduce tu nivel de conocimientos. Tras unos segundos de carga, te aparecera una imagen de un artrópodo. A su lados tendrás su nombre y una descripción generalista para que puedas saber más sobre él. Finalmente escribe en el cuadro de texto tus descripción detallada del animal que estás viendo. ¡Cuantos más detalles mejor! Luego pulsa enviar. ¡Puedes repetirlo tantas veces como quieras!")
    st.markdown("## ¿Dudas, fallos, propuestas de colaboración?")
    st.markdown("Dirígete a contacto y allí te podrás poner en contacto con nosotros :)")
            
    # Add any additional information here



elif selected_tab == "App":
# Display content based on the selected tab
    st.write("¿Estás preparadx? Antes de continuar describe tu nivel de conocimiento de insectos del 1 al 10.")
    st.write("1: No tengo ni idea")
    st.write("10: Soy un experto")
    # Add your app content here
    user_expertise = st.number_input("¡Describe tu nivel de conocimiento de insectos!", min_value=1, max_value=10, step=1)

    if user_expertise <5:
        st.write("Tu nivel de conocimientos es bajo. No te preocupes, te ayudaremos con la descripción mostrandote un diagrama para que sepas cómo nombrar diferentes partes comunes de los artrópodos.")
        st.image("https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/images/esquema de insecto basico.png" , caption="De: https://leerciencia.net/insectos-las-3-partes-de-su-cuerpo/ Todos los derechos reservados",use_column_width=True)
        st.markdown("## ¡A describir!")

    # get a random row from  df
    df = pd.read_excel('https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/database/animales_filtered.xlsx')
    pd.set_option('display.max_colwidth', None)
    random_row = df.sample()

    # join Género and Especie column to get the full name
    full_name = random_row['Género'] + ' ' + random_row['Especie']
    full_name = full_name.to_string(index=False)
    # search image in inaturalist
    # Set the iNaturalist API endpoint and parameters
    url = "https://api.inaturalist.org/v1/search"
    params = {
        "q": full_name,  # Replace with the desired species name
        "photos": "true",
        "order_by": "random",
        "per_page": 1
    }

    # Send a GET request to the iNaturalist API
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the photo URL from the response
    observation = data["results"][0]
    photo_url = observation['record']['default_photo']['medium_url']

    print("Photo URL:", photo_url)

    # Make a request to the URL and get the image data
    response = requests.get(photo_url)
    image = Image.open(BytesIO(response.content))
    author = observation['record']['default_photo']['attribution']
    # Display the image in Streamlit
    st.image(image, caption='Fotografía del especimen: '+full_name +' \n '+author, use_column_width=True)

    # add text from the df
    st.write('Estas viendo un especimen de   ', random_row['Género'].to_string(index=False), ' ', random_row['Especie'].to_string(index=False))
    
    





    # expertise level

    # Create a text input field
    user_description = st.text_input("¡Describe el animal que estás viendo!", max_chars=500)

    submit = st.button("¡He terminado!")

    if user_description and user_expertise and submit:
        # Authenticate to Firestore with the JSON account key.
        print('¡Enviado info a la base de datos!')
        key_dict = json.loads(st.secrets["textkey"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        db = firestore.Client(credentials=creds, project="arthropods-webapp")
        # generate a random id using uuid
        id = str(uuid.uuid4())
        doc_ref = db.collection("description").document(id)
        doc_ref.set({
        'Description': user_description,
        'Expertise': user_expertise,
        'Family': random_row['Familia'].to_string(index=False),
        'Genus': random_row['Género'].to_string(index=False),
        'Order': random_row['Orden'].to_string(index=False),
        'Species': random_row['Especie'].to_string(index=False),
        'class': random_row['Clase'].to_string(index=False),
        'link_to_photo': photo_url
        })


        user_description=""
        user_description = st.text_input("¡Describe el animal que estás viendo!", max_chars=500,value=user_description)
        st.write("¡Gracias por tu colaboración!")
        st.write("Puedes segui jugando enviando cuantas descripciones quieras :smile:")
        st.write("Aquí te dejamos una descripción generalista del animal que acabas de ver para que puedas aprender algo más sobre él:")
        descri = random_row['Descripción'].to_string(index=False)
        # remove extra spaces
        descri = descri.strip()
        # remove extra lines
        descri = descri.replace('\n', ' ')
        # remove extra tabs
        descri = descri.replace('\t', ' ')
        # remove extra spaces
        descri = descri.replace('  ', ' ')
        st.write(descri)

elif selected_tab == "Contacto":
    # Add a title and description for the contact page
    st.title("Contacto")
    st.write("Dudas o sugerencias? ¡Escribenos!")

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




