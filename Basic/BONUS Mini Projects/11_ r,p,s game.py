#  rock paper scissor game
import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = tuple(emojis.keys())

def user_choce():
    user_choce = input("Chose:- Rock, paper, or scissors? (r/p/s): ")
    user_choce.lower()
    if user_choce in user_choce:
        return user_choce
    else:
        return

def show_choise(computer_chose, user_chose):
    print(f"You chose: {emojis[user_chose]}")
    print(f"Computer chose: {emojis[computer_chose]}")

def show_winner(computer_chose, user_chose):
    if (user_chose == computer_chose):
        print("Tie!")
    elif((user_chose == ROCK and computer_chose == SCISSORS) or (user_chose == SCISSORS == computer_chose == PAPER) or (user_chose == PAPER and computer_chose == ROCK)):
        print("Congras, You Win! 🥳")
    else:
        print("You Lose 😓")

def main():
    while True:
        user_chose = user_choce()
        computer_chose = random.choice(choices)
        
        show_choise(computer_chose, user_chose)
        show_winner(computer_chose, user_chose)
        
        want_continue = input('Continue? (y/n): ').lower()
        if want_continue == 'n':
            break

main()