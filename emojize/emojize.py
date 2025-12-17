import emoji

def main():
    x = input("Input: ")
    if("_" in x):
        print(emoji.emojize("Output: "+x))
    else:
        print(emoji.emojize("Output: "+x, language = 'alias'))


main()