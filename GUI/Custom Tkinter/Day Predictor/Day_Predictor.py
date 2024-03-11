# This file will predict the day of the week by taking in user input inform of a data

# Imports
import customtkinter
from PIL import Image, ImageTk

#########################################################################
# Constants, these serves in the main logic

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

year_ranges = {
    (1600, 1699): 6,
    (1700, 1799): 4,
    (1800, 1899): 2,
    (1900, 1999): 0,
    (2000, 2099): 6,
    (2100, 2199): 4,
    (2200, 2299): 2,
    (2300, 2399): 0,
    (2400, 2499): 6,
    (2500, 2599): 4,
    (2600, 2699): 2,
    (2700, 2799): 0,
    (2800, 2899): 6,
    (2900, 2999): 4,
    (3000, 3099): 2,
    (3100, 3199): 0

}

##########################################################

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

########################################################################

# All the functions definitions

# Global Variables
display_box = None

# Displays the result on the screen
def display_message(string):
    global display_box
    display_box = customtkinter.CTkLabel(gui, text=string, font=("Helvetica", 12), padx=10, pady=10)
    display_box.place(x=125, y=114)
    return display_box

# Functionality to remove the Result label from the screen
def destroy_fun():
    global display_box
    if display_box:
        display_box.destroy()

# Find button functionality (Main Logic)
def find_button_click():
    
    # Getting the input from user typed text and slicing the input
    input_date = entry.get()
    date = int(input_date[:2])
    month = int(input_date[3:5])
    year = int(input_date[6:10])
    last_two_digits_of_year = year % 100

    # Core logic of the application
    
    # Empty list which will be populated with some values
    values = []

    # STEP 1 
    values.append(last_two_digits_of_year)

    # STEP 2
    quotient_value = last_two_digits_of_year / 4
    values.append(quotient_value)

    # STEP 3
    values.append(date)

    # STEP 4
    values.append(month_codes[month])

    # STEP 5
    for year_range, value in year_ranges.items():
        if year_range[0] <= year <= year_range[1]:
            values.append(value)
            break
    else:
        display_message("Year entered in out of range!")

    
    # STEP 6
    grand_total = sum(values)

    # STEP 7
    day_key = grand_total % 7
    answer = days[day_key]
    display_message(f"------ It's {answer} ------")
    
# Clear button functionality
def clear_button_click():
    entry.delete(0, customtkinter.END)
    destroy_fun()
        
#######################################################################

# GUI Widgets

# Load the image
image_path = r".\images-bkgrd\bakground.png"  # Replace with the path to your image
original_image = Image.open(image_path)
resized_image = original_image.resize((gui_width, gui_height))
background_image = ImageTk.PhotoImage(resized_image)

# Set the image as the background
background_label = customtkinter.CTkLabel(gui, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place the entry widget
entry_label = customtkinter.CTkLabel(gui, text="Enter Date (dd/mm/yyyy):")
entry_label.place(x=125, y=40)
entry = customtkinter.CTkEntry(gui)
entry.place(x=125, y=80)

# Create and place the "Find!" button
find_button = customtkinter.CTkButton(gui, text="Find!", command=find_button_click)
find_button.place(x= 128, y = 155)

# Create and place the "Clear" button
clear_button = customtkinter.CTkButton(gui, text="Clear", command=clear_button_click)
clear_button.place(x= 128, y= 190)

# Driver code
gui.mainloop()