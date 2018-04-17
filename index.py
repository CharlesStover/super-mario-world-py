import pygame
from datetime import datetime
from mario import mario
from model import model
from reducer import reducer

pygame.init()
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

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

    for gameObject in self.model['objects']:
      if gameObject.props['controller']:
        gameObject.props['controller'](gameObject)



# View
class View():
  def __init__(self, model):
    self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32)
    self.model = model

  def draw(self):    
    self.screen.fill([0, 0, 0])
    model['lastRender'] = datetime.now()
    model['renders'] = (model['renders'] + 1) % 100
    for gameObject in self.model['objects']:

      # Calculate speeds
      if gameObject.props['horizontalAcceleration'] != 0:
        gameObject.props['horizontalVelocity'] = min(
          max(
            gameObject.props['horizontalVelocity'] + gameObject.props['horizontalAcceleration'],
            -1 * gameObject.props['maxHorizontalVelocity']
          ),
          gameObject.props['maxHorizontalVelocity']
        )
      if gameObject.props['verticalAcceleration'] != 0:
        gameObject.props['verticalVelocity'] = min(
          max(
            gameObject.props['verticalVelocity'] + gameObject.props['verticalAcceleration'],
            -1 * gameObject.props['maxVerticalVelocity']
          ),
          gameObject.props['maxVerticalVelocity']
        )
      coordinates = (WINDOW_WIDTH / 2 + gameObject.props['x'] - mario.props['x'], WINDOW_HEIGHT - gameObject.props['y'] - gameObject.props['height'])
      sprite = (gameObject.props['sprite'][0], gameObject.props['sprite'][1], gameObject.props['width'], gameObject.props['height'])
      self.screen.blit(gameObject.props['image'], coordinates, sprite)
    pygame.display.update()



view = View(model)
controller = Controller(model, view)

clock = pygame.time.Clock()
while not controller.exit:
  controller.animationFrame()
  view.draw()
  clock.tick(40)
