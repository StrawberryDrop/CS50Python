def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if x.lower() =="forty-two" or x.lower() =="forty two" or x.replace(" ","") == "42" :
        print("Yes")
    else:
        print("No")

main()