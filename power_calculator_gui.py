import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to format the date automatically by inserting "/" after day and month
def on_date_input_change(entry_widget, value):
    # Remove all non-digit characters and limit the string length
    value = ''.join(c for c in value if c.isdigit())[:8]
    
    # Insert slashes at correct positions (DD/MM/YYYY)
    if len(value) >= 3:
        value = value[:2] + '/' + value[2:]
    if len(value) >= 6:
        value = value[:5] + '/' + value[5:]

    # Update the entry widget with the formatted value
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, value)

# Function to format the date and ensure correct date input
def format_date(date_string):
    try:
        # Format the string into a date format DD/MM/YYYY
        return datetime.strptime(date_string, "%d/%m/%Y")
    except ValueError:
        # Return None if the input is incorrect
        return None

# Function to calculate power consumption
def calculate_power_consumption():
    try:
        # Retrieve user inputs from the GUI
        begin_date_str = begin_date_entry.get()
        between_date_str = between_date_entry.get()
        end_date_str = end_date_entry.get()
        total_kwh = float(total_kwh_entry.get())

        # Convert the input strings to datetime objects
        begin_date = format_date(begin_date_str)
        between_date = format_date(between_date_str)
        end_date = format_date(end_date_str)

        # Check if the input is valid
        if not begin_date or not between_date or not end_date:
            messagebox.showerror("Input Error", "Please enter the dates in the correct format (DD/MM/YYYY).")
            return

        # Calculate the number of days between the dates
        total_days = (end_date - begin_date).days + 1  # Include the end date
        days_between_begin_and_between = (between_date - begin_date).days  # From begin to the between date (excluding the last day)
        days_between_between_and_end = (end_date - between_date).days + 1  # From between date to the end date (including the last day)

        # Calculate consumption per day
        consumption_per_day = total_kwh / total_days

        # Calculate consumption for the individual periods
        consumption_begin_to_between = consumption_per_day * days_between_begin_and_between
        consumption_between_to_end = consumption_per_day * days_between_between_and_end

        # Output the results in the GUI
        result_text.set(f"The total number of days between {begin_date_str} and {end_date_str} is: {total_days} days.\n")
        result_text.set(result_text.get() + f"Consumption per day: {consumption_per_day:.2f} kWh.\n")
        result_text.set(result_text.get() + f"\nThe number of days between {begin_date_str} and {between_date_str} (excluding the last day) is: {days_between_begin_and_between} days.\n")
        result_text.set(result_text.get() + f"Total consumption from {begin_date_str} to {between_date_str}: {consumption_begin_to_between:.2f} kWh.\n")
        result_text.set(result_text.get() + f"\nThe number of days between {between_date_str} and {end_date_str} (including the last day) is: {days_between_between_and_end} days.\n")
        result_text.set(result_text.get() + f"Total consumption from {between_date_str} to {end_date_str}: {consumption_between_to_end:.2f} kWh.\n")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {e}. Please ensure the dates are in the correct format (DD/MM/YYYY).")

# Set up the GUI window
root = tk.Tk()
root.title("Power Consumption Calculator")

# Labels for user instructions
tk.Label(root, text="Enter the begin date (DD/MM/YYYY):").pack()
begin_date_entry = tk.Entry(root)
begin_date_entry.pack()
begin_date_entry.bind("<KeyRelease>", lambda event: on_date_input_change(begin_date_entry, begin_date_entry.get()))

tk.Label(root, text="Enter the between date (DD/MM/YYYY):").pack()
between_date_entry = tk.Entry(root)
between_date_entry.pack()
between_date_entry.bind("<KeyRelease>", lambda event: on_date_input_change(between_date_entry, between_date_entry.get()))

tk.Label(root, text="Enter the end date (DD/MM/YYYY):").pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()
end_date_entry.bind("<KeyRelease>", lambda event: on_date_input_change(end_date_entry, end_date_entry.get()))

tk.Label(root, text="Enter the total power consumption in kWh over the entire period:").pack()
total_kwh_entry = tk.Entry(root)
total_kwh_entry.pack()

# Button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_power_consumption)
calculate_button.pack()

# Text widget to display the results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.pack()

# Run the GUI
root.mainloop()
