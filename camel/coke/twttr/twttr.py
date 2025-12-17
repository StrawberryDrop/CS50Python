#def main():
#    x = input("Input: ")
#    r = ""
#    for i in  range(len(x)):
#        if("A" != x[i] and "E" != x[i] and "O" != x[i] and "U" != x[i] and "I"!= x[i] and "a" != x[i] and "e" != x[i] and "o" != x[i] and "u" != x[i] and "i" != x[i] ):
#            r += x[i]
#    print("Output: "+r)
#main()

def main():
    x = input("Input: ")
    z = shorten(x)
    print("Output: "+z)

def shorten(word):
    k = ""
    for i in  range(len(word)):
        if("A" != word[i] and "E" != word[i] and "O" != word[i] and "U" != word[i] and "I"!= word[i] and "a" != word[i] and "e" != word[i] and "o" != word[i] and "u" != word[i] and "i" != word[i] ):
            k += word[i]
    return k

5
if __name__ == "__main__":
    main()