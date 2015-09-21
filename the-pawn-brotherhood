'''
Chess is a two-player strategy game played on a checkered game board laid out in eight rows 
(called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. 
Each square of the chessboard is identified by a unique coordinate pair
— a letter and a number (ex, "a1", "h8", "d6"). 
For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece 
on a square diagonally in front of it on an adjacent file, by moving to that square. 
For white pawns the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. 
With this strategy, one pawn defends the others. 
A pawn is safe if another pawn can capture a unit on that square. 
We have several white pawns on the chess board and only white pawns. 
You should design your code to find how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

For a game AI one of the important tasks is the ability to estimate game state. 
This concept will show how you can do this on the simple chess figures positions.
'''

def board():
    ''' Creates chess board. Used to identify
    location of a pawn based on coordinate (x, y) '''
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rank = ['1', '2', '3', '4', '5', '6', '7', '8']
    return [[''.join([col, row]) for row in rank]
                            for col in file]
​
def safe_pawns(pawns):
    safe = 0
    brd = board()
    #Two for loops, to identify and append pawn locations.
    pawn_locations = [(rank.index(pawn), file) for pawn in pawns 
                    for file, rank in enumerate(brd) if pawn in rank]
    #Determines whether or not potential defenses exist within list of locations.
    for pawn in pawn_locations:
        if (pawn[0]-1, pawn[1]+1) in pawn_locations or \
        (pawn[0]-1, pawn[1]-1) in pawn_locations:
            safe += 1
    return safe

