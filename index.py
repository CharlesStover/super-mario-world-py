from pygame import display, event, init, key, mouse, MOUSEBUTTONUP
from pygame.locals import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT
from time import sleep

init()

# Controller
class Controller():
	def __init__(self, model, view):
		self.exit = False
		self.model = model
		self.view = view

	def animationFrame(self):
		for e in event.get():
			if e.type == QUIT:
				self.exit = True
			elif e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					self.exit = True
			# elif e.type == MOUSEBUTTONUP:
				# self.model.set_dest(mouse.get_pos())
		keys = key.get_pressed()
		if keys[K_LEFT]:
			self.model.dest_x -= 1
		if keys[K_RIGHT]:
			self.model.dest_x += 1
		if keys[K_UP]:
			self.model.dest_y -= 1
		if keys[K_DOWN]:
			self.model.dest_y += 1



# Goomba
class Goomba():
	def __init__(self, x, y):
		self.x = x
		self.y = y



# Mario
class Mario():
	staticHeight = 95
	staticWidth = 60

	def __init__(self, x, y):
		self.jumpVelocity = 10
		self.x = x
		self.y = y

	def getJumpVelocity(self):
		return self.jumpVelocity



# Model
class Model():

	def __init__(self):
		self.windowHeight = 480
		self.gameObjects = [
			Mario(0, (self.windowHeight - Mario.staticHeight) / 2),
			Goomba(255, 255)
		]
		self.setScrollX(0)
		self.windowWidth = 640

	def addGameObject(self, gameObject):
		self.gameObjects.append(gameObject)

	def getGameObject(self, i):
		return self.gameObjects[i]

	def getGameObjects(self):
		return self.gameObjects

	def setScrollX(self, scrollX):
		self.scrollX = scrollX


# View
class View():
	def __init__(self, model):
		self.screen = display.set_mode((640, 480), 32)
		# self.turtle_image = pygame.image.load("turtle.png")
		self.model = model
		# self.model.rect = self.turtle_image.get_rect()

	def draw(self):    
		self.screen.fill([0, 0, 0])
		# self.screen.blit(self.turtle_image, self.model.rect)
		display.flip()

model = Model()
view = View(model)
controller = Controller(model, view)

while not controller.exit:
	controller.animationFrame()
	view.draw()
