import pygame
from controller import Controller
from view import View

pygame.init()

view = View()
controller = Controller()

clock = pygame.time.Clock()
while not controller.exit:
  controller.animationFrame()
  view.draw()
  clock.tick(40)
