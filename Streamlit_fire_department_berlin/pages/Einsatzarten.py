import streamlit as st
from app import df
import pandas as pd
import plotly.express as px

st.header("Einsatzarten und Reaktionszeiten")

df_agg = df.agg("sum")

df_agg_reset = pd.DataFrame({"Einsatzarten und Reaktionszeiten": df_agg.index, "Anzahl und Totale Zeit": df_agg.values})
st.write(df_agg_reset)

st.header("Visualisierung im Pie-Chart")
st.write(px.pie(df_agg_reset, names="Einsatzarten und Reaktionszeiten", values="Anzahl und Totale Zeit"))