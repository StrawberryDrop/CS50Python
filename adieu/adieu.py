import sys

def main():
    names = []
    t = True
    while t:
        try:
            x = input()
            names.append(x)
        except EOFError :
            t = False
    print("Adieu, adieu, to",end ="")
    if(len(names) == 2):
        print(" "+names[0]+ " and "+names[1])
        sys.exit()
    for name in names:
        if(name == names[len(names)-1] ):
            if(len(names)-1 == 0):
                print(" "+name)
            else:
                print(" and "+name)
        else:
            print(" "+name+",",end ="")


main()
