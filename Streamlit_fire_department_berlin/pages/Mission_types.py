import streamlit as st
from app import df
import pandas as pd
import plotly.express as px

st.header("Aufgabe 2.5")

df_agg = df.agg("sum")

df_agg_reset = pd.DataFrame({"Spalten": df_agg.index, "Summen": df_agg.values})

st.write(df_agg)
st.write(df_agg_reset)

st.write(px.pie(df_agg_reset, names="Spalten", values="Summen"))