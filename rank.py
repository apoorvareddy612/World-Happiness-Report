import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def info():
	df = pd.read_csv('data/happiness_combined_year copy 2.csv')
	df = df.drop(columns=['Unnamed: 0'],axis=1)

	rank = list(df['Happiness Rank'].unique())
	rank_sel = st.multiselect('Select Happiness Rank', rank)

	for i in rank_sel:
		a = df[df['Happiness Rank'] == i]
		st.write(a)

		plt.figure(figsize=(16,8))
		plt.subplot(3, 2, 1)
		sns.pointplot(x = "Year",
		              y = "Economy (GDP per Capita)",
		              data = a,hue='Country')
		st.pyplot()
		plt.subplot(3, 2, 2)
		sns.pointplot(x = "Year",
		              y = "Family",
		              data = a,hue='Country')
		st.pyplot()
		plt.subplot(3, 2, 3)
		sns.pointplot(x = "Year",
		              y = "Health (Life Expectancy)",
		              data = a,hue='Country')
		st.pyplot()
		plt.subplot(3, 2, 4)
		sns.pointplot(x = "Year",
		              y = "Freedom",
		              data = a,hue='Country')
		st.pyplot()
		plt.subplot(3, 2, 5)
		sns.pointplot(x = "Year",
		              y = "Trust (Government Corruption)",
		              data = a,hue='Country')
		st.pyplot()
		plt.subplot(3, 2, 6)
		sns.pointplot(x = "Year",
		              y = "Generosity",
		              data = a,hue='Country')
		st.pyplot()







def load_page():
	info()


if __name__ == "__main__":
	load_page()
