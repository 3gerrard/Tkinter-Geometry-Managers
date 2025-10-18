import tkinter as tk
from datetime import date

# Function to calculate age and display message
def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        birth_date = date(year, month, day)
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_text.config(state='normal')  # Enable editing the Text widget
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Hello {name}!\nYou are {age} years old.")
        result_text.config(state='disabled')  # Disable editing again
    except ValueError:
        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid date, month, and year.")
        result_text.config(state='disabled')

# Create main window
window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")
window.configure(bg="#f9f9f9")  # Light background

# Heading
heading = tk.Label(window, text="Age Calculator", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#2e3f4f")
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Name
tk.Label(window, text="Name:", bg="#f9f9f9", fg="#333").grid(row=1, column=0, sticky='e', padx=10, pady=5)
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=1, column=1, pady=5)

# Day
tk.Label(window, text="Day:", bg="#f9f9f9", fg="#333").grid(row=2, column=0, sticky='e', padx=10, pady=5)
day_entry = tk.Entry(window, width=25)
day_entry.grid(row=2, column=1, pady=5)

# Month
tk.Label(window, text="Month:", bg="#f9f9f9", fg="#333").grid(row=3, column=0, sticky='e', padx=10, pady=5)
month_entry = tk.Entry(window, width=25)
month_entry.grid(row=3, column=1, pady=5)

# Year
tk.Label(window, text="Year:", bg="#f9f9f9", fg="#333").grid(row=4, column=0, sticky='e', padx=10, pady=5)
year_entry = tk.Entry(window, width=25)
year_entry.grid(row=4, column=1, pady=5)

# Calculate button
calc_button = tk.Button(window, text="Calculate Age", command=calculate_age,
                        bg="#4a90e2", fg="white", activebackground="#357ABD")
calc_button.grid(row=5, column=0, columnspan=2, pady=15)

# Result box
result_text = tk.Text(window, height=4, width=35, bg="#e6f7ff", fg="#000")
result_text.grid(row=6, column=0, columnspan=2, pady=10)
result_text.config(state='disabled')  # Initially read-only

# Run the application
window.mainloop()
