from Cell import Cell
import random
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches

'''
Grid object represents the game board. it's a 2d array.
Each array element represents GridCell which has their coordinates
and actors assigned
'''
class Board:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        grid_list = [[Cell(x, y) for x in range(self.X)] for y in range(self.Y)]
        self.grid = np.array(grid_list)

    # add incoming actor to cell
    # board is stupic, does not know about actors per cell limitation
    # you have to make sure invariant is fulfilled on environment level
    def add_actor(self, actor, Y, X):
        if ((X is None or X > self.X) or (Y is None or Y > self.Y)):
            return -1

        cell = self.grid[Y,X]
        cell.assign_actor(actor)

    def replace_random_actor(self, cell, actor):
        index_to_replace = random.randint(0, len(cell.get_actors()) - 1)
        # sprint("actor {} replaced by {}".format(cell.actors[index_to_replace].name, actor.name))
        cell.actors[index_to_replace] = actor


    # READ MODEL
    def get_grid(self):
        return self.grid


    def print_board_info(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                # Number of actors in the cell
                num_actors = len(cell.get_actors())
                # Print cell info with actor count
                print(f"Cell({y},{x})[{num_actors}]", end="\t")
            print()  # New line after each row
        print()  # Extra newline for better readability


    def print_actors_info(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                actor_info = ", ".join([f"{actor.name}({actor.color})" for actor in cell.get_actors()])
                cell_info = f"Cell({y},{x}): [{actor_info}]"
                print(cell_info.ljust(30), end=" ")
            print()  # New line after each row
        print()  # Extra newline for better readability

    def draw_board_rich(self):
        fig, ax = plt.subplots()

        # Set the dimensions of the plot
        ax.set_xlim(0, self.X)
        ax.set_ylim(0, self.Y)
        ax.set_aspect('equal', adjustable='box')

        cell_padding = 0.1  # Padding inside each cell
        text_vertical_padding = 0.2  # Vertical padding for text

        # Draw the grid cells and annotate actor information
        for y in range(self.Y):
            for x in range(self.X):
                cell = self.grid[y, x]

                # Draw cell with padding
                rect = patches.Rectangle(
                    (x + cell_padding / 2, self.Y - y - 1 + cell_padding / 2),
                    1 - cell_padding, 1 - cell_padding,
                    linewidth=1, edgecolor='black', facecolor='none')
                ax.add_patch(rect)

                # Display each actor's info inside the cell
                actors = cell.get_actors()
                num_actors = len(actors)
                for i, actor in enumerate(actors):
                    # Get the last 4 characters of the actor's name
                    actor_info = actor.name[-4:]
                    # Calculate the position to distribute the text vertically in the cell
                    text_y = (self.Y - y - 1 + 0.5 +
                              (0.5 - text_vertical_padding) * (i - num_actors / 2))
                    ax.text(
                        x + 0.5, text_y,
                        actor_info, ha='center', va='center',
                        color=actor.color.lower(), fontsize=8)

        # Show the plot
        plt.gca().invert_yaxis()  # Invert y-axis to match the row-column format
        plt.show()

    def find_random(self):
        x_random = random.randint(0, self.X - 1)
        y_random = random.randint(0, self.Y - 1)

        return self.grid[y_random, x_random]


'''
if __name__ == "__main__":
    grid = Grid(10, 10, 2)

    grid.print_grid()
'''
