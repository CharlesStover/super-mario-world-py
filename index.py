import pygame
from mario import mario
from model import model
from reducer import reducer

pygame.init()

# Controller
class Controller():
  def __init__(self, model, view):
    self.exit = False
    self.model = model
    self.view = view

  def animationFrame(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.exit = True

      # Key Down
      elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
          self.exit = True

      # Key Up
      elif e.type == pygame.KEYUP:
        if e.key == pygame.K_CTRL:
          reducer('SHOOT_FIREBALL')
        elif e.key == pygame.K_LEFT:
          reducer('BRAKE_LEFT')
        elif e.key == pygame.K_RIGHT:
          reducer('BRAKE_RIGHT')

      # Mouse Up
      elif e.type == pygame.MOUSEBUTTONUP:
        reducer('ADD_TUBE', {
          'x': pygame.mouse.get_pos_x(),
          'y': pygame.mouse.get_pos_y()
        })



# Goomba
class Goomba():
  def __init__(self, x, y):
    self.x = x
    self.y = y




# View
class View():
  def __init__(self, model):
    self.screen = pygame.display.set_mode((640, 480), 32)
    self.model = model

  def draw(self):    
    self.screen.fill([0, 0, 0])
    pygame.display.update()

view = View(model)
controller = Controller(model, view)

while not controller.exit:
  controller.animationFrame()
  view.draw()
