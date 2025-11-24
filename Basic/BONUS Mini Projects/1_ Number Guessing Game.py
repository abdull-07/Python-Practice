# Number Guessing Game
import random

print("Welcome to the Number Guessing Game!.")
gen_num=random.randint(1,100)
user_guess=int(input("Guess a number between 1 and 100: "))
if user_guess==gen_num:
    print("Congratulations! You guessed the correct number: ",gen_num)
elif user_guess<gen_num:
    print(":ow! the correct number was: ", gen_num)
else:
    print("HIgh! the correct number is:", gen_num)