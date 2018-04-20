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
    screen.fill([ 0, 0, 0 ])
    model['lastRender'] = datetime.now()
    model['renders'] = (model['renders'] + 1) % 100

    for gameObject in model['objects']:

      # Calculate speeds
      if gameObject.props['horizontalAcceleration'] != 0.0:
        gameObject.props['horizontalVelocity'] = min(
          max(
            gameObject.props['horizontalVelocity'] + gameObject.props['horizontalAcceleration'],
            -1.0 * gameObject.props['maxHorizontalVelocity']
          ),
          gameObject.props['maxHorizontalVelocity']
        )
      if gameObject.props['verticalAcceleration'] != 0.0:
        gameObject.props['verticalVelocity'] = min(
          max(
            gameObject.props['verticalVelocity'] + gameObject.props['verticalAcceleration'],
            -1.0 * gameObject.props['maxVerticalVelocity']
          ),
          gameObject.props['maxVerticalVelocity']
        )

      # Calculate Y coordinate.
      if gameObject.props['verticalVelocity']:
        newY = gameObject.props['y'] + gameObject.props['verticalVelocity']
        if newY <= 0.0:
          gameObject.props['falling'] = False
          gameObject.props['verticalVelocity'] = 0.0
          gameObject.props['y'] = 0.0
        else:
          gameObject.props['falling'] = True
          gameObject.props['y'] = newY

          # Collision detection: Y
          if gameObject.props['collisionY']:
            for gameObject2 in model['objects']:
              if gameObject == gameObject2 or gameObject2.props['static'] or not gameObject.isInside(gameObject2):
                continue
              gameObject.props['collisionY'](gameObject, gameObject2)

      # Calculate X coordinate.
      if gameObject.props['horizontalVelocity']:
        gameObject.props['x'] = gameObject.props['x'] + gameObject.props['horizontalVelocity']

        # Collision detection: X
        if gameObject.props['collisionX']:
          for gameObject2 in model['objects']:
            if gameObject == gameObject2 or gameObject2.props['static'] or not gameObject.isInside(gameObject2):
              continue
            gameObject.props['collisionX'](gameObject, gameObject2)

      if gameObject.props['controller']:
        gameObject.props['controller'](gameObject)
      gameObject.view()

      coordinates = (WINDOW_WIDTH / 2 + gameObject.props['x'] - mario.props['x'], WINDOW_HEIGHT - gameObject.props['y'] - gameObject.props['height'])
      sprite = (gameObject.props['sprite'][0], gameObject.props['sprite'][1], gameObject.props['width'], gameObject.props['height'])
      screen.blit(gameObject.props['image'], coordinates, sprite)
    pygame.display.update()
