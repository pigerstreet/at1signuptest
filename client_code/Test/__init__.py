from ._anvil_designer import TestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import login_flow

class Test(TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.update_login_status()
    
  def update_login_status (self):
    user = anvil.users.get_user()
    if user is None:
      self.login_status_lbl.text = "You are not logged in."
    else:
      self.login_status_lbl.text = "You are logged in as %s" % user['email']

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    login_flow.login_with_form()
    self.update_login_status()

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    self.update_login_status()

  def signup_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    login_flow.signup_with_form()





