def is_position_inside_board(board , row, col):
    real_size_of_board_row_and_col=len(board)
    if row<real_size_of_board_row_and_col and row>-1 and col<real_size_of_board_row_and_col and col>-1==True:
        return True   
    print("its not in borad")
    return False
def is_empty(board, row, col):
    if board[row][col]=="*":
        return True
    print("the position is taken try another")
    return False 
def is_vaild_move(board,row,col):
    first_chek=is_position_inside_board(board,row,col)
    if first_chek == False:
        return False
    secend_chek=is_empty(board,row,col)
    if(first_chek and secend_chek is True):
        return True
    return False

def vaild_move_input(lst_num):
    if len(lst_num) != 2:
        return False
    try:
        int(lst_num[0])
        int(lst_num[1])
    except:
        return False