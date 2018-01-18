import sys

markers = [ 'X', 'O' ]

def create_board():
    return [ None ] * 9

def is_full(board):
    return all(board)

def print_board(board):
    for i in range(0, 9):
        print '%s' % board[i] if board[i] else ' ',
        if (i+1) % 3 == 0:
            print

def make_move(marker, board, index):
    if index < 1 or index > 9:
        print "Index out of range, plase choose a number between 1 and 9"
        return False
    
    been_played = [ i for i in range(0,9) if board[i] ]
    if index-1 in been_played:
        print "Board position already played, please retry"
        return False

    board[index-1] = marker
    return True

def check_game(board, marker):
    '''
    Check whether the player with given marker wins or
    if the game is a tie.
    '''
    
    have_marker = set([ i for i in range(0,9) if board[i] == marker ])
    # print have_marker
    
    win, tie = False, False
    # print { 0, 1, 2 } <= have_marker
    # print { 3, 4, 5} <= have_marker
    # print { 6, 7, 8 } <= have_marker
    # print { 0, 3, 6 } <= have_marker
    # print { 1, 4, 7 } <= have_marker
    # print { 2, 5, 8 } <= have_marker
    # print { 1, 4, 7 } <= have_marker
    # print { 2, 4, 6 } <= have_marker
    
    if { 0, 1, 2 } <= have_marker or { 3, 4, 5} <= have_marker or { 6, 7, 8 } <= have_marker or \
       { 0, 3, 6 } <= have_marker or { 1, 4, 7 } <= have_marker or { 2, 5, 8 } <= have_marker or \
       { 1, 4, 7 } <= have_marker or { 2, 4, 6 } <= have_marker:
        win = True

    if not win and is_full(board):
        tie = True

    return (win, tie)

if __name__ == '__main__':
    print 'Game begins'
    print 'Player 1 is "X", 2 is "O"'
    
    board = create_board()
    game_status = [False, False, False] # (x wins, o wins, tie)
    player = 0
    
    while not is_full(board) and not any(game_status):
        if player == 0:
            marker = 'X'
        else:
            marker = 'O'

        index = int(raw_input('Player %d turn: ' % (player+1)))
        while not make_move(marker, board, index):
            index = int(raw_input('Player %d turn: ' % (player+1)))
        
        print_board(board)

        win, tie = check_game(board, marker)
        game_status[player] = win
        game_status[2] = tie
        # print game_status
        
        if player == 0: player = 1
        else: player = 0
    
    status = [ i for i, x in enumerate(game_status) if x ]
    if len(status) > 1:
        print "Something went wrong: seems there's a win and tie at the same time"
    else:
        if status[0] == 2:
            print "Result is a tie"
        else:
            print "Player %d wins" % (status[0]+1)


