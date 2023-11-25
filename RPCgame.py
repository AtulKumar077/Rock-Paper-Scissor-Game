import random

user_score = 0
computer_score = 0

def play():
    global user_score, computer_score
    while True:
        user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to Quit\n")
        if user == 'q':
            break
        computer = random.choice(['r', 'p', 's'])
        print(f"Computer's choice: {computer}")

        if user == computer:
            print('It\'s a tie')

        if is_win(user, computer):
            user_score += 1
            print('You won!')
        else:
            computer_score += 1
            print('You lost!')

    print(f"Final User Score: {user_score}, Final Computer Score: {computer_score}")

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

play()
