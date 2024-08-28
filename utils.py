# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd 

@st.cache_data
def load_data():
    data = pd.read_csv('data/cleansed.csv')
    

    return data

@st.cache_eda_data
def load_eda_data():
    eda = pd.read_csv('data/cleansed.csv')

    return eda