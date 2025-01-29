import streamlit as st
import pandas as pd
from app import df
import plotly.express as px

st.title("Datenanalyse Dashboard")

selected_cols = st.multiselect("Wähle die Spalten zum Filtern", df.columns)

date_range = st.date_input(
    "Zeitraum auswählen", 
    (df.index.min(), df.index.max()), 
    min_value=df.index.min(),
    max_value=df.index.max())

if selected_cols:
    filtered_df = df[(df.index >= pd.to_datetime(min(date_range))) & (
        df.index <= pd.to_datetime(max(date_range)))][selected_cols]
    
    aggregation_type = st.radio("Aggregationsart", ("Summe", "Mittelwert"), horizontal=True)
    aggregation = st.radio("Zeitraum wählen", ("Täglich", "Wöchentlich", "Monatlich", "Jährlich"), horizontal=True)
    
    resolution = {"Täglich": "D", "Wöchentlich": "W", "Monatlich": "ME", "Jährlich": "YE"}.get(aggregation, "D")
    
    filtered_and_aggregated_df = (
        filtered_df[selected_cols].resample(resolution).sum()
        if aggregation_type == "Summe" else
        filtered_df[selected_cols].resample(resolution).mean()
    )
    
    with st.expander("Daten anzeigen"):
        st.dataframe(filtered_and_aggregated_df)
    with st.expander("Liniendiagramm"):
        st.line_chart(filtered_and_aggregated_df[selected_cols])
    with st.expander("Interaktive Grafik"):
        fig = px.line(filtered_and_aggregated_df[selected_cols])
        st.plotly_chart(fig)
