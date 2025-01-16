import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def load_df(location):
    ### Load dataframe ###
    df = pd.read_csv(location).iloc[:-1]

    ### Convert mission_created_date to datetime and set as index ###
    df["mission_created_date"] = pd.to_datetime(df["mission_created_date"])
    df = df.set_index("mission_created_date").sort_index()

    ### convert types of columns to int or float ###
    for col in df.columns:
        try:
            df[col] = df[col].astype(int)
        except:
            df[col] = df[col].astype(float)
    return df

df = load_df("data/BFw_mission_data_daily.csv")