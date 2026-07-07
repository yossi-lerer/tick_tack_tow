
def show_nain_menu():
    while True:
        user_choose=input("  \n### tic tack tow ###\n\nDeveloped by Elyashiv Cohen, Chaim Doitch, Yossi Lerer, Aarye Naori\n\n* Menu *\n1). Play\n2). Exit\nEnter your choose: ")
        if user_choose=="2":
            exit()
            
        elif user_choose=="1":
            return True
        
        print("\ninvalid nemu, try agein!")