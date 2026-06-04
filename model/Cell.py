class Cell:
    # Actor objects only
    # collection of actors "standing" on a current cell

    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.actors = []

    def assign_actor(self, actor):
        self.actors.append(actor)

    def get_actors(self):
        return self.actors

    def get_coordinates(self):
        return self.Y, self.X
