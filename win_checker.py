# [["*","*","*"]
# ,["*","*","*"]
# ,["*","*","*"]]
def check_column_win(board, symbol: str) -> bool:
    check = [0, 0, 0]
    for i in board:
        if i[0] == symbol:
            check[0] += 1
        if i[1] == symbol:
            check[1] += 1
        if i[2] == symbol:
            check[2] += 1
            
    print(check)


check_column_win([["x","x","3"],["x","x","*"],["x","*","x"]], "x")