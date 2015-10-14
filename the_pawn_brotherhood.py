'''
From the Checkio task page:
"For a game AI one of the important tasks is the ability to estimate game state. 
This concept will show how you can do this on the simple chess figures positions."

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

More info at https://www.checkio.org/mission/pawn-brotherhood/
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

