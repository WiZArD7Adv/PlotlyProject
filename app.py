import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px


df = pd.read_csv('india.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)
st.set_page_config(layout='wide')

def get_info_overall(pri,sec):
    st.write( 'Primary Parameter as size of dots')
    st.write( 'Secondary Parameter as color of dots')
    fig = px.scatter_map(df, lat="Latitude", lon="Longitude", size_max=25, zoom=5, size=pri, color=sec,height=700,width=1200,map_style="carto-positron",hover_name='District',color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig, use_container_width=True)






def get_info_state(state,pri,sec):
    st.write('Primary Parameter as size of dots')
    st.write('Secondary Parameter as color of dots')
    df_state = df[df['State'] == state]
    fig = px.scatter_map(df_state, lat="Latitude", lon="Longitude", size_max=25, zoom=5, size=pri, color=sec, height=700,
                         width=1200, map_style="carto-positron", hover_name='District',
                         color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig, use_container_width=True)




st.sidebar.title('India Map')

a = st.sidebar.selectbox('Select',['Overall','State'])

if a == 'State':
    state = st.sidebar.selectbox('Select State',df['State'].unique())

pri = st.sidebar.selectbox('Select Primary Parameter',np.array(df.columns)[5:])

sec = st.sidebar.selectbox('Select Secondary Parameter',np.array(df.columns)[5:])

btn = st.sidebar.button('Plot')

if btn:
    if a == 'Overall':
        get_info_overall(pri,sec)


    if a == 'State':

        get_info_state(state,pri,sec)

