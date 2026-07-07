from players import ask_player_name, show_turn_message
from board import create_board, print_board, place_symbol

def play_single_player_game():
    player_name = ask_player_name()
    symble = "X"
    create_statrt_board = create_board()
    show_board = print_board(create_statrt_board)
    round = 0
    while round < 9:
        turn_message = show_turn_message(player_name, symble)
        move = ask_move()
        place = place_symbol(create_statrt_board, move[0], move[1], symble)
        show_after_place = print_board(create_statrt_board)
        round += 1

def ask_move() -> tuple[int, int]:
    move = input("please enter two number for your next move first num for row and secend num for column. Mandatory separation of numbers with a dot. for exemple 1.2 ")
    move = move.split(".")
    move[0] = int(move[0])
    move[1] = int(move[1])
    return move[0]-1, move[1]-1
