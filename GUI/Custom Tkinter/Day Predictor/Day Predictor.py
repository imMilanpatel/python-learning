# This file will predict the day of the week by taking in user input inform of a data

# Imports
import customtkinter
from PIL import Image, ImageTk

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
    input_date = entry.get()
    print(input_date)
    # Implement the functionality for the "Find!" button using input_date

# Clear button functionality
def clear_button_click():
    entry.delete(0, customtkinter.END)

def format_date(entry):
    current_text = entry.get()

    # Remove any non-digit characters
    formatted_text = ''.join(c for c in current_text if c.isdigit())

    # Format the date with slashes
    if len(formatted_text) >= 2:
        formatted_text = formatted_text[:2] + '/' + formatted_text[2:]
    if len(formatted_text) >= 5:
        formatted_text = formatted_text[:5] + '/' + formatted_text[5:]

    # Limit the year to a maximum of four characters
    if len(formatted_text) > 9:
        formatted_text = formatted_text[:9]

    entry.delete(0, customtkinter.END)
    entry.insert(0, formatted_text)


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

# Bind the format_date function to the key press event
entry.bind('<Key>', lambda event: format_date(entry))

# Create and place the "Find!" button
find_button = customtkinter.CTkButton(gui, text="Find!", command=find_button_click)
find_button.place(x= 128, y = 155)

# Create and place the "Clear" button
clear_button = customtkinter.CTkButton(gui, text="Clear", command=clear_button_click)
clear_button.place(x= 128, y= 190)


# Driver code
gui.mainloop()