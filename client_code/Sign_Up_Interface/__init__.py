from ._anvil_designer import Sign_Up_InterfaceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Sign_Up_Interface(Sign_Up_InterfaceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def signup_submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    first_name = self.first_name_textbox.text
    last_name = self.last_name_textbox.text
    staff_id = self.staff_id_textbox.text
    role = self.role_dropdown.selected_value
    username = first_name.replace(" ", "").lower()
    
    anvil.server.call('create_user', username, "default_password", first_name, last_name, staff_id, role)
    alert("Account created successfully! Please log in.")
    open_form('Login_Interface')
    pass
  