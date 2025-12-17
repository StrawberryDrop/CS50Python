def main():
    x = input("camealCase: " )
    scase = snake_case(x)
    print(scase)

def snake_case(word):
    newword=""
    for i in range(len(word)):
        if(word[i].isupper()):
            newword += "_"+(word[i].lower())
        else:
            newword +=word[i]
    return newword




main()