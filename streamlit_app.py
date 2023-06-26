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

st.header('Hello 🌎!')
if st.button('Balloons?'):
    st.balloons()
