# Dic Rollong game
import random
total_score = 0

while True:
    c = input("Roll the dice? (y/n): ")
    choice = c.lower()
    if choice == 'y':
        dic1 = random.randint(1,6)
        dic2 = random.randint(1,6)
        role_score = dic1 + dic2
        total_score += role_score
        print(f"{dic1}, {dic2}\nYour current score is {role_score}\nYour total score is {total_score}")
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid Choice")