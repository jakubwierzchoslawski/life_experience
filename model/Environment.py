import nsmath.nums as nums
from Actor import Actor
from Board import Board
import random

'''
Environment class is composed of 
 - board - 2D space represented by array called Grid
 - actors
 - rules - set of possible actions for actors. also contains invariants
'''
class Environment:

    # initialize environment with some pre-sets
    def __init__(self, X, Y, actors_per_cell, actors_nr):
        self.X = X
        self.Y = Y
        self.actors_per_cell = actors_per_cell

        # create board
        self.board = Board( self.X, self.Y)

        # add some actors to the environment
        self.__initialize_actors(actors_nr)



    def __initialize_actors(self, anr):
        for i in range(anr):
            self.add_actor_to_board(Actor())

    # EVENTS
    def add_actor_to_board(self, actor):
        # verify if there is a cell when new actor could born
        y, x = self.__random_free_cell_cords()

        if x == -1 and y == -1:
            self.board.replace_random_actor(self.board.find_random(), actor)
        else:
            self.board.add_actor(actor, y , x)

    # returns coordinates of free cell (less than 2 actors occupy cell)
    def __random_free_cell_cords(self):
        all_cell_cords = [(x, y) for x in range(self.X) for y in range(self.Y)]
        random.shuffle(all_cell_cords)

        for x, y in all_cell_cords:
            temp_cell = self.board.grid[y][x]
            if len(temp_cell.get_actors()) < self.actors_per_cell:
                return y, x

        print("WARNING! from Environment.__random_free_cell_cords ::: Grid msg: no free cell found!")
        return -1, -1

