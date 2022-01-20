from operator import pos
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
    options = possibilities(board)

    car = random.choice(list(options.keys()))
    move = random.choice(options[car])

    board.move_car(car, move)

    return car, move


def random_traffic_control(board, sol_number, best_sol):
    """Creates a list of all the moves and returns the length of the solution"""
    move_path = []

    while not(board.game_won()):
        car, move = random_move(board)
        move_path.append({'car': car, 'move': move})
        # check if length exceeds best solution's length
        if int(len(move_path)) > int(best_sol):
            return 1000

    sol_length = board.after_win(move_path, sol_number)

    return sol_length

