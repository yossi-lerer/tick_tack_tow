def is_position_inside_board(board , row, col):
    real_size_of_board_row_and_col=len(board)
    return row<real_size_of_board_row_and_col and row>-1 and col<real_size_of_board_row_and_col and col>-1
def is_empty(board, row, col):
    if board[row][col]=="*":
        return True
    return False
def is_vaild_move(board,row,col):
    first_chek=is_position_inside_board(board,row,col)
    if first_chek == False:
        return False
    secend_chek=is_empty(board,row,col)
    if(first_chek and secend_chek is True):
        return True
    return False


    