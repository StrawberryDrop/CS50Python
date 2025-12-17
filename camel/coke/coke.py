def main():
    x = 50
    while(x > 0):
        print("Amount Due:",x)
        z = int (input("Insert Coin: "))
        if (z==25 or z==5 or z== 10):
            x -= z
    print("Changed Owed:",(0-x))

main()
