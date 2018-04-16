from mario import mario
from model import model
from sprite import Sprite

TUBE_WIDTH = 32
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

def TubeBottom(x, y):
  yCoord = WINDOW_HEIGHT - y - 16
  while yCoord > 0:
    model['objects'].append(
      Sprite('images/tube.gif', {
        'height': 16,
        'sprite': [ TUBE_WIDTH, 0 ],
        'type': 'tube',
        'x': mario.props['x'] + x - WINDOW_WIDTH / 2 - TUBE_WIDTH / 2,
        'y': yCoord - 16,
        'width': TUBE_WIDTH
      })
    )
    yCoord = yCoord - 16

def TubeTop(x, y):
  return Sprite('images/tube.gif', {
    'height': 16,
    'sprite': [ 0, 0 ],
    'type': 'tube',
    'x': mario.props['x'] + x - WINDOW_WIDTH / 2 - TUBE_WIDTH / 2,
    'y': WINDOW_HEIGHT - y - 16,
    'width': TUBE_WIDTH
  })