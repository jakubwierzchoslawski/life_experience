import numpy as np

class Point:

    def __init__(self):
        self.pX, self.pY, self.pH = self.generate_random_point()


    def generate_random_point():
        x = np.random.randint(0, 99)
        y = np.random.randint(0, 99)
        h = np.random.randint(-3, 6)
        return x, y, h

    def genrate_point(self, px, py, ph):
        self.pX = px
        self.pY = py
        self.pH = ph

        return self.pX, self.pY, self.pH
