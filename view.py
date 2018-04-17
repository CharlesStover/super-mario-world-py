import pygame
from datetime import datetime
from mario import mario
from model import model

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32)

class View():
  def __init__(self):
    pass

  def draw(self):
    screen.fill([0, 0, 0])
    model['lastRender'] = datetime.now()
    model['renders'] = (model['renders'] + 1) % 100
    for gameObject in model['objects']:

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
      screen.blit(gameObject.props['image'], coordinates, sprite)
    pygame.display.update()