def main():
    k = input("Expression: ")
    r = k.split(" ")
    x = float(r[0])
    y = r[1]
    z = float(r[2])
    if("+" in y.lower()):
        print(f"{ x+z:.1f}")
    if("-" in y.lower()):
        print(f"{ x-z:.1f}")
    if("*" in y.lower()):
        print(f"{ x*z:.1f}")
    if("/" in y.lower()):
     print(f"{ x/z:.1f}")

main()