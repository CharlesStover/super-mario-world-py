from datetime import datetime
from mario import mario
from model import model
from random import randint, seed
from sprite import Sprite
from tube import TubeBottom, TubeTop

seed(datetime.now())

FIREBALL_WIDTH = 8.0
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

def fireballCollisionX(self, obj):
  if obj.props['type'] == 'galoomba':
    obj.props['dead'] = 1.0
    obj.props['horizontalAcceleration'] = 0.0
    obj.props['horizontalVelocity'] = 0.0
    obj.props['sprite'] = [ 32, 0 ]
  elif obj.props['type'] == 'tube':
    if self.props['horizontalVelocity'] > 0.0:
      n = -1.0 * self.props['width'] - 0.1
    else:
      n = obj.props['width'] + 0.1
    self.props['x'] = obj.props['x'] + n
    self.props['horizontalVelocity'] = -1.0 * self.props['horizontalVelocity']

def fireballCollisionY(self, obj):
  if obj.props['type'] == 'galoomba':
    obj.props['dead'] = 1
    obj.props['horizontalAcceleration'] = 0.0
    obj.props['horizontalVelocity'] = 0.0
    obj.props['sprite'] = [ 32, 0 ]
  elif obj.props['type'] != 'mario' and self.props['verticalVelocity'] <= 0.0:
    self.props['verticalVelocity'] = 7.5
    self.props['y'] = obj.props['y'] + obj.props['height'] + 0.1

def fireballController(self):
  if not self.props['falling']:
    self.props['falling'] = True
    self.props['verticalVelocity'] = 7.5
  if self.props['x'] < mario.props['x'] - WINDOW_WIDTH / 2 - FIREBALL_WIDTH / 2 or self.props['x'] > mario.props['x'] + WINDOW_WIDTH / 2 + FIREBALL_WIDTH / 2:
    reducer('DELETE', self)

def galoombaCollisionX(self, obj):
  if obj.props['type'] == 'mario':
    if self.props['horizontalVelocity'] < 0.0:
      obj.props['x'] = self.props['x'] - obj.props['width'] - 0.01
    else:
      obj.props['x'] = self.props['x'] + self.props['width'] + 0.01
  elif obj.props['type'] == 'galoomba' or obj.props['type'] == 'tube':
    self.props['horizontalAcceleration'] = -1.0 * self.props['horizontalAcceleration']
    if self.props['horizontalVelocity'] > 0.0:
      self.props['x'] = obj.props['x'] - self.props['width'] - 0.1
    else:
      self.props['x'] = obj.props['x'] + obj.props['width'] + 0.1
    self.props['horizontalVelocity'] = -1.0 * self.props['horizontalVelocity']

def galoombaCollisionY(self, obj):
  if obj.props['type'] == 'tube':
    self.props['verticalVelocity'] = 0.0
    self.props['y'] = obj.props['y'] + obj.props['height'] + 0.1

def galoombaController(self):
  if self.props['x'] > mario.props['x'] + WINDOW_WIDTH or self.props['x'] < mario.props['x'] - WINDOW_WIDTH:
    reducer('DELETE', self)
  if self.props['dead']:
    self.props['dead'] = self.props['dead'] + 1
    if self.props['dead'] > 8:
      reducer('DELETE', self)
  else:
    self.props['frame'] = self.props['frame'] + 1
    if self.props['horizontalVelocity'] > 0.0:
      if self.props['frame'] > 8:
        self.props['sprite'] = [ 64, 0 ]
      else:
        self.props['sprite'] = [ 48, 0 ]
    else:
      if self.props['frame'] > 8:
        self.props['sprite'] = [ 16, 0 ]
      else:
        self.props['sprite'] = [ 0, 0 ]
    if self.props['frame'] > 15:
      self.props['frame'] = 0

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
    'maxVerticalVelocity': 10.0,
    'type': 'fireball',
    'verticalAcceleration': -1.0,
    'x': mario.props['x'],
    'y': mario.props['y'] + mario.props['height'] * 0.5,
    'width': FIREBALL_WIDTH
  })

def reducer(type, action = None):
  if type == 'ADD_GALOOMBA':
    speed = randint(-2, 2)
    if speed < 0:
      horizontalAcceleration = -0.1
    else:
      horizontalAcceleration = 0.1
    if speed > 0.0:
      sprite = [ 48, 0 ]
    else:
      sprite = [ 0, 0 ]
    model['objects'].append(Sprite('images/galoomba.gif', {
      'collisionX': galoombaCollisionX,
      'collisionY': galoombaCollisionY,
      'controller': galoombaController,
      'dead': 0,
      'frame': 0,
      'height': 15.0,
      'horizontalAcceleration': horizontalAcceleration,
      'horizontalVelocity': speed,
      'maxHorizontalVelocity': 2.0,
      'maxVerticalVelocity': -5.0,
      'verticalAcceleration': -1.0,
      'sprite': sprite,
      'type': 'galoomba',
      'width': 16.0,
      'x': mario.props['x'] + randint(-WINDOW_WIDTH, WINDOW_WIDTH),
      'y': WINDOW_HEIGHT
    }))

  elif type == 'ADD_TUBE':
    model['objects'].append(TubeTop(action['x'], action['y']))
    TubeBottom(action['x'], action['y'])

  elif type == 'BRAKE_LEFT':
    if mario.props['walking'] == -1:
      mario.props['horizontalAcceleration'] = 0.0
      mario.props['horizontalVelocity'] = 0.0
      mario.props['walking'] = 0

  elif type =='BRAKE_RIGHT':
    if mario.props['walking'] == 1:
      mario.props['horizontalAcceleration'] = 0.0
      mario.props['horizontalVelocity'] = 0.0
      mario.props['walking'] = 0

  elif type == 'DELETE':
    model['objects'].remove(action)

  elif type == 'JUMP':
    if not mario.props['falling']:
      mario.props['verticalVelocity'] = mario.props['jumpVelocity']

  elif type == 'SHOOT_FIREBALL':
    model['objects'].append(Fireball())

  elif type == 'WALK_LEFT':
    if mario.props['walking'] != -1:
      mario.props['direction'] = False
      mario.props['horizontalAcceleration'] = -1.0 * mario.props['walkAcceleration']
      mario.props['horizontalVelocity'] = -0.25 * mario.props['horizontalVelocity']
      mario.props['walking'] = -1

  elif type == 'WALK_RIGHT':
    if mario.props['walking'] != 1:
      mario.props['direction'] = True
      mario.props['horizontalAcceleration'] = mario.props['walkAcceleration']
      mario.props['horizontalVelocity'] = -0.25 * mario.props['horizontalVelocity']
      mario.props['walking'] = 1
