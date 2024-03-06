# This file will predict the day of the week by taking in user input inform of a data

# Imports
import customtkinter

# GUI customization
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui.geometry("500x350")

def find_button_click():
    input_date = entry.get()
    # Implement the functionality for the "Find!" button using input_date

# Create and place the entry widget
entry_label = customtkinter.CTkLabel(gui, text="Enter Date (dd/mm/yyyy):")
entry_label.pack(pady=10)
entry = customtkinter.CTkEntry(gui)
entry.pack(pady=10)

# Create and place the "Find!" button
find_button = customtkinter.CTkButton(gui, text="Find!", command=find_button_click)
find_button.pack(pady=10)


# Driver code
gui.mainloop()