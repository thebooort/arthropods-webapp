#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   WebApp.py
@Time    :   2023/06/28 14:00:34
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

st.set_page_config(page_title="Colabora y difunde", page_icon="❤️")


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
st.write("Ayúdanos a llegar a mas gente difundiendo el proyecto por redes sociales, a traves de la web o del QR")
st.markdown(centered_image_html, unsafe_allow_html=True)
# Add a title and description for the contact page
st.title("Media para difundir en redes sociales")

image_url = "https://raw.githubusercontent.com/thebooort/arthropods-webapp/main/images/QR.png" 
image_width = 400
centered_image_html = f"""
<div style="display: flex; justify-content: center;">
<img src="{image_url}" style="width: {image_width}px;">
</div>
"""
st.markdown(centered_image_html, unsafe_allow_html=True)