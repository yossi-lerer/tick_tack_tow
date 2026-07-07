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