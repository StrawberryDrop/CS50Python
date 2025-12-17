import random
import sys

def main():
    while True:
        level = input("Level: ")
        if(level.isnumeric() and int(level) > 0):
            break
    ran = random.randint(1,int(level))
    while True:
        while True:
            guess = input("Guess: ")
            if(guess.isnumeric() and int(guess) > 0):
                break
        if(int(guess) < ran):
             print("Too small!")
        elif(int(guess) > ran):
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

main()