import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#@anvil.server.callable


@anvil.server.callable
def create_user(username, password, first_name, last_name, staff_id, role):
    app_tables.users.add_row(username=username, password=password, first_name=first_name, last_name=last_name, staff_id=staff_id, role=role)

@anvil.server.callable
def get_user(username, password):
    # Fetch the user from the Users table
    user = app_tables.users.get(username=username, password=password)
    return user  # This will return the user record if found, or None if not

@anvil.server.callable
def add_attendance(student, date, status):
    app_tables.attendance.add_row(student=student, date=date, status=status)

@anvil.server.callable
def get_attendance(student, date):
    return app_tables.attendance.search(student=student, date=date)

@anvil.server.callable
def mark_attendance(student_id, date, status):
    # Check if attendance for the student on that date already exists
    existing_record = app_tables.attendance.get(student=student_id, date=date)
    if existing_record:
        existing_record['status'] = status  # Update existing record
    else:
        add_attendance(student_id, date, status)  # Add new record
