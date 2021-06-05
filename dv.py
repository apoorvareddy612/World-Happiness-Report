import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import SessionState
import cba
import avg
import spatial
import con
import graph
import rank
import seaborn as sns
import matplotlib.pyplot as plt
import histo

def side_bar_homepage():
    st.sidebar.title("Team Members")
    st.sidebar.info("""Apoorva Reddy 19BCE2196""")
    st.sidebar.info("""Shubh Almal 19BCE2130""")
    st.sidebar.info("""Diva Bhatia 19BCE2452""")

def homepage():
	st.markdown("<h1 style='text-align: center;'>WORLD HAPPINESS REPORT</h1>", unsafe_allow_html=True)
	st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)
	st.write("We are going to visualise what are the factors and which countries have the most happy population.")
	st.write("The World Happiness Report is a publication of the Sustainable Development Solutions Network, powered by data from the Gallup World Poll and Lloyd’s Register Foundation, who provided access to the World Risk Poll.")
	st.markdown(f"**Data source and information about data collect can be found on [Kaggle](https://www.kaggle.com/unsdsn/world-happiness)**")
	st.markdown("We have visualized the dataset all way possible trying to interpret and analyse using diffrent factors which is playing important role in deciding the happiness score.There are different criteria defined in the report:")
	criteria_list = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)','Freedom', 'Trust (Government Corruption)', 'Generosity']

	for i in criteria_list:
		st.markdown('**'+i+'**')

	st.write("We have used these visualization tools:")
	st.image("Image/tool.png",use_column_width=True)
    	


def createlayout():
#     st.sidebar.title("Menu")
    query_params = st.experimental_get_query_params()
    app_check = st.experimental_get_query_params()

    session_state = SessionState.get(first_query_params=query_params)
    first_query_params = session_state.first_query_params

    app_check = {k: v[0] if isinstance(v, list) else v for k, v in app_check.items()}
    st.sidebar.title("Menu")
    page_list = ["Homepage", "Country based analysis", "Average based analysis", "Spatial based analysis","Heatmap of Continents","Scatter plots","Rank based Analysis","Histogram of Scores Distribution"]
#     default_selectbox = int(app_check["selectbox"]) if "selectbox" in app_check else 0
    default_selectbox = int(app_check["selectbox"]) if "selectbox" in app_check else 0
    app_mode = st.sidebar.selectbox("Please select a page", page_list,index = default_selectbox)
    if app_mode:
#         app_check["selectbox"] = page_list.index(app_mode)
#         st.experimental_set_query_params(**app_check)
        app_check["selectbox"] = page_list.index(app_mode)
        st.experimental_set_query_params(**app_check)
#     app_mode = st.sidebar.selectbox("Please select a page", ["Homepage", "Gender Gap", "Popular YouTubers"])
        if app_mode == "Homepage":
            homepage()
        elif app_mode == "Country based analysis":
            cba.load_page()
        elif app_mode == "Average based analysis":
            avg.load_page()
        elif app_mode == "Spatial based analysis":
            spatial.viz_page()
        elif app_mode == "Heatmap of Continents":
            con.load_page()
        elif app_mode == "Scatter plots":
            graph.load_page()
        elif app_mode == "Rank based Analysis":
            rank.load_page()
        elif app_mode == "Histogram of Scores Distribution":
            histo.load_page()

def main():
    createlayout()
    side_bar_homepage()

if __name__ == "__main__":
    main()

