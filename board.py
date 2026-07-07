def create_board():
    row=3 #שורה
    col=3 # עמודה
    list_of_borad=[["*" for _ in range(col)] for _ in range(row)]
    return list_of_borad
def print_board(board):
     row=len(board)
     col=row
     for i in range(row):
        print("")
        for j in range(col):
            print(board[i][j] ,end= "")

