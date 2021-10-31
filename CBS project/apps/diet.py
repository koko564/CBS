import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv  
from csv import reader


def app():
    st.header("Dietary Recommendations for ages 1 to 18:")
    gender= st.selectbox(
         'Gender',
         ('Select an option','Male', 'Female'))

    age= st.selectbox(
         'Age',
         ('Select an option',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))



    if gender=='Female' and age!='Select an option':
        df=pd.read_csv('female.csv',usecols=[0,age])
        df.index = [">"] * len(df)
        st.table(df)
      

    elif gender=='Male' and age!='Select an option':
            df=pd.read_csv('male.csv',usecols=[0,age])
            df.index = [">"] * len(df)
            st.table(df)