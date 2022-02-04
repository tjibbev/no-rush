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


def random_traffic_control_long(board, sol_number):
    """
    Randomly moves cars till the puzzle is solved

    Return solved board and the board path
    """
    move_path = []

    while not(board.game_won()):
        car, move = random_move(board)
        move_path.append({'car': car, 'move': move})

    solution = board.after_win(move_path, sol_number)

    return solution
