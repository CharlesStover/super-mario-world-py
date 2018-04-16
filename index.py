import pygame
from datetime import datetime
from mario import mario
from model import model
from random import randint, seed
from tube import TubeBottom, TubeTop
seed(datetime.now())

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



# View
class View():
  def __init__(self, model):
    self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32)
    self.model = model

  def draw(self):    
    self.screen.fill([0, 0, 0])
    for gameObject in self.model['objects']:
      coordinates = (WINDOW_WIDTH / 2 + gameObject.props['x'] - mario.props['x'], WINDOW_HEIGHT - gameObject.props['y'] - gameObject.props['height'])
      sprite = (gameObject.props['sprite'][0], gameObject.props['sprite'][1], gameObject.props['width'], gameObject.props['height'])
      self.screen.blit(gameObject.props['image'], coordinates, sprite)
    pygame.display.update()



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



view = View(model)
controller = Controller(model, view)

clock = pygame.time.Clock()
while not controller.exit:
  controller.animationFrame()
  view.draw()
  clock.tick(40)
