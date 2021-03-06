import random

board = []

for x in range(5):
    board.append(['O']*5)

def print_board(board):
    for row in board:
        print ' '.join(row)

print "Let's play Battleship!"

print_board(board)

def random_row(board):
    return random.randint(0, len(board)-1)
    
            
def random_col(board):
    return random.randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

#print ship_row
#print ship_col
max_guesses = 25
for turn in range(max_guesses):
    guess_row = input('Guess Row:')
    guess_col = input('Guess Col:')

    if guess_row == ship_row and guess_col == ship_col:
        print 'You sunk my Battleship!'

    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops that's not even in the ocean!"

        elif (board[guess_row][guess_col]== 'X'):
            print 'You hit that spot already!'

        else:
            print 'You miss my Battleship!'
            board[guess_row][guess_col]= 'X'
            if turn == (max_guesses - 1):
                print 'Game Over!'

        print 'This is your', turn + 1, '-nth guesses left'

        print_board(board)
