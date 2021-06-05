import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def info():
	df = pd.read_csv('data/avg.csv')
	

	x = st.sidebar.selectbox(
	    "X axis",
	    tuple(df.columns.to_list())
	)

	y = st.sidebar.selectbox(
	    "Y axis",
	    tuple(df.columns.to_list())
	)

	sns.scatterplot(x,y,data=df,hue='Country')
	plt.legend(bbox_to_anchor=(1.01, 1.05),borderaxespad=0)

	st.pyplot()



def load_page():
	info()

if __name__ == "__main__":
	load_page()
