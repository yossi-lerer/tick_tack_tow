def check_diagonal_win(board,symbal):
    lens_of_board=len(board)
    right_diagonal_its_folwing = True
    left_diagonal_its_folwing = True
    secend_lens_of_borad=len(board)-1
    for index in range(lens_of_board):
        if board[index][index]!=symbal:
            right_diagonal_its_folwing = False
        if board[index][secend_lens_of_borad]!=symbal:
            left_diagonal_its_folwing = False
        secend_lens_of_borad=secend_lens_of_borad-1
    if left_diagonal_its_folwing or right_diagonal_its_folwing:
        return True
    return False

def check_column_win(board, symbol: str) -> bool:
    check = [0, 0, 0]
    for row in board:
        for index in range(len(check)):
          if row[index] == symbol:
                check[index] += 1
    for col in check:
        if col == 3:
            return True
    return False

def check_win(board, symbol: str) -> bool:
    if check_column_win(board, symbol) or check_row_win(board, symbol) or check_diagonal_win(board, symbol):
        return True
    else:
        return False
    
print(check_win([["o","o" ,"o"],["o","x","x"],["x","o","o"]], "x"))
        

