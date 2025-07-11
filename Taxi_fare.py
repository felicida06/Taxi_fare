import os
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ---- Load your trained RandomForest model ----
with open('Downloads/Feli python prog/project 3/best_random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("NYC Taxi Fare Prediction App 🚖")
st.write("Enter trip details below to predict the total fare amount.")

st.header("Trip Details:")

# ---- Input widgets ----
VendorID = st.selectbox("VendorID", [1, 2])
RatecodeID = st.selectbox("RatecodeID", [1, 2, 3, 4, 5, 6])
store_and_fwd_flag = st.radio("Store and Forward Flag", [0, 1], format_func=lambda x: "Yes" if x else "No")
payment_type = st.selectbox("Payment Type", [1, 2, 3, 4, 5, 6])
pickup_weekday = st.selectbox("Pickup Weekday (0=Monday)", list(range(7)), format_func=lambda x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][x])
is_weekend = st.radio("Is Weekend?", [0, 1], format_func=lambda x: "Yes" if x else "No")
am_pm = st.radio("AM or PM?", [0, 1], format_func=lambda x: "AM" if x == 0 else "PM")
is_night = st.radio("Is Night?", [0, 1], format_func=lambda x: "Yes" if x else "No")

trip_distance_km = st.number_input("Trip Distance (km)", min_value=0.1, step=0.1, value=2.0)
trip_duration_minutes = st.number_input("Trip Duration (minutes)", min_value=1.0, step=1.0, value=10.0)
avg_speed_kmh = st.number_input("Average Speed (km/h)", min_value=1.0, step=0.5, value=20.0)
total_surcharges = st.number_input("Total Surcharges ($)", min_value=0.0, step=0.1, value=0.0)
tip_percentage = st.number_input("Tip Percentage (%)", min_value=0.0, step=0.1, value=10.0)

is_zero_passenger = st.radio("Is Zero Passenger?", [0, 1], format_func=lambda x: "Yes" if x else "No")

pickup_day_of_month = st.slider("Pickup Day of Month", 1, 31, 15)
pickup_month = st.slider("Pickup Month", 1, 12, 6)
pickup_year = st.selectbox("Pickup Year", [2016, 2017, 2018, 2019, 2020])
rush_hour = st.radio("Rush Hour?", [0, 1], format_func=lambda x: "Yes" if x else "No")

# ---- Predict button ----
if st.button("Predict Fare"):
    

    # Arrange input data in correct order
    input_data = pd.DataFrame([[
        VendorID,
        RatecodeID,
        store_and_fwd_flag,
        payment_type,
        pickup_weekday,
        is_weekend,
        am_pm,
        is_night,
        trip_distance_km,
        trip_duration_minutes,
        avg_speed_kmh,
        total_surcharges,
        tip_percentage,
        is_zero_passenger,
        pickup_day_of_month,
        pickup_month,
        pickup_year,
        rush_hour,
        
    ]], columns=[
        'VendorID',
        'RatecodeID',
        'store_and_fwd_flag',
        'payment_type',
        'pickup_weekday',
        'is_weekend',
        'am_pm',
        'is_night',
        'trip_distance_km',
        'trip_duration_minutes',
        'avg_speed_kmh',
        'total_surcharges',
        'tip_percentage',
        'is_zero_passenger',
        'pickup_day_of_month',
        'pickup_month',
        'pickup_year',
        'rush_hour',
        
    ])

    # ---- Make prediction ----
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Total Fare Amount: ${prediction:.2f}")