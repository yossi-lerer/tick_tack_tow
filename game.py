
from players import ask_player_name, show_turn_message
from board import create_board, print_board, place_symbol
from validatiionss import is_vaild_move, vaild_move_input
from win_checker import check_win 
from config import settings_game

def play_single_player_game():
    player_name1 = settings_game["name player 1"]
    player_name2 = settings_game["name player 2"]

    symbleplayer1 = settings_game["symbol player 1"]
    symbleplayer2 = settings_game["symbol player 2"]

    create_new_board = create_board()
    show_board = print_board(create_new_board)
    round = 0
    whos_turn=True
    while round < 9:
        if whos_turn:
            turn_message = show_turn_message(player_name1, symbleplayer1)
        if whos_turn==False:
            turn_message = show_turn_message(player_name2, symbleplayer2)
        move = ask_move()
        move=ask_valid_move(create_new_board,move[0],move[1])
        if whos_turn:
            place = place_symbol(create_new_board, move[0], move[1], symbleplayer1)
        if whos_turn==False:
            place = place_symbol(create_new_board, move[0], move[1], symbleplayer2)
        show_after_place = print_board(create_new_board)
        if whos_turn:
            winner=check_win(create_new_board,symbleplayer1)
            if winner:
                print("~~Congratulations~~ ", player_name1,"win!")
                exit()
        if whos_turn==False:
            winner=check_win(create_new_board,symbleplayer2)
            if winner:
                print("~~Congratulations~~ ", player_name2,"win!")
                exit()
        if whos_turn:
            whos_turn=False
        elif whos_turn==False:
            whos_turn=True
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
        
    
            


    