import sys

from os.path import exists
lines= []

def main():
    count = 0
    if(len(sys.argv) < 2 ):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 2 ):
        sys.exit("Too many command-line arguments")
    elif(sys.argv[1].find('.')== -1):
        sys.exit("Not a Python file")
    else:
        a = sys.argv[1].split(".")
        if(a[1] != 'py' ):
                sys.exit("Not a Python file")
        else:
            if(exists(sys.argv[1])):
                with open(sys.argv[1]) as file:
                    for line in file:
                        lines.append(line.rstrip())
                for ln in lines:
                    ln = str(ln)
                    ln = ln.strip()
                    if  (str(ln)).startswith("#") :
                        count = count
                    elif(ln == ""):
                        count = count
                    else:
                        count = count +1
                print(count)
            else:
                sys.exit("File does not exist")













main()


