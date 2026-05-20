"""In a game of Go two players take turns to place black and white stones on
a game board. The winner is the player who manages to encircle a bigger area
on the board with their own game pieces.

Please write a function named who_won(game_board: list),
 which takes a two-dimensional array as its argument.

 The array consists of integer values, which represent the following situations:

0: empty square
1: player 1 game piece
2: player 2 game piece

The scoring rules of Go can be quite complex,
but in this exercise it is enough to compare the number of pieces each player has
on the game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won,
and the value 2 if player 2 won. If both players have the same number of pieces
on the board, the function should return the value 0."""


# Write your solution here
def who_won(game_board: list):
    player1_pieces = 0
    player2_pieces = 0

    for row in game_board:
        for square in row:
            if square == 0:
                continue  # I used to put break here but then it wouldn't work
            elif square == 1:
                player1_pieces += 1
            else:
                player2_pieces += 1

    if player1_pieces == player2_pieces:
        return 0
    elif player1_pieces > player2_pieces:
        return 1
    else:
        return 2


"""
# Suggested Solution

def who_won(game_board: list):
    points1 = 0
    points2 = 0
 
    for row in game_board:
        for square in row:
            if square == 1:
                points1 += 1
            elif square == 2:
                points2 += 1
    
    if points1 > points2:
        return 1
    elif points2 > points1:
        return 2
    else:
        return 0

#Review
My solution returns the same output, I do however check for 0 altough I see why it's not
necessary and thus skipped by the suggested solution. 
"""
