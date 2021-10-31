
import matplotlib as mp
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv  
from csv import reader
import streamlit as st
from multiapp import MultiApp
from apps import stunted, under, wasted, severe, anaemic# import your app modules here


st.title("Malnutrition in Indian Children")
st.write("Malnutrition amongst children under the age of five is a doorway to a life landmarked with cognitive and physical setbacks. With words like ‘consumerism’ and ‘food surplus’ headlining the world today, high levels of malnutrition shine light on the harsh truth of inequality, lack of access and poverty that continue to affect the lives of millions around the globe.")
st.write("The prevalence of malnutrition and its detrimental effects on children in India is alarming. In a report published by UNICEF , it was noted that malnutrition was the cause of 69% of deaths of children under the age of five in India, additionally noting that within the under-five age bracket, every second child suffers from some form of malnutrition  (Economic Times, 2019).")
st.header("NHFS data on malnourishment in children under 5 years of age")
st.write("The National Family Health Survey (NFHS) is a large-scale, multi-round survey conducted in a representative sample of households throughout India. Three rounds of the survey have been conducted since the first survey in 1992-93. The survey provides state and national information for India on fertility, infant and child mortality, the practice of family planning, maternal and child health, reproductive health, nutrition, anaemia, utilization and quality of health and family planning services. ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

app = MultiApp()

st.markdown("""

""")
# Add all your application here
app.add_app("Prevalance of stunting in children under 5 years of age", stunted.app)
app.add_app("Prevalance of wasting in children under 5 years of age", wasted.app)
app.add_app("Prevalance of severe wasting in children under 5 years of age", severe.app)
app.add_app("Underweight children under 5 years of age", under.app)
app.add_app("Anaemic children under 5 years of age", anaemic.app)
#app.add_app("Dietary Recommendations for ages 1 to 18:", diet.app)
# The main app
app.run()

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