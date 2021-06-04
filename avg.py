import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def info():
	df = pd.read_csv('data/happiness_combined_year copy 2.csv')
	df = df.drop(columns=['Unnamed: 0'],axis=1)
	avg = df.groupby(['Country']).mean().sort_values(by='Happiness Score',ascending=False).reset_index()
	
	avg.plot('Country','Generosity')
	plt.title("Average Generosity Country-wise")
	st.pyplot()

	avg.plot('Country','Trust (Government Corruption)')
	plt.title("Average Government Corruption Country-wise")
	st.pyplot()

	avg.plot('Country','Freedom')
	plt.title("Average Freedom Country-wise")
	st.pyplot()

	avg.plot('Country','Economy (GDP per Capita)')
	plt.title("Average GDP Country-wise")
	st.pyplot()

	avg.plot('Country','Health (Life Expectancy)')
	plt.title("Average Life Expectancy Country-wise")
	st.pyplot()

	avg.plot('Country','Family')
	plt.title("Average Social Support Country-wise")
	st.pyplot()

def load_page():
	st.markdown("<h1 style='text-align: center;'>Average Based Analysis</h1>", unsafe_allow_html=True)
	info()
    

if __name__ == "__main__":
	load_page()
