from pygame import image

class Sprite:
  def __init__(self, sheet, attr):
    self.changes = []
    self.props = {
      'className': None,
      'collisionX': None,
      'collisionY': None,
      'controller': None,
      'height': 0.0,
      'horizontalAcceleration': 0.0,
      'horizontalVelocity': 0.0,
      'image': None,
      'maxHorizontalVelocity': 0.0,
      'maxVerticalVelocity': 0.0,
      'sprite': [ 0, 0 ],
      'static': False,
      'type': None,
      'verticalAcceleration': -0.5,
      'verticalVelocity': 0.0,
      'width': 0.0,
      'x': 0.0,
      'y': 0.0
    }
    for key in attr.keys():
      self.props[key] = attr[key]
    self.setImage(sheet)

  def isInside(self, that):
    return (
      self.props['x'] + self.props['width'] >= that.props['x'] and
      self.props['x'] <= that.props['x'] + that.props['width'] and
      self.props['y'] <= that.props['y'] + that.props['height'] and
      self.props['y'] + self.props['height'] >= that.props['y']
    )

  def setImage(self, sheet):
    self.props['image'] = image.load(sheet)

  def view(self):
    pass
