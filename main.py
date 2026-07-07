from menu import show_nain_menu
from game import  play_single_player_game
def main():
    choose=show_nain_menu()
    if choose:
        play_single_player_game()   
main()