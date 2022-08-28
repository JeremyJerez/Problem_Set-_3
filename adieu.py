# Python_Intro
# Problem Set 4
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Adieu, Adieu" problem
"""
import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break
output = p.join(names)
print("Adieu, adieu, to ", output)
