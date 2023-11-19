import numpy as np
import nsmath.nums as nums

class Actor:

    # class variable
    colors = ['RED', 'GREEN']

    def __init__(self):
       # self.lifespan = nums.custom_probability_distribution(0, 130, .7, 60, 80)
        self.lifespan = nums.gausianlike_probability_distribution(0,130,70,50)
        self.name = "Name_" + str(np.random.random())
        self.color = np.random.choice(self.colors)
        self.position= None
      # if self.lifespan < 60 or self.lifespan>80:
        #print("Actor: {} lifespan is set to: {}".format(self.name, self.lifespan))

    def set_position(self, x, y):
        self.position = (x, y)

