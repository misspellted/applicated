

import applicated.graphical
import pygame


class PyGameApp(applicated.graphical.GraphicalApplication):
  def __init__(self, length=640, height=360):
    pygame.init()
    applicated.graphical.GraphicalApplication.__init__(self)
    self.display = pygame.display.set_mode((length, height))

  def caption(self, text):
    """
    Updates the caption of the window.
    """

    # TODO: Ignore changing the caption if in full-screen mode?
    pygame.display.set_caption(text)

  def handle(self, event):
    print(event)

  def process(self):
    """
    Processes the pygame event queue.

    The QUIT event is handled internally by calling the ::stop method, setting
    up the termination sequence.

    Any other event (for now) is forwarded to ::handle(event) for further
    processing.
    """

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.stop()
        break
      else:
        self.handle(event)

  def refresh(self):
    pygame.display.flip()

  def stop(self):
    applicated.graphical.GraphicalApplication.stop(self)
    pygame.quit()


if __name__ == "__main__":
  app = PyGameApp()
  app.caption("This is not the game you are looking for.")
  app.start()

