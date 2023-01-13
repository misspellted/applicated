

from applicated import Application


class GraphicalApplication(Application):
  """
  An abstract extension of the application adding an notification point to refresh the display.
  """

  def refresh(self):
    """
    Refreshes the display visible to the user.
    """
    pass

  def update(self):
    """
    By default, only calls the refresh() method to update the display.

    Any graphical-related updates required by the application should be performed prior to this call executing.
    For example, an overriding class could override GraphicalApplication::update(), performing all the graphical
      updates, then finishing with calling the overridden GraphicalApplication::update() which will update the
      display.
    """
    self.refresh()
  
