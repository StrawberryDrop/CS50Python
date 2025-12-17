def main():
    while True:
        try:
            z = input("Fraction: ")
            frac = z.split("/")
            x = int(frac[0])
            y = int(frac[1])
        except ValueError or ZeroDivisionError:
            pass
        else:
            if x > y:
                pass
            else:
                amount = (float(x) / float(y))*100
                if amount >= 99:
                    print("F")
                    break
                elif amount <= 1:
                    print("E")
                    break
                else:
                     print(f"{amount:.0f}%")
                     break

main()



