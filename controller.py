import pygame
from model import model
from reducer import reducer

class Controller():
  def __init__(self):
    self.exit = False

  def animationFrame(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.exit = True

      # Key Down
      elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
          self.exit = True
        elif e.key == pygame.K_LEFT:
          reducer('DECREASE_SCROLL_X')
          reducer('WALK_LEFT')
        elif e.key == pygame.K_RIGHT:
          reducer('INCREASE_SCROLL_X')
          reducer('WALK_RIGHT')
        elif e.key == pygame.K_SPACE:
          reducer('JUMP')

      # Key Up
      elif e.type == pygame.KEYUP:
        if e.key == pygame.K_LCTRL or e.key == pygame.K_RCTRL:
          reducer('SHOOT_FIREBALL')
        elif e.key == pygame.K_LEFT:
          reducer('BRAKE_LEFT')
        elif e.key == pygame.K_RIGHT:
          reducer('BRAKE_RIGHT')

      # Mouse Up
      elif e.type == pygame.MOUSEBUTTONUP:
        x, y = pygame.mouse.get_pos()
        reducer('ADD_TUBE', {
          'x': x,
          'y': y
        })
