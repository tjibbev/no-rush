import random


def possibilities(board):
    """Creates & returns dict containing all possible car movements"""
    possibles = {}
    for car in board._cars.keys():
        length = board._cars[car]._length
        car_possibilities = []
        for move in range(- board._size + length, board._size - length + 1):
            if board.is_valid_move(car, move):
                car_possibilities.append(move)

        # Add car only if moveable
        if car_possibilities != []:
            possibles[car] = car_possibilities

    return possibles


def random_move(board):
    """ Moves a random car by a random amount of steps """
    options = possibilities(board)

    car = random.choice(list(options.keys()))
    move = random.choice(options[car])

    board.move_car(car, move)

    return car, move


def random_traffic_control(board, sol_number, best_sol):
    """
    Randomly moves cars till the puzzle is solved
    Stops solving when more moves are done than in best_sol
    Return solved board and the board path
    """
    move_path = []

    while not(board.game_won()):
        car, move = random_move(board)
        move_path.append({'car': car, 'move': move})
        # check if length exceeds best solution's length
        if len(move_path) > len(best_sol[1]):
            return best_sol

    solution = board.after_win(move_path, sol_number)

    return solution
