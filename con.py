import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def info():
	df = pd.read_csv('data/data1.csv')
	df.drop(['Unnamed: 0'],axis=1)

	Region = ['Europe','Asia','America','Africa']
	Region_SELECTED = st.multiselect('Select countries', Region)


	Europe = df[(df['Region'] == 'Western Europe') | (df['Region'] == 'Central and Eastern Europe')]
	America = df[(df['Region'] == 'North America') | (df['Region'] == 'Latin America and Caribbean')]
	Asia = df[(df['Region'] == 'Southeastern Asia') | (df['Region'] == 'Eastern Asia') | (df['Region']== 'Southern Asia') ]
	Africa = df[(df['Region'] == 'Middle East and Northern Africa') | (df['Region'] == 'Sub-Saharan Africa')]

	for i in Region_SELECTED:
		if i == 'Europe':
			corr = Europe.iloc[:,3:].corr()
			mask = np.zeros_like(corr)
			mask[np.triu_indices_from(mask)] = True
			with sns.axes_style("white"):
			    f, ax = plt.subplots(figsize=(7, 5))
			    ax = sns.heatmap(corr, mask=mask, vmax=.9, square=True)
			    plt.title("Happiness Matrix in Europe")
			st.pyplot()

		elif i == 'Asia':
			corr = Asia.iloc[:,3:].corr()
			mask = np.zeros_like(corr)
			mask[np.triu_indices_from(mask)] = True
			with sns.axes_style("white"):
			    f, ax = plt.subplots(figsize=(7, 5))
			    ax = sns.heatmap(corr, mask=mask, vmax=.9, square=True)
			    plt.title("Happiness Matrix in Asia")
			st.pyplot()

		elif i == 'America':
			corr = America.iloc[:,3:].corr()
			mask = np.zeros_like(corr)
			mask[np.triu_indices_from(mask)] = True
			with sns.axes_style("white"):
			    f, ax = plt.subplots(figsize=(7, 5))
			    ax = sns.heatmap(corr, mask=mask, vmax=.9, square=True)
			    plt.title("Happiness Matrix in America")
			st.pyplot()

		elif i == 'Africa':
			corr = Africa.iloc[:,3:].corr()
			mask = np.zeros_like(corr)
			mask[np.triu_indices_from(mask)] = True
			with sns.axes_style("white"):
			    f, ax = plt.subplots(figsize=(7, 5))
			    ax = sns.heatmap(corr, mask=mask, vmax=.9, square=True)
			    plt.title("Happiness Matrix in Africa")
			st.pyplot()

		



	


def load_page():
	st.markdown("<h1 style='text-align: center;'>Heatmap of Continents</h1>", unsafe_allow_html=True)
	info()

if __name__ == "__main__":
	load_page()
