import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

def info():

	df = pd.read_csv('data/happiness_combined_year copy 2.csv')
	df = df.drop(columns=['Unnamed: 0'],axis=1)
	data = {'score>7':df[df['Happiness Score'] > 7].shape[0],'7=>score>6':df[(df['Happiness Score'] > 6) & (df['Happiness Score'] <= 7)].shape[0],'6=>score>5':df[(df['Happiness Score'] > 5) & (df['Happiness Score'] <= 6)].shape[0],'5=>score>4':df[(df['Happiness Score'] > 4) & (df['Happiness Score'] <= 5)].shape[0],'4=>score>3': df[(df['Happiness Score'] > 3) & (df['Happiness Score'] <= 4)].shape[0],'3=>score>2':df[(df['Happiness Score'] > 2) & (df['Happiness Score'] <= 3)].shape[0]}
	score = pd.DataFrame(data.items())
	score.plot(0,1,kind='bar')
	plt.xlabel('Happiness Score')
	plt.ylabel('Count of countries')
	st.pyplot()

def load_page():
	info()


if __name__ == "__main__":
	load_page()
