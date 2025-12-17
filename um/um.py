import re
import sys


def main():
    print(count(input("Input: ")))


def count(s):
    tot = 0
    k = s.split(" ")
    for st in k :
        matches = re.search(r"^(um|um,|um\.+|um\?)$",st, flags = re.IGNORECASE)
        if matches:
            tot = tot +1
    return tot

if __name__ == "__main__":
    main()