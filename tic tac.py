import math

board = [' 'for _ in range(9)]
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|' + '|' .join(row) + '|')

def winner(b,player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combos:
        if all(b[i] == player for i in combo):
            return True
    return False

def is_full():
    return ' ' not in board

def minimax (b,depth,is_maximizing):
    if winner(b, '0'):
        return 1
    if winner(b, 'x'):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i]==' ':
                b[i]='0'
                score=minimax(b,depth + 1,False)
                b[i]=' '
                best_score = max(score,best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b,depth + 1,True)
                b[i] = ' '
                best_score =min(score,best_score)
        return best_score

def ai_move():
        best_score = -math.inf
        move = None
        for i in range(9):
            if board[i]==' ':
                board[i]='0'
                score = minimax(board,0,False)
                board[i]= ' '
                if score > best_score:
                    best_score = score
                    move = i
        board[move] = '0'

def player_move():
    while True:
        try:
            move = int(input("Enter your move(1-9):")) -1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is already taken.")
        except(ValueError, IndexError):
            print("Invalid input.Choose a number between 1 and 9.")

def play_game():
    print("Your are X,AI is o.")
    print_board()

    while True:
        player_move()
        print_board()
        if winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move()
        print_board()
        if winner(board, '0'):
            print("AI wins! Better luck next time.")
            break
        if is_full():
            print("It's a draw!")
            break

play_game()



