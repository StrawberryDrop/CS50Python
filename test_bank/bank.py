def main():
    x = input("Greeting: ")
    z = value(x)
    print(z)


def value(greeting):
    if("Hello" in greeting):
        return 0
    elif ("H" in greeting):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()