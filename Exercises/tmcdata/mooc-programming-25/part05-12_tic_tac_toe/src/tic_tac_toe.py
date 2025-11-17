"""
Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting
noughts and crosses. If either player succeeds in placing three of their own
symbols on any row, column or diagonal, they win. If neither player manages this,
it is a draw.

Please write a function named play_turn(game_board: list, x: int, y: int, piece: str)
, which places the given symbol at the given coordinates on the board.
The values of the coordinates on the board are between 0 and 2.

NB: when compared to the sudoku exercises, the arguments the function takes are
the other way around here. The column x comes first, and the row y second.

The board consists of the following strings:

"": empty square
"X": player 1 symbol
"O": player 2 symbol

The function should return True if the square was empty and the symbol was
successfully placed on the game board. The function should return False if
the square was occupied, or if the coordinates weren't valid.

An example execution of the function:

game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))
print(game_board)

Sample output
True
[['', '', 'X'], ['', '', ''], ['', '', '']]
"""


# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(0, 3) or y not in range(0, 3):
        return False
    if game_board[y][x] == "":  # Parameters are reversed where row is y and column is x
        game_board[y][x] = piece
        return True
    else:
        return False
    return False


if __name__ == "__main__":
    game_board = [["", "", ""], ["0", "0", "0"], ["", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)


"""
# Suggested Solution

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
 
    # Note, that y-coordinate is given first
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
 
    return False

#Review
My solution gives the same result. Structurally, the suggested one simplifies 
the coordinate validation by using direct comparisons instead of range(), 
making it a bit clearer and slightly faster.
"""
