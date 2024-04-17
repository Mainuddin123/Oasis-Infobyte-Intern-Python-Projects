import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        bmi_label.config(text=f"BMI: {bmi:.2f}")

        category = classify_bmi(bmi)
        category_label.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create input fields
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, columnspan=2)

# Create labels to display BMI result and category
bmi_label = tk.Label(root, text="BMI:")
bmi_label.grid(row=3, columnspan=2)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=4, columnspan=2)

# Run the application
root.mainloop()
