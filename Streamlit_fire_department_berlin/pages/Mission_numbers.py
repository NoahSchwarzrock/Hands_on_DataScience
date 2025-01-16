import streamlit as st
from app import df
import pandas as pd
import plotly.express as px

st.header("Aufgabe 2.6")

fig = px.line(df, x=df.index, y="mission_count_all")

st.plotly_chart(fig)