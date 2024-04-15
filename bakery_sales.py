import streamlit as st
import numpy as np
import pandas as pd 


# load data
@st.cache_data
def load_data():
    df = pd.read_csv('bakerysales.csv')
    return df

df = load_data()
st.write(df.head(3))
