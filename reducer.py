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

def reducer(type, action):
  if type == 'ADD_GALOOMBA':
    var speed = Math.random() * 4 - 2;
    self.objects.push(new Sprite('images/galoomba.gif', {
      collisionX: galoombaCollisionX,
      collisionY: galoombaCollisionY,
      controller: galoombaController,
      dead: 0,
      frame: 0,
      height: 15,
      horizontalAcceleration: speed < 0 ? -0.1 : 0.1,
      horizontalVelocity: speed,
      maxHorizontalVelocity: 2,
      maxVerticalVelocity: -5,
      verticalAcceleration: -1,
      sprite:
        speed > 0
        ? [48, 0]
        : [0, 0],
      type: 'galoomba',
      width: 16,
      x: mario.x + Math.random() * document.body.clientWidth - document.body.clientWidth / 2,
      y: document.body.clientHeight
    }))
  elif type == 'ADD_TUBE':
    var TUBE_WIDTH = 32;
    self.objects.push(new Sprite(null, {
      className: 'tube',
      height: document.body.clientHeight - action.y,
      sheet: ['images/tube.gif', 'images/tube.gif'],
      sprite: [[0, 0], [TUBE_WIDTH, 0]],
      type: 'tube',
      x: mario.x + action.x - document.body.clientWidth / 2 - TUBE_WIDTH / 2,
      y: 0,
      width: TUBE_WIDTH
    }))
  elif type == 'BRAKE_LEFT':
    if (mario.walking == -1) {
      mario.set('horizontalAcceleration', 0);
      mario.set('horizontalVelocity', 0);
      mario.set('walking', 0);
    }
  elif type =='BRAKE_RIGHT':
    if (mario.walking == 1) {
      mario.set('horizontalAcceleration', 0);
      mario.set('horizontalVelocity', 0);
      mario.set('walking', 0);
    }
  elif type == 'DELETE':
    for (var x of Object.keys(self.objects)) {
      if (self.objects[x] == action) {
        document.body.removeChild(self.objects[x].element);
        delete self.objects[x];
        break;
      }
    }
  elif type == 'JUMP':
    if (!mario.falling) {
      mario.set('verticalVelocity', mario.jumpVelocity);
    }
  elif type == 'RESIZE_WINDOW':
    // document.body.style.setProperty('padding-left', Math.round(document.body.clientWidth / 2) + 'px');
    document.body.style.setProperty('padding-top', document.body.clientHeight + 'px');
  elif type == 'SHOOT_FIREBALL':
    self.objects.push(Fireball());
  elif type == 'WALK_LEFT':
    if (mario.walking !== -1) {
      mario.set('direction', false);
      mario.set('horizontalAcceleration', -1 * mario.walkAcceleration);
      mario.set('horizontalVelocity', -0.25 * mario.horizontalVelocity);
      mario.set('walking', -1);
    }
  elif type == 'WALK_RIGHT':
    if (mario.walking !== 1) {
      mario.set('direction', true);
      mario.set('horizontalAcceleration', mario.walkAcceleration);
      mario.set('horizontalVelocity', -0.25 * mario.horizontalVelocity);
      mario.set('walking', 1);
    }
