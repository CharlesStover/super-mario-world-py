from mario import mario
from reducer import reducer

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
