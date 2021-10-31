import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import csv  
from csv import reader

def app():
	data5=pd.read_csv('anaemic.csv')
	df5=pd.DataFrame(data5)

	anaemic=st.container()
	with anaemic:
		st.header("Anaemic children under 5 years of age")
		st.write("Anemia is a common problem in children. A child who has anemia does not have enough red blood cells or hemoglobin. Hemoglobin is a type of protein that allows red blood cells to carry oxygen to other cells in the body.")
		X=list(df5.iloc[:,0])
		Y=list(df5.iloc[:,1])
		fig=plt.figure(figsize=(5,5))
		st.subheader("Graph showing prevalance of anaemia in children:")
		plt.barh(X,Y,color='cadetblue')
		plt.xlabel("States/UTs")
		plt.ylabel("percentage of population")
		st.pyplot(fig)