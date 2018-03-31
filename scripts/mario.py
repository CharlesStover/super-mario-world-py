from sprite import Sprite

def collisionX(self, obj):
  if obj.type == 'galoomba':
    self.set('horizontalVelocity', 0)

    # Collision while running right.
    if self.direction:
      self.set('x', obj.x - self.width - 0.1)

    # Collision while running left.
    else:
      self.set('x', obj.x + obj.width + 0.1)

  elif obj.type == 'tube':
    self.set('horizontalVelocity', 0)

    # Collision while running right.
    if self.direction:
      self.set('x', obj.x - self.width - 0.1)

    # Collision while running left.
    else:
      self.set('x', obj.x + obj.width + 0.1)

def collisionY(self, obj):
  if obj.type == 'galoomba':
    self.set('verticalVelocity', -1 * self.verticalVelocity)

  elif obj.type == 'tube':
    self.set('falling', False)
    self.set('verticalVelocity', 0)
    self.set('y', obj.y + obj.height + 0.1)

def controller(self):
  xPerFrame = 7
  if self.walking:
    self.walkFrame = (self.walkFrame + 1) % (xPerFrame * 4)
  else:
    self.walkFrame = 0

  # Set sprite.
  if self.direction:
    def adjustWidth(self, width):
      previousWidth = self.width
      self.set('width', width)
      self.set('x', self.x + previousWidth - width)
    if self.walking:
      if self.walkFrame < xPerFrame:
        if self.horizontalVelocity == self.maxHorizontalVelocity:
          self.set('sprite', [95, 0])
          adjustWidth(self, 18)
        else:
          self.set('sprite', [0, 0])
          adjustWidth(self, 15)
      elif self.walkFrame < xPerFrame * 2:
        if self.horizontalVelocity == self.maxHorizontalVelocity:
          self.set('sprite', [113, 0])
          adjustWidth(self, 18)
        else:
          self.set('sprite', [15, 0])
          adjustWidth(self, 15)
      elif self.walkFrame < xPerFrame * 3:
        if self.horizontalVelocity == self.maxHorizontalVelocity:
          self.set('sprite', [95, 0])
          adjustWidth(self, 18)
        else:
          self.set('sprite', [0, 0])
          adjustWidth(self, 15)
      else:
        if self.horizontalVelocity == self.maxHorizontalVelocity:
          self.set('sprite', [131, 0])
          adjustWidth(self, 18)
        else:
          self.set('sprite', [30, 0])
          adjustWidth(self, 16)
    else:
      self.set('sprite', [0, 0])
      adjustWidth(self, 15)
  else:
    if self.walking:
      if self.walkFrame < xPerFrame:
        if Math.abs(self.horizontalVelocity) == self.maxHorizontalVelocity:
          self.set('sprite', [95, 28])
          self.set('width', 18)
        else:
          self.set('sprite', [80, 28])
          self.set('width', 15)
      elif self.walkFrame < xPerFrame * 2:
        if Math.abs(self.horizontalVelocity) == self.maxHorizontalVelocity:
          self.set('sprite', [131, 28])
          self.set('width', 18)
        else:
          self.set('sprite', [65, 28])
          self.set('width', 15)
      elif self.walkFrame < xPerFrame * 3:
        if Math.abs(self.horizontalVelocity) == self.maxHorizontalVelocity:
          self.set('sprite', [95, 28])
          self.set('width', 18)
        else:
          self.set('sprite', [80, 28])
          self.set('width', 15)
      else:
        if Math.abs(self.horizontalVelocity) == self.maxHorizontalVelocity:
          self.set('sprite', [113, 28])
          self.set('width', 18)
        else:
          self.set('sprite', [49, 28])
          self.set('width', 16)
    else:
      self.set('sprite', [80, 28])
      self.set('width', 15)

  # Set background.
  document.body.style.setProperty('background-position', (Math.round(window.model.renders / 10) % 4) * -512 + (-1 * self.x) / 2 + 'px center')
  document.body.style.setProperty('margin-left', (-1 * self.x + document.body.clientWidth / 2) + 'px')

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
