import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv  
from csv import reader

def app():
	data4=pd.read_csv('under.csv')
	df4=pd.DataFrame(data4)

	underweight=st.container()
	with underweight:
		st.header("Underweight children under 5 years of age")
		st.write("Wasting is the most immediate, visible and life-threatening form of malnutrition. It results from the failure to prevent malnutrition among the most vulnerable children. Children with wasting are too thin and their immune systems are weak, leaving them vulnerable to developmental delays, disease and death. Some children affected by wasting also suffer from nutritional oedema, characterized by a swollen face, feet and limbs.")
		X=list(df4.iloc[:,0])
		Y=list(df4.iloc[:,1])
		fig=plt.figure(figsize=(5,5))
		st.subheader("Graph showing prevalance of underweight children:")
		plt.barh(X,Y,color='cadetblue')
		plt.xlabel("States/UTs")
		plt.ylabel("percentage of population")
		st.pyplot(fig)