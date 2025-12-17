def main():
    grocery = {}
    while True:
        try:
            x = input()
            if(x.upper() in grocery):
                grocery[x.upper()] += 1
            elif x == "":
                break
            else:
                grocery[x.upper()] = 1
        except EOFError:
            break
    for i in sorted(grocery):
        print(grocery[i],i)

main()
