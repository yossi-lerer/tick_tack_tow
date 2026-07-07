def check_column_win(board, symbol: str) -> bool:
    check = [0, 0, 0]
    for row in board:
        for index in range(3):
          if row[index] == symbol:
                check[index] += 1
    for col in check:
        if col == 3:
            return True
    return False