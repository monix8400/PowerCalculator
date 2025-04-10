import streamlit as st
from datetime import datetime

# Titlu aplicație
st.title("Power Consumption Calculator")

# Inputuri de la utilizator
begin_date = st.date_input("Enter the begin date:", value=None)
between_date = st.date_input("Enter the between date:", value=None)
end_date = st.date_input("Enter the end date:", value=None)
total_kwh = st.number_input("Enter the total power consumption in kWh over the entire period:", min_value=0.0, format="%.2f")

# Buton de calcul
if st.button("Calculate"):

    if not begin_date or not between_date or not end_date:
        st.error("Please enter the dates in the correct format (DD/MM/YYYY).")
    else:
        total_days = (end_date - begin_date).days + 1
        days_begin_to_between = (between_date - begin_date).days
        days_between_to_end = (end_date - between_date).days + 1

        if total_days <= 0 or days_begin_to_between < 0 or days_between_to_end < 0:
            st.error("Invalid date range. Make sure the dates are in chronological order.")
        else:
            consumption_per_day = total_kwh / total_days
            consumption_begin_to_between = consumption_per_day * days_begin_to_between
            consumption_between_to_end = consumption_per_day * days_between_to_end

            st.success(f"Total number of days: {total_days} days")
            st.write(f"Consumption per day: {consumption_per_day:.2f} kWh")

            st.markdown("---")
            st.write(f"From {begin_date_str} to {between_date_str} (excluding last day): {days_begin_to_between} days")
            st.write(f"Consumption: {consumption_begin_to_between:.2f} kWh")

            st.markdown("---")
            st.write(f"From {between_date_str} to {end_date_str} (including last day): {days_between_to_end} days")
            st.write(f"Consumption: {consumption_between_to_end:.2f} kWh")
