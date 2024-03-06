# This file will predict the day of the week by taking in user input inform of a data

# Imports
import customtkinter
from PIL import Image, ImageTk

# Constants
days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"

}

month_codes = {
    1 : 0, # January
    2 : 3, # February
    3 : 3, # March
    4 : 6, # April
    5 : 1, # May
    6 : 4, # June
    7 : 6, # July
    8 : 2, # August
    9 : 5, # September
    10 : 0, # October
    11 : 3, # November
    12 : 5, # December
}

# GUI customization
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
gui = customtkinter.CTk()
gui_width = 400
gui_height = 400
gui_x = str(gui_width)
gui_y = str(gui_height)
gui.geometry(f"{gui_x}x{gui_y}")
gui.resizable(width=False, height=False)

# Find button functionality (Main Logic)
def find_button_click():
    
    # Getting the input from user typed text and splitting the input
    # Also, date, month and year are stored in seprate variables
    input_date = entry.get()
    date = int(input_date[:2])
    month = int(input_date[3:5])
    year = int(input_date[6:10])
    
    
    

# Clear button functionality
def clear_button_click():
    entry.delete(0, customtkinter.END)
    
#######################################################################

# Load the image
image_path = r"GUI\Custom Tkinter\Day Predictor\images-bkgrd\bakground.png"  # Replace with the path to your image
original_image = Image.open(image_path)
resized_image = original_image.resize((gui_width, gui_height))
background_image = ImageTk.PhotoImage(resized_image)

# Set the image as the background
background_label = customtkinter.CTkLabel(gui, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place the entry widget
entry_label = customtkinter.CTkLabel(gui, text="Enter Date (dd/mm/yyyy):")
entry_label.place(x=125, y=60)
entry = customtkinter.CTkEntry(gui)
entry.place(x=125, y=100)

# Create and place the "Find!" button
find_button = customtkinter.CTkButton(gui, text="Find!", command=find_button_click)
find_button.place(x= 128, y = 155)

# Create and place the "Clear" button
clear_button = customtkinter.CTkButton(gui, text="Clear", command=clear_button_click)
clear_button.place(x= 128, y= 190)

# Driver code
gui.mainloop()