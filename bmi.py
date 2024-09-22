import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # Convert height to meters
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Tracker")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Enter your height (cm):").grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1)

tk.Label(root, text="Enter your weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, columnspan=2)

# Start the main loop
root.mainloop()
