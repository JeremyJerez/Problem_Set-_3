# Python_Intro
# Problem Set 4
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Frank, Ian and Glen’s Letters" problem
"""
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    xFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1]== "--font"):
    xFont = False
else:
    print("Invalid usage")#sys.exit to exit program
    sys.exit(1)

if xFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)

text = input("Input: ")

print(f"output: {figlet.renderText(text)}")
