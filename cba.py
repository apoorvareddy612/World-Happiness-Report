import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv('data/happiness_combined_year copy 2.csv')
df = df.drop(columns=['Unnamed: 0'],axis=1)

def plot_fac(df):
	    plt.figure(figsize=(16,8))
	    d = {1:['Economy (GDP per Capita)','red'],2:['Family','blue'],3:['Health (Life Expectancy)','green'],4:['Freedom','yellow'],5:['Trust (Government Corruption)','orange'],6:['Generosity','magenta']}
	    for key,value in d.items():
	        plt.subplot(3, 2, key)
	        sns.pointplot(x = "Year",
	                      y = value[0],
	                      data = df,color=value[1])
def plot(lst,data=df):
	for i in lst:
		d = data[data['Country'] == i]
		sns.pointplot(x = "Year",
              y = "Happiness Rank",
              data = d)
		plt.title(i)
		st.pyplot()
		plot_fac(d)
		st.pyplot()

def info():
	df = pd.read_csv('data/happiness_combined_year copy 2.csv')
	df = df.drop(columns=['Unnamed: 0'],axis=1)

	COUNTRIES = df['Country'].unique()
	COUNTRIES_SELECTED = st.multiselect('Select countries', COUNTRIES)

	# Mask to filter dataframe
	mask_countries = df['Country'].isin(COUNTRIES_SELECTED)

	df = df[mask_countries]

	

	plot(COUNTRIES_SELECTED)





	
	

    
    
def load_page():
	st.markdown("<h1 style='text-align: center;'>Country based analysis</h1>", unsafe_allow_html=True)
	info()
    

if __name__ == "__main__":
	load_page()
