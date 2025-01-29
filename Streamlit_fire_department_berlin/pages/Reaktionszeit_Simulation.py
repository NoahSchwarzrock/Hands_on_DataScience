from app import load_df
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = load_df("data/BFw_mission_data_daily.csv")

### Heading ###
st.header("Reaktionszeit Simulation")

### User input ###
mission_count_fire_user = st.slider("Einsätze wegen Brand (pro Tag):", min_value=0, max_value=10000)

### User input ###
mission_count_ems_critical_user = st.slider("Einsätze kritisch (pro Tag):", min_value=0, max_value=10000)

### Dataframe of user input ###
df_user = pd.DataFrame({"mission_count_fire": [mission_count_fire_user], "mission_count_ems_critical": [mission_count_ems_critical_user]})

## Linear regression model ###

X = df[["mission_count_fire", "mission_count_ems_critical"]]

y = df["response_time_fire_time_to_first_pump_mean"]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=73)

model = LinearRegression()

model.fit(X_train, y_train)

predicted_values = model.predict(X_test)

### User input prediction ###

predicted_values_user = model.predict(df_user)

st.write("Vorhergesagte Reaktionszeit bis zur Ankunft am Einsatzort (in sekunden):", predicted_values_user)


### Mean squared error value ###
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
st.write(f"Mean Squared Error (MSE): {mse:.2f}")
