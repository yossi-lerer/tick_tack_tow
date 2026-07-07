
from players import ask_player_name, show_turn_message
from board import create_board, print_board, place_symbol
from validatiionss import is_vaild_move
from win_checker import check_win 

def play_single_player_game():
    player_name = ask_player_name()
    symble = "X"
    c_boars = create_board()
    show_board = print_board(c_boars)
    round = 0
    while round < 9:
        turn_message = show_turn_message(player_name, symble)
        move = ask_move()
        move=ask_valid_move(c_boars,move[0],move[1])
        place = place_symbol(c_boars, move[0], move[1], symble)
        show_after_place = print_board(c_boars)
        if check_win:
            print("~~~Congratulations! ", player_name,"win!~~~")
        round += 1

def ask_move() -> tuple[int, int]:
    move = input("please enter two number for your next move first num for row and secend num for column. for exemple 1.2 ")
    move = move.split(".")
    move[0] = int(move[0])
    move[1] = int(move[1])
    return move[0]-1, move[1]-1

def ask_valid_move(bourd,row,col):
    while True:
        if is_vaild_move(bourd,row,col):
            return row,col
        
        else:
            print("!invalid index, try again!")
            row,col=ask_move()
        
    
            


    