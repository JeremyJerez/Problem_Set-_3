# Python_Intro
# Problem Set 4
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Bitcoin Price Index" problem
"""
import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    result = r.json()
    bit = result["bpi"]["USD"]["rate_float"]
    amount = bit * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit(1)
