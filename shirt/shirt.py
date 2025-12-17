import sys
import PIL
from PIL import Image

def main():
    count = 0
    if(len(sys.argv) < 3 ):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 3 ):
        sys.exit("Too many command-line arguments")
    elif(sys.argv[1].find('.')== -1):
        sys.exit("Invalid input")
    else:
        a = sys.argv[1].split(".")
        b = sys.argv[2].split(".")
        if(a[1] != 'jpeg' and a[1] != 'jpg' and a[1] != 'png'):
            sys.exit("Invalid input")
        elif(b[1] != 'jpeg' and b[1] != 'jpg' and b[1] != 'png'):
            sys.exit("Invalid output")
        elif(a[1] != b[1]):
            sys.exit("Input and output have different extensions")
        else:
            try:
                person = PIL.Image.open(sys.argv[1])
                shirt = PIL.Image.open("shirt.png")
                size = shirt.size
                person = PIL.ImageOps.fit(person, size)
                person.paste(shirt, mask = shirt)
                person.save(sys.argv[2])
            except:
                sys.exit()


main()
