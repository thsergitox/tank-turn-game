class ObjectController:
    def __init__(self):
        self.screen = None
        self.list = []

    def start(self):
        for obj in self.list:
            obj.start()

    def update(self):
        for obj in self.list:
            obj.update()

    def draw(self):
        for obj in self.list:
            obj.draw(self.screen)

    def end(self):
        for obj in self.list:
            obj.end()
        self.list.clear()  # Clear the list after ending all objects

    def add_object(self, obj):
        self.list.append(obj)

    def remove_object(self, obj):
        if obj in self.list:
            self.list.remove(obj)
