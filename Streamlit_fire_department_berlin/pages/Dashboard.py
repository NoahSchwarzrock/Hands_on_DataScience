import streamlit as st
import pandas as pd
from app import df
import plotly.express as px

st.header("Aufgabe 2.1")
# Aufgabe 2.1.1
selected_cols = st.multiselect("Wähle die Spalten aus, nach denen zu filter möchtest", df.columns)

date_range = st.date_input(
    "Datumsbereich", 
    (df.index.min(), df.index.max()), 
    min_value=df.index.min(),
    max_value=df.index.max())

if selected_cols:
    filtered_df = df[(df.index >= pd.to_datetime(min(date_range))) & (
        df.index <= pd.to_datetime(max(date_range)))][selected_cols]
    
    aggregation_type = st.radio("Aggregationsart.", ("Summe", "Mittelwert"))
    
    aggregation = st.radio("Zeitraum Wählen", ("Tag", "Woche", "Monat", "Jahr"))
    
    if aggregation == "Tag":
        resolution = "D"
    elif aggregation == "Woche":
        resolution = "W"
    elif aggregation == "Tag":
        resolution = "ME"
    else:
        resolution = "YE"
        
    if aggregation_type == "Summe":
        filtered_and_aggregated_df = filtered_df[selected_cols].resample(resolution).sum()
    if aggregation_type == "Mittelwert":
        filtered_and_aggregated_df = filtered_df[selected_cols].resample(resolution).mean()
        
    with st.expander("Dataframe ansehen"):
        st.write(filtered_and_aggregated_df)
    with st.expander("Grafik ansehen"):
        st.line_chart(filtered_and_aggregated_df[selected_cols])
    with st.expander("Grafik mit plotly"):
        fig = px.line(filtered_and_aggregated_df[selected_cols])
        st.plotly_chart(fig)