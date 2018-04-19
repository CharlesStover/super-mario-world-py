from mario import mario
from model import model
from sprite import Sprite

TUBE_WIDTH = 32.0
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

def TubeBottom(x, y):
  yCoord = WINDOW_HEIGHT - y - 16.0
  while yCoord > 0.0:
    model['objects'].append(
      Sprite('images/tube.gif', {
        'height': 16.0,
        'sprite': [ TUBE_WIDTH, 0 ],
        'type': 'tube',
        'x': mario.props['x'] + x - WINDOW_WIDTH / 2.0 - TUBE_WIDTH / 2.0,
        'y': yCoord - 16.0,
        'width': TUBE_WIDTH
      })
    )
    yCoord = yCoord - 16.0

def TubeTop(x, y):
  return Sprite('images/tube.gif', {
    'height': 16.0,
    'sprite': [ 0, 0 ],
    'type': 'tube',
    'x': mario.props['x'] + x - WINDOW_WIDTH / 2.0 - TUBE_WIDTH / 2.0,
    'y': WINDOW_HEIGHT - y - 16.0,
    'width': TUBE_WIDTH
  })