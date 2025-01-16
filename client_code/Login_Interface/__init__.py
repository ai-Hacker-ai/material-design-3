from ._anvil_designer import Login_InterfaceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login_Interface(Login_InterfaceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    def login_button_click(self, **event_args):
        username = self.username_textbox.text
        password = self.password_textbox.text
        user = anvil.server.call('get_user', username, password)
        if user:
            open_form('Student Attendance Tracker')  # Change to your main app form name
        else:
            alert("Invalid credentials")

    def signup_button_click(self, **event_args):
        open_form('Sign_Up_Interface')