

class ObjectController():
	screen = None
	list = []

	def start(self):
		for obj in self.list:
			obj.start()

	def update(self):
		for obj in self.list:
			obj.draw(self.screen)
			obj.update()
	
	def end(self):
		for obj in self.list:
			obj.end()