from ._anvil_designer import Add_Student_InterfaceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Add_Student_Interface(Add_Student_InterfaceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_student_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    first_name = self.student_first_name_textbox.text
    last_name = self.student_last_name_textbox.text
    student_id = self.student_id_textbox.text
        
    anvil.server.call('add_student', first_name, last_name, student_id)
    alert("Student added successfully!")
    pass
