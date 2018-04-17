from datetime import datetime
from mario import mario
from model import model
from random import randint, seed
from tube import TubeBottom, TubeTop

seed(datetime.now())

def reducer(type, action = None):
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
    model['objects'].append(Sprite('images/galoomba.gif', {
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
      'x': mario.props['x'] + randint(-WINDOW_WIDTH, WINDOW_WIDTH),
      'y': WINDOW_HEIGHT
    }))
  elif type == 'ADD_TUBE':
    model['objects'].append(TubeTop(action['x'], action['y']))
    TubeBottom(action['x'], action['y'])
  elif type == 'BRAKE_LEFT':
    if mario.props['walking'] == -1:
      mario.props['horizontalAcceleration'] = 0
      mario.props['horizontalVelocity'] = 0
      mario.props['walking'] = 0
  elif type =='BRAKE_RIGHT':
    if mario.props['walking'] == 1:
      mario.props['horizontalAcceleration'] = 0
      mario.props['horizontalVelocity'] = 0
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
      mario.props['horizontalAcceleration'] = -1 * mario.props['walkAcceleration']
      mario.props['horizontalVelocity'] = -0.25 * mario.props['horizontalVelocity']
      mario.props['walking'] = -1
  elif type == 'WALK_RIGHT':
    if mario.props['walking'] != 1:
      mario.props['direction'] = True
      mario.props['horizontalAcceleration'] = mario.props['walkAcceleration']
      mario.props['horizontalVelocity'] = -0.25 * mario.props['horizontalVelocity']
      mario.props['walking'] = 1
