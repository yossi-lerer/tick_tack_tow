def create_board():
    row=3 
    col=3 
    list_of_borad=[["*" for _ in range(col)] for _ in range(row)]
    return list_of_borad
def print_board(board):
     row=len(board)
     col=row
     for row1 in range(row):
        for col1 in range(col):
            print(board[row1][col1] ,end= "")
        print("")
        
    
def place_symbol(board,row,col,symbol):
    board[row][col] = symbol
    
