
import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv  
from csv import reader


def app():
	data1=pd.read_csv('stunted.csv')
	df1=pd.DataFrame(data1)

	stunted=st.container()
	with stunted:

		st.header("Prevalance of stunting in children under 5 years of age")
		st.write("Stunting is the impaired growth and development that children experience from poor nutrition, repeated infection, and inadequate psychosocial stimulation.")
		st.write("Stunting in early life -- particularly in the first 1000 days from conception until the age of two - impaired growth has adverse functional consequences on the child. Some of those consequences include poor cognition and educational performance, low adult wages, lost productivity and, when accompanied by excessive weight gain later in childhood, an increased risk of nutrition-related chronic diseases in adult life.")
		X=list(df1.iloc[:,0])
		Y=list(df1.iloc[:,1])
		fig=plt.figure(figsize=(5,5))
		st.subheader("Graph showing prevalance of stunting:")
		plt.barh(X,Y,color='cadetblue')
		plt.xlabel("States/UTs")
		plt.ylabel("percentage of population")
		st.pyplot(fig)
