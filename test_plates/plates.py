def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if ("." in s or " " in s or "?" in s or "," in s or ":" in s or ";" in s or "-" in s or "!" in s or "\"" in s or "[" in s or "]" in s or "{" in s or "}" in s or "(" in s or ")" in s):
        return False
    elif ( len(s)< 2 or len(s) > 6):
        return False
    elif (s[0].isnumeric()  or s[1].isnumeric() ):
        return False
    else:
        K = True
        p = False
        for i in range(len(s)) :
            if (s[i].isnumeric()):
                p = True
                if(K == True and int(s[i]) == 0):
                    return False
                else:
                    K = False
            else:
                if(p == True):
                    return False

        return True


if __name__ == "__main__":
    main()