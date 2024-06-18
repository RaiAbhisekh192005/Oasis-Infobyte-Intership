import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height / 100) ** 2
        bmi = round(bmi, 2)
        result.set(f"BMI: {bmi}")
        if bmi < 18.5:
            category.set("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            category.set("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            category.set("Category: Overweight")
        else:
            category.set("Category: Obesity")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

# Initialize the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Create and place the widgets
tk.Label(root, text="Height (cm):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Label(root, text="Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

result = tk.StringVar()
category = tk.StringVar()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Label(root, textvariable=result, font=('Helvetica', 14)).pack(pady=5)
tk.Label(root, textvariable=category, font=('Helvetica', 14)).pack(pady=5)

# Run the application
root.mainloop()
