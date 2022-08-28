# Python_Intro
# Problem Set 4
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Guessing Game" problem
"""
import random

while True:
    try:
        level = int(input("Level: "))
        if level >0:
            break
    except:
        pass

random_number = random.randint(1, level)

while True:
    try:
        guess = int(input("guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass
