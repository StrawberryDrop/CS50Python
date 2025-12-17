def main():
    x = input()
    print(convert(x))

def convert(word):
    word = word.replace(":)","🙂")
    word = word.replace(":(","🙁")
    return word

main()