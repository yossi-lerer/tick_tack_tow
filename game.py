def play_single_player_game():
    pass

def ask_move() -> tuple[int, int]:
    move = input("please enter two number for your next move first num for row and secend num for column. for exemple 1.2 ")
    move = move.split(".")
    move[0] = int(move[0])
    move[1] = int(move[1])
    return move[0], move[1]
print(ask_move())