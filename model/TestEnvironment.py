from Environment import Environment
from Actor import Actor

class TestModel:

    __Y_DIM = 3
    __X_DIM = 2
    actors_per_cell = 2
    actors_nr = 20


def test_environment(self, ):


    eenv = Environment(Environment.__Y_DIM, Environment.__X_DIM, Environment.actors_per_cell, Environment.actors_nr)
    eenv.board.print_board_info()

    eenv.add_actor_to_board(Actor())
    eenv.board.print_actors_info()

    eenv.board.draw_board_rich()

    eenv.board.executeStep()


if __name__ == "__main__":
    test = TestModel()

    test.test_environmen()
