def ask_player_name():
    player_1=input("enter your name: ")
    return player_1

def show_turn_message(player_name,simbol):
     print(f"{player_name}: it is your turn. Your symbol is {simbol} ")

show_turn_message(ask_player_name(),"x")

