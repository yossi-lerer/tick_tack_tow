
from players import ask_player_name, show_turn_message
from board import create_board, print_board, place_symbol
from validatiionss import is_vaild_move, vaild_move_input
from win_checker import check_win 

def play_single_player_game():
    player_name = ask_player_name()
    symble = "X"
    create_new_board = create_board()
    show_board = print_board(create_new_board)
    round = 0
    while round < 9:
        turn_message = show_turn_message(player_name, symble)
        move = ask_move()
        move=ask_valid_move(create_new_board,move[0],move[1])
        place = place_symbol(create_new_board, move[0], move[1], symble)
        show_after_place = print_board(create_new_board)
        winner=check_win(create_new_board,symble)
        if winner:
            print("~~Congratulations~~ ", player_name,"win!")
            exit()
        round += 1


def ask_move() -> tuple[int, int]:
    move = input("please enter two number for your next move first num for row and secend num for column. Insert a . (point) between the numbers. for exemple 1.2 ")
    move = move.split(".")
    while True:
        vaild = vaild_move_input(move)
        if vaild == True:
            break
        else:
            move = input("please enter two number for your next move first num for row and secend num for column. Insert a . (point) between the numbers. for exemple 1.2 ")
            move = move.split(".")
    move[0] = int(move[0])
    move[1] = int(move[1])
    return move[0]-1, move[1]-1

def ask_valid_move(bourd,row,col):
    while True:
        if is_vaild_move(bourd,row,col):
            return row,col
        
        else:
            row,col=ask_move()
        
    
            


    