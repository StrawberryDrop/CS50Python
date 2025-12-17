def main():
    x = input("What time is it? ")
    tot =convert(x)
    if(7 <= tot <=8):
        print("breakfast time")
    if(12<=tot<=13 or ("p.m." in x and (12<=tot<=13 or tot == 1))):
        print("lunch time")
    if(18<=tot<=19 or ("p.m." in x and 6<=tot<=7)):
        print("dinner time")


def convert(time):
    y = time.split(":")
    hr = float(y[0])
    min =float(y[1]) / 60
    return hr+min


if __name__ == "__main__":
    main()