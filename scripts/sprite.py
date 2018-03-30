class Sprite:
  def __init__(self, sheet, attr):
    self.changes = []
    self.set('element', document.createElement('div'))
    if sheet:
      self.set('sheet', sheet)
    self.className = None
    self.collisionX = None
    self.collisionY = None
    self.controller = None
    self.horizontalAcceleration = 0
    self.horizontalVelocity = 0
    self.maxHorizontalVelocity = 0
    self.maxVerticalVelocity = 0
    self.sprite = [0, 0]
    self.static = false
    self.type = None
    self.verticalAcceleration = -0.5
    self.verticalVelocity = 0
    attributes = {
      height: 0,
      width: 0,
      x: 0,
      y: 0,
      **attr
    }
    for key, value in attributes:
      self.set(key, value)

  def isInside(self, that):
    return (
      self.x + self.width >= that.x and
      self.x <= that.x + that.width and
      self.y <= that.y + that.height and
      self.y + self.height >= that.y
    )

  def set(self, key, value):
    self[key] = value
    self.changes.append(key)

  def view():

    # Changes that require view.
    while len(self.changes) > 0:
      change = self.changes.pop()
      if change == 'className':
        self.element.className = self.className;
      elif change == 'element':
        document.body.appendChild(self.element);
      elif change == 'height':
        self.element.style.setProperty('height', self.height + 'px');
        self.element.style.setProperty('margin-top', (-1 * self.height) + 'px');
      elif change == 'sheet':
        self.element.style.setProperty(
          'background-image',
          (
            Array.isArray(self.sheet)
            ? self.sheet
            : [self.sheet]
          )
          .map(function(sheet) {
            return 'url("' + sheet + '")';
          })
          .join(', ')
        )
      elif change == 'sprite':
        self.element.style.setProperty(
          'background-position',
          (
            Array.isArray(self.sprite[0])
            ? self.sprite
            : [ self.sprite ]
          )
          .map(function(sprite) {
            return (-1 * sprite[0]) + 'px ' + (-1 * sprite[1]) + 'px';
          })
          .join(', ')
        )
      elif change == 'x':
        self.element.style.setProperty('left', self.x + 'px');
      elif change == 'y':
        self.element.style.setProperty('top', (-1 * self.y) + 'px');
      elif change == 'width':
        # self.element.style.setProperty('margin-left', (-1 * self.width / 2) + 'px')
        self.element.style.setProperty('width', self.width + 'px')
