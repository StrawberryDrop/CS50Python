import sys
import csv
from tabulate import tabulate

def main():
    lines = []
    title = []
    if(len(sys.argv) < 2 ):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 2 ):
        sys.exit("Too many command-line arguments")
    elif(sys.argv[1].find('.')== -1):
        sys.exit("Not a CSV file")
    else:
        a = sys.argv[1].split(".")
        if(a[1] != 'csv' ):
                sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1]) as file:
                        k = csv.reader(file)
                        for line in k:
                            if("Small"== line[1]):
                                title.append( line[0])
                                title.append(line[1])
                                title.append(line[2])
                            else:
                                lines.append([ line[0],  line[1], line[2]])
                print(tabulate( lines,title, tablefmt = "grid"))

            except:
                sys.exit("File does not exist")




main()