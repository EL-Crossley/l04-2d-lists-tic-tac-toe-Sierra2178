# Put your function here
def ticTacToe(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    else:
        return "TIE"

# testing
board = [['X','O','O'],['O','X','O'],['X','O','X']]
print(ticTacToe(board))
