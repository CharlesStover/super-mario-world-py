from pygame import image

class Sprite:
  def __init__(self, sheet, attr):
    self.changes = []
    self.props = {
      'className': None,
      'collisionX': None,
      'collisionY': None,
      'controller': None,
      'height': 0,
      'horizontalAcceleration': 0,
      'horizontalVelocity': 0,
      'image': None,
      'maxHorizontalVelocity': 0,
      'maxVerticalVelocity': 0,
      'sheet': None,
      'sprite': [0, 0],
      'static': False,
      'type': None,
      'verticalAcceleration': -0.5,
      'verticalVelocity': 0,
      'width': 0,
      'x': 0,
      'y': 0
    }
    if sheet:
      self.set('sheet', sheet)

  def isInside(self, that):
    return (
      self.props['x'] + self.props['width'] >= that.props['x'] and
      self.props['x'] <= that.props['x'] + that.props['width'] and
      self.props['y'] <= that.props['y'] + that.props['height'] and
      self.props['y'] + self.props['height'] >= that.props['y']
    )

  def set(self, key, value):
    self.props[key] = value
    self.changes.append(key)

  def view(self):

    # Changes that require view.
    while len(self.changes) > 0:
      change = self.changes.pop()
      if change == 'sheet':
        if self.props['sheet'] is list:
          self.props['image'] = image.load(self.props['sheet'])
        else:
          self.props['image'] = image.load(self.props['sheet'])
