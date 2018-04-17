from sprite import Sprite

def collisionX(self, obj):
  if obj.props['type'] == 'galoomba':
    self.props['horizontalVelocity'] = 0

    # Collision while running right.
    if self.props['direction']:
      self.props['x'] = obj.props['x'] - self.props['width'] - 0.1

    # Collision while running left.
    else:
      self.props['x'] = obj.props['x'] + obj.props['width'] + 0.1

  elif obj.props['type'] == 'tube':
    self.props['horizontalVelocity'] = 0

    # Collision while running right.
    if self.props['direction']:
      self.props['x'] = obj.props['x'] - self.props['width'] - 0.1

    # Collision while running left.
    else:
      self.props['x'] = obj.props['x'] + obj.props['width'] + 0.1

def collisionY(self, obj):
  if obj.type == 'galoomba':
    self.props['verticalVelocity'] = -1 * self.props['verticalVelocity']

  elif obj.type == 'tube':
    self.props['falling'] = False
    self.props['verticalVelocity'] = 0
    self.props['y'] = obj.props['y'] + obj.props['height'] + 0.1

def controller(self):
  xPerFrame = 7
  if self.props['walking']:
    self.props['walkFrame'] = (self.props['walkFrame'] + 1) % (xPerFrame * 4)
  else:
    self.props['walkFrame'] = 0

  # Set sprite.
  if self.props['direction']:
    def adjustWidth(self, width):
      previousWidth = self.props['width']
      self.props['width'] = width
      self.props['x'] = self.props['x'] + previousWidth - width
    if self.props['walking']:
      if self.props['walkFrame'] < xPerFrame:
        if self.props['horizontalVelocity'] == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [95, 0]
          adjustWidth(self, 18)
        else:
          self.props['sprite'] = [0, 0]
          adjustWidth(self, 15)
      elif self.props['walkFrame'] < xPerFrame * 2:
        if self.props['horizontalVelocity'] == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [113, 0]
          adjustWidth(self, 18)
        else:
          self.props['sprite'] = [15, 0]
          adjustWidth(self, 15)
      elif self.props['walkFrame'] < xPerFrame * 3:
        if self.props['horizontalVelocity'] == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [95, 0]
          adjustWidth(self, 18)
        else:
          self.props['sprite'] = [0, 0]
          adjustWidth(self, 15)
      else:
        if self.props['horizontalVelocity'] == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [131, 0]
          adjustWidth(self, 18)
        else:
          self.props['sprite'] = [30, 0]
          adjustWidth(self, 16)
    else:
      self.props['sprite'] = [0, 0]
      adjustWidth(self, 15)
  else:
    if self.props['walking']:
      if self.props['walkFrame'] < xPerFrame:
        if abs(self.props['horizontalVelocity']) == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [95, 28]
          self.props['width'] = 18
        else:
          self.props['sprite'] = [80, 28]
          self.props['width'] = 15
      elif self.props['walkFrame'] < xPerFrame * 2:
        if abs(self.props['horizontalVelocity']) == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [131, 28]
          self.props['width'] = 18
        else:
          self.props['sprite'] = [65, 28]
          self.props['width'] = 15
      elif self.props['walkFrame'] < xPerFrame * 3:
        if abs(self.props['horizontalVelocity']) == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [95, 28]
          self.props['width'] = 18
        else:
          self.props['sprite'] = [80, 28]
          self.props['width'] = 15
      else:
        if abs(self.props['horizontalVelocity']) == self.props['maxHorizontalVelocity']:
          self.props['sprite'] = [113, 28]
          self.props['width'] = 18
        else:
          self.props['sprite'] = [49, 28]
          self.props['width'] = 16
    else:
      self.props['sprite'] = [80, 28]
      self.props['width'] = 15

  # Set background.
  # document.body.style.setProperty('background-position', (Math.round(window.model.renders / 10) % 4) * -512 + (-1 * self.x) / 2 + 'px center')
  # document.body.style.setProperty('margin-left', (-1 * self.x + document.body.clientWidth / 2) + 'px')

mario = Sprite('images/mario.gif', {
  'collisionX': collisionX,
  'collisionY': collisionY,
  'controller': controller,
  'direction': True,
  'falling': False,
  'jumpVelocity': 10,
  'type': 'mario',
  'maxHorizontalVelocity': 6,
  'maxVerticalVelocity': 10,
  'walkAcceleration': 0.1,
  'walkFrame': 0,
  'walking': 0,
  'height': 28,
  'width': 15
})
