import streamlit as st
import pandas as pd
from app import df
import plotly.express as px

st.header("Aufgabe 2.4")

date_range = st.date_input("Datumsbereich:",
                           (df.index.min(), df.index.max())
                           , min_value = df.index.min(), max_value = df.index.max())

filtered_df = df[["response_time_ems_critical_mean", "response_time_fire_time_to_first_pump_mean"]]

st.write(filtered_df[(filtered_df.index >= pd.to_datetime(min(date_range))) & (filtered_df.index <= pd.to_datetime(max(date_range)))])


st.header("Aufgabe 2.7")


response_time_cols = [col for col in df.columns if "response" in col and "mean" in col]

df_response_mean = df[response_time_cols]

df_melted = pd.melt(
    df_response_mean.reset_index(),
    id_vars=["mission_created_date"],
    value_vars=response_time_cols,
    var_name="Einsatzart",
    value_name="Reaktionszeit",
)

# Boxplot erstellen
fig = px.box(
    df_melted,
    x="Einsatzart",
    y="Reaktionszeit",
    title="Verteilung der Reaktionszeiten nach Einsatzart",
    labels={"Einsatzart": "Einsatzart", "Reaktionszeit": "Reaktionszeit (Minuten)"},
    color="Einsatzart",
    width=1200,
    height=600,
)

st.plotly_chart(fig)