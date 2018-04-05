from mario import mario
from model import model
from pygame import display, event, init, key, mouse, MOUSEBUTTONUP
from pygame.locals import K_CTRL, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, KEYUP, QUIT
from reducer import reducer
from time import sleep

init()

# Controller
class Controller():
  def __init__(self, model, view, reducer):
    self.exit = False
    self.model = model
    self.reducer = reducer
    self.view = view

  def animationFrame(self):
    for e in event.get():
      if e.type == QUIT:
        self.exit = True
      elif e.type == KEYDOWN:
        if e.key == K_ESCAPE:
          self.exit = True
      elif e.type == KEYUP:
        if e.key == K_CTRL:
          self.reducer('SHOOT_FIREBALL')
        elif e.key == K_LEFT:
          self.reducer('BRAKE_LEFT')
        elif e.key == K_RIGHT:
          self.reducer('BRAKE_RIGHT')
      # elif e.type == MOUSEBUTTONUP:
        # self.model.set_dest(mouse.get_pos())



# Goomba
class Goomba():
  def __init__(self, x, y):
    self.x = x
    self.y = y




# View
class View():
  def __init__(self, model):
    self.screen = display.set_mode((640, 480), 32)
    # self.turtle_image = pygame.image.load("turtle.png")
    self.model = model
    # self.model.rect = self.turtle_image.get_rect()

  def draw(self):    
    self.screen.fill([0, 0, 0])
    # self.screen.blit(self.turtle_image, self.model.rect)
    display.flip()

view = View(model)
controller = Controller(model, view, reducer)

while not controller.exit:
  controller.animationFrame()
  view.draw()
