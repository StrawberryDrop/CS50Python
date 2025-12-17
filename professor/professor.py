import random


def main():
    l = get_level()
    score = 10
    for i in range(9):
        attempt = 0
        x = generate_integer(l)
        y = generate_integer(l)
        while True:
            if(attempt == 3):
                print(str(x)+" + "+str(y)+" = "+str(x+y))
                break
            z = input(str(x)+" + "+str(y)+" = ")
            if(z.isnumeric()):
                z = int(z)
                if(z == x+y):
                    break
                else:
                    print("EEE")
                    attempt += 1
            else:
                print("EEE")
                attempt += 1
        if(attempt > 0):
            score -= 1
    print("Score: "+str(score))

def get_level():
    while True:
        le = input("Level: ")
        if(le.isnumeric()):
            le = int(le)
            if(le == 1 or le == 2 or le == 3):
                return le
                break



def generate_integer(level):
    if (level == 1):
        return random.randint(0,9)
    elif(level == 2):
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()