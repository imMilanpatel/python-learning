# This file will have the Objects that are present in Login Page of OrangeHRM Demo Page

# Class Definition
class LoginPage:

    # Constructor method
    def __init__(self, page) -> None:
        self.page = page
        
        #Login Page elements IDs
        self.username_input_box = page.get_by_placeholder("Username")
        self.password_input_box = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    # Navigates to Login Page
    def navigate_to_login_page(self,url) -> None:
        self.page.goto(url)
    
    # Inputs username
    def username(self, username_credential) -> None:
        self.username_input_box.fill(username_credential)

    # Inputs password    
    def password(self,password_credential) -> None:
        self.password_input_box.fill(password_credential)

    # Clicks login button
    def click_login_button(self) -> None:
        self.login_button.click()