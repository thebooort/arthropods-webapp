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


# get a random row from  df
df = pd.read_excel('https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/database/animales_filtered.xlsx')
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
st.write(random_row['Descripción'].to_string(index=False))

# expertise level
user_expertise = st.number_input("¡Describe tu nivel de conocimiento de insectos!", min_value=1, max_value=10, step=1)
# Create a text input field
user_description = st.text_input("¡Describe el animal que estás viendo!", "")

submit = st.button("¡He terminado!")


# Authenticate to Firestore with the JSON account key.
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="arthropods-webapp")

# # Create a reference to the Google post.
# doc_ref = db.collection("description").document("qzuXvqwqFOzmsjoqPbRn")

# # Then get the data at that reference.
# doc = doc_ref.get()

# # Let's see what we got!
# st.write("The id is: ", doc.id)
# st.write("The contents are: ", doc.to_dict())

if user_description and user_expertise and submit:
	# generate a random id using uuid
    id = str(uuid.uuid4())
    doc_ref = db.collection("description").document(id)
    doc_ref.set({
    'Description': user_description,
    'Expertise': user_expertise,
    'Family': random_row['Familia'],
    'Genus': random_row['Género'],
    'Order': random_row['Orden'],
    'Species': random_row['Especie'],
    'class': random_row['Clase'],
    'link_to_photo': photo_url
	})



