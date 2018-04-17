from mario import mario
from reducer import reducer

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