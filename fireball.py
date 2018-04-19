from mario import mario
from sprite import Sprite

FIREBALL_WIDTH = 8.0
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

def fireballCollisionX(self, obj):
  if obj.props['type'] == 'galoomba':
    obj.props['dead'] = 1
    obj.props['horizontalAcceleration'] = 0.0
    obj.props['horizontalVelocity'] = 0.0
    obj.props['sprite'] = [ 32, 0 ]
  elif obj.props['type'] == 'tube':
    if self.props['horizontalVelocity'] > 0.0:
      n = -1 * self.props['width'] - 0.1
    else:
      n = obj.props['width'] + 0.1
    self.props['x'] = obj.props['x'] + n
    self.props['horizontalVelocity'] = -1.0 * self.props['horizontalVelocity']

def fireballCollisionY(self, obj):
  if obj.props['type'] == 'galoomba':
    obj.props['dead'] = 1
    obj.props['horizontalAcceleration'] = 0
    obj.props['horizontalVelocity'] = 0
    obj.props['sprite'] = [ 32, 0 ]
  elif obj.props['type'] != 'mario' and self.props['verticalVelocity'] <= 0:
    self.props['verticalVelocity'] = 7.5
    self.props['y'] = obj.props['y'] + obj.props['height'] + 0.1

def fireballController(self):
  if not self.props['falling']:
    self.props['falling'] = True
    self.props['verticalVelocity'] = 7.5
  if self.props['x'] < mario.props['x'] - WINDOW_WIDTH / 2 - FIREBALL_WIDTH / 2 or self.props['x'] > mario.props['x'] + WINDOW_WIDTH / 2 + FIREBALL_WIDTH / 2:
    reducer('DELETE', self)

def Fireball():
  if mario.props['direction']:
    horizontalVelocity = 7.5
  else:
    horizontalVelocity = -7.5
  return Sprite('images/fireball.gif', {
    'collisionX': fireballCollisionX,
    'collisionY': fireballCollisionY,
    'controller': fireballController,
    'height': FIREBALL_WIDTH,
    'horizontalVelocity': mario.props['horizontalVelocity'] + horizontalVelocity,
    'maxVerticalVelocity': 10,
    'type': 'fireball',
    'verticalAcceleration': -1,
    'x': mario.props['x'],
    'y': mario.props['y'] + mario.props['height'] * 0.5,
    'width': FIREBALL_WIDTH
  })
