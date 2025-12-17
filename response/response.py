import validators

def main():
    address = input("What's your email address? ")
    x = valid(address)
    if x:
        print("Valid")
    else:
        print("Invalid")

def valid(email):
    return validators.email(email)



if __name__ == "__main__":
    main()