def chek_diagonal_win(board,symbal):
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
print(chek_diagonal_win([["o","o" ,"o"],["o","x","x"],["x","o","o"]], "x"))
    

        

