'''
to run ,do not click the play button, in the terminal type:
  cd app_one
  streamlit run app.py
  '''

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
     page_title='App One',
     page_icon='1️⃣',
     layout='wide',
)

@st.cache
def load_data():
    return pd.read_csv("cps_85_wages.csv")
st.title('streamlit data one')
st.subheader('very easy data analytics in python')

df = load_data()
st.dataframe(df)

st.sidebar.header('Select Option')
if st.sidebar.checkbox('Show Pivot Table Summary'):
    st.subheader("Pivot Table Summary")
    c1, c2 = st.columns(2)
    categorical_cols = df.select_dtypes(exclude=np.number).columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    index_cols = c1.selectbox('Pivot Index',options = categorical_cols)
    values_cols = c1.multiselect('Pivot Values',options=numeric_cols)
    func = c1.selectbox('Pivot Function',options=['mean','sum','count','min','max','std'])
    pivot_df =df.pivot_table(index=index_cols,values=values_cols,aggfunc=func)
    c2.dataframe(pivot_df)
    for col in values_cols:
        fig = px.pie(pivot_df,values=col, names=pivot_df.index)
        st.plotly_chart(fig)