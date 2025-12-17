def main():
    z = input("Fraction: ")
    print( gauge(convert(z ) ) )


def convert(fraction):
    while True:
        try:
                frac = fraction.split("/")
                x = int(frac[0])
                y = int(frac[1])
                #if y == 0:
                #    raise Exception(ZeroDivisionError)
                k = int((float(x) / float(y))*100)
                if(k > 100):
                    raise Exception(ValueError)
                else:
                    return k
        except ValueError:
                raise Exception(ValueError)


def gauge(percentage):
        if percentage >= 99:
            return "F"
        elif percentage <=1:
            return "E"
        else:
           return f"{percentage:.0f}%"




if __name__ == "__main__":
    main()