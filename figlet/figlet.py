import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if (len(sys.argv) == 2 or sys.argv[2] not in figlet.getFonts() or  ((sys.argv[1] != "-f") & (sys.argv[1] != "--f"))):
        sys.exit("Invalid usage")
    x = input("Input: ")
    if(len(sys.argv) < 2 ):
        y = random.choice(figlet.getFonts())
        figlet.setFont(font=y)
        print(figlet.renderText((x)))
    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText((x)))


main()