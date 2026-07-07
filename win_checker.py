def check_row_win(board,symbol):

    for row in board:
        check=True
        for num in range(len(row)):
            if row[num] !=symbol:
                   check=False
                   break
        if check is True: 
            return check
    return check            


