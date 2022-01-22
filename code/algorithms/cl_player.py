from code.classes.board import Board

def test_game(board):
    """Simple test game that moves cars on input"""

    # Creat list for the movement path
    move_path = []

    while not(board.game_won()):
        # Prompt for car input
        command = input("> ").upper()

        # Allows player to exit the game loop
        if command == "QUIT":
            break

        try:
            carname = command.split()[0]
            move = int(command.split()[1])

            if not(board.move_car(carname, move)):
                print("move not possible")
            else:
                print()
                for row in board.visualize():
                    print(row)
                print()
                move_path.append({'car': carname, 'move': move})
        except IndexError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")
        except ValueError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")

    board.after_win(move_path, "cl")