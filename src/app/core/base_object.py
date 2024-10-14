
from abc import abstractmethod


class BaseObject():
	
	components = []

	def __init__(self, object_controller):
		object_controller.list.append(self)

	def add_component(self, component):
		self.components.append(component)

	def get_component(self, component):
		for c in self.components:
			if isinstance(c, component):
				return c
		return None

	@abstractmethod
	def start(self):
		for component in self.components:
			component.start()

	def update(self):
		for component in self.components:
			component.update()

	def end(self):
		for component in self.components:
			component.end()