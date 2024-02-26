# This is a basic file to demonstrate the usage of Custom Tkinter Library
# Make sure you have installed the "customtkinter" library package using pip command before using this.

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

#TODO: Need to implement login functionality !!!!!!!
def login():
    print("Test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

username_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username_entry.pack(pady=12, padx=10)

password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entry.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=frame, text="Login", command= login)
login_button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me?")
checkbox.pack(pady=12,padx=10)

root.mainloop()