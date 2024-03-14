# This file will have the Objects that are present in Login Page of OrangeHRM Demo Page

# Class Definition
class LoginPage:

    # Constructor method
    def __init__(self, page) -> None:
        self.page = page
        
        #Login Page elements IDs
        self.username_input_box = page.locator()
        self.password_input_box = page.locator()
        self.login_button = page.locator()

    # Navigates to Login Page
    def navigate_to_login_page(self) -> None:
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Inputs username
    def username(self) -> None:
        self.username_value = "Admin"
        self.username_input_box.fill(self.username_value)

    # Inputs password    
    def password(self) -> None:
        self.passsword_value = "admin123"
        self.username_input_box.fill(self.password_value)

    # Clicks login button
    def click_login_button(self) -> None:
        self.login_button.click()