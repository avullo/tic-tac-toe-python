import sys, random

def create_board():
    return [ None ] * 9

def is_full(board):
    return all(board)

def print_board(board):
    for i in range(0, 9):
        print '%s' % board[i] if board[i] else ' ',
        if (i+1) % 3 == 0:
            print

def choose_first():
    if random.randint(0,1) == 0:
        return 0
    else:
        return 1
    
def assign_markers(player):
    marker = ''
    while marker not in ('X', 'O'):
        marker = raw_input('Player %d. Please choose your marker ("X", "O"): ' % (player+1))

    if marker == 'X':
        other_marker = 'O'
    else:
        other_marker = 'X'
        
    markers = [None] * 2
    markers[player] = marker

    if player == 0:
        other_player = 1
    else:
        other_player = 0

    markers[other_player] = other_marker
    return markers

def repeat_game():
    return raw_input("Do you want to play again? (Yes/No): ").lower().startswith("y")

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

def player_input(player, marker):
    index = int(raw_input('Player %d. Choose a board position (1-9): ' % (player+1)))
    while not make_move(marker, board, index):
        index = int(raw_input('Player %d. Choose a VALID board position: ' % (player+1)))
    
def check_game(board, marker):
    '''
    Check whether the player with given marker wins or
    if the game is a tie.
    '''
    
    have_marker = set([ i for i in range(0,9) if board[i] == marker ])
    win, tie = False, False
    
    if { 0, 1, 2 } <= have_marker or { 3, 4, 5} <= have_marker or { 6, 7, 8 } <= have_marker or \
       { 0, 3, 6 } <= have_marker or { 1, 4, 7 } <= have_marker or { 2, 5, 8 } <= have_marker or \
       { 0, 4, 8 } <= have_marker or { 2, 4, 6 } <= have_marker:
        win = True

    if not win and is_full(board):
        tie = True

    return (win, tie)

if __name__ == '__main__':
    print '***************************'
    print '* Welcome to Tic Tac Toe! *'
    print '***************************'
    print 
    print 'This is a two players game.' 
    print 'Please choose who is Player 1 and 2 among the two.'
    
    player = choose_first()
    markers = assign_markers(player)

    game_on = True
    while game_on:
        print
        print 'Game begins'
        print 'Player %d is first (%s)' % (player+1, markers[player])
    
        board = create_board()
        game_status = [False]*3 # (1 wins, 2 wins, tie)
    
        while not is_full(board) and not any(game_status):
            marker = markers[player]

            player_input(player, marker)
            print_board(board)

            win, tie = check_game(board, marker)
            game_status[player] = win
            game_status[2] = tie
        
            if player == 0: player = 1
            else: player = 0
    
        status = [ i for i, x in enumerate(game_status) if x ]
        if len(status) > 1:
            print "Something went wrong: seems there's a win and tie at the same time"
            sys.exit()
        else:
            if status[0] == 2:
                print "Result is a tie"
            else:
                print "Player %d. You won!" % (status[0]+1)
                print 
            game_on = repeat_game()

    print "Bye."
