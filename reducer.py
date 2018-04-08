from datetime import datetime
from random import randint, seed
seed(datetime.now())

WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

def galoombaCollisionX(self, obj):
  if obj.props['type'] == 'mario':
    if self.props['horizontalVelocity'] < 0:
      obj.set('x', self.props['x'] - obj.props['width'] - 0.01)
    else:
      obj.set('x', self.props['x'] + self.props['width'] + 0.01)
  elif obj.props['type'] == 'galoomba' or obj.props['type'] == 'tube':
    self.set('horizontalAcceleration', -1 * self.props['horizontalAcceleration']);
    if self.props['horizontalVelocity'] > 0:
      self.set('x', obj.props['x'] - self.props['width'] - 0.1)
    else:
      self.set('x', obj.props['x'] + obj.props['width'] + 0.1)
    self.set('horizontalVelocity', -1 * self.props['horizontalVelocity']);

def galoombaCollisionY(self, obj):
  if obj.props['type'] == 'tube':
    self.set('verticalVelocity', 0)
    self.set('y', obj.props['y'] + obj.props['height'] + 0.1)

def galoombaController(self):
    if self.props['x'] > mario.props['x'] + WINDOW_WIDTH or self.props['x'] < mario.props['x'] - WINDOW_WIDTH:
      reducer('DELETE', self)
    if self.dead:
      self.dead = self.dead + 1
      if self.dead > 8:
        reducer('DELETE', self)
    else:
      self.frame = self.frame + 1
      if self.props['horizontalVelocity'] > 0:
        if self.props['frame'] > 8:
          self.set('sprite', [64, 0])
        else:
          self.set('sprite', [48, 0])
      else:
        if self.props['frame'] > 8:
          self.set('sprite', [16, 0])
        else:
          self.set('sprite', [0, 0])
      if self.props['frame'] > 15:
        self.frame = 0

def reducer(model):
  def r(type, action):
    if type == 'ADD_GALOOMBA':
      speed = randint(-2, 2)
      if speed < 0:
        horizontalAcceleration = -0.1
      else:
        horizontalAcceleration = 0.1
      if speed > 0:
        sprite = [48, 0]
      else:
        sprite = [0, 0]
      model.objects.add(Sprite('images/galoomba.gif', {
        'collisionX': galoombaCollisionX,
        'collisionY': galoombaCollisionY,
        'controller': galoombaController,
        'dead': 0,
        'frame': 0,
        'height': 15,
        'horizontalAcceleration': horizontalAcceleration,
        'horizontalVelocity': speed,
        'maxHorizontalVelocity': 2,
        'maxVerticalVelocity': -5,
        'verticalAcceleration': -1,
        'sprite': sprite,
        'type': 'galoomba',
        'width': 16,
        'x': mario.x + randint(-WINDOW_WIDTH, WINDOW_WIDTH),
        'y': WINDOW_HEIGHT
      }))
    elif type == 'ADD_TUBE':
      TUBE_WIDTH = 32
      model.objects.add(Sprite(null, {
        'className': 'tube',
        'height': WINDOW_HEIGHT - action.y,
        'sheet': ['images/tube.gif', 'images/tube.gif'],
        'sprite': [[0, 0], [TUBE_WIDTH, 0]],
        'type': 'tube',
        'x': mario.x + action.x - WINDOW_WIDTH / 2 - TUBE_WIDTH / 2,
        'y': 0,
        'width': TUBE_WIDTH
      }))
    elif type == 'BRAKE_LEFT':
      if mario.props['walking'] == -1:
        mario.set('horizontalAcceleration', 0)
        mario.set('horizontalVelocity', 0)
        mario.set('walking', 0)
    elif type =='BRAKE_RIGHT':
      if mario.props['walking'] == 1:
        mario.set('horizontalAcceleration', 0)
        mario.set('horizontalVelocity', 0)
        mario.set('walking', 0)
    elif type == 'DELETE':
      model.objects.remove(action)
    elif type == 'JUMP':
      if not mario.props['falling']:
        mario.set('verticalVelocity', mario.jumpVelocity)
    elif type == 'SHOOT_FIREBALL':
      model.objects.add(Fireball())
    elif type == 'WALK_LEFT':
      if mario.props['walking'] !== -1:
        mario.set('direction', False)
        mario.set('horizontalAcceleration', -1 * mario.props['walkAcceleration'])
        mario.set('horizontalVelocity', -0.25 * mario.props['horizontalVelocity'])
        mario.set('walking', -1)
    elif type == 'WALK_RIGHT':
      if mario.props['walking'] !== 1:
        mario.set('direction', True)
        mario.set('horizontalAcceleration', mario.props['walkAcceleration'])
        mario.set('horizontalVelocity', -0.25 * mario.props['horizontalVelocity'])
        mario.set('walking', 1)
      }
  return r
