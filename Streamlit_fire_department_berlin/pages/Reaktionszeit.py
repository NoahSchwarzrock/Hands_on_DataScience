import streamlit as st
import pandas as pd
from app import df
import plotly.express as px

st.header("Datumsbereich auswählen")

date_range = st.date_input(
    "Datumsbereich:",
    (df.index.min(), df.index.max()),
    min_value=df.index.min(),
    max_value=df.index.max()
)

filtered_df = df[(df.index >= pd.to_datetime(min(date_range))) & (df.index <= pd.to_datetime(max(date_range)))]

st.header("Boxplot zur durchschnittlichen Reaktionszeit")

response_time_cols = [col for col in df.columns if "response" in col and "mean" in col]

df_response_mean_filtered = filtered_df[response_time_cols]

df_melted = pd.melt(
    df_response_mean_filtered.reset_index(),
    id_vars=["mission_created_date"],
    value_vars=response_time_cols,
    var_name="Einsatzart",
    value_name="Reaktionszeit",
)

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
