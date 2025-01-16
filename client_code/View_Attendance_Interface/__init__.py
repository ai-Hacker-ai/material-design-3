from ._anvil_designer import View_Attendance_InterfaceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class View_Attendance_Interface(View_Attendance_InterfaceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    def __init__(self, **properties):
        self.init_components(**properties)
        self.student_dropdown.items = anvil.server.call('get_students')

    def view_attendance_button_click(self, **event_args):
        selected_student = self.student_dropdown.selected_value
        selected_date = self.date_picker.selected_date
        records = anvil.server.call('get_attendance', selected_student, selected_date)
        self.attendance_repeating_panel.items = records