import sys
import csv

def main():
    if(len(sys.argv) < 3 ):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 3 ):
        sys.exit("Too many command-line arguments")
    elif(sys.argv[1].find('.')== -1):
        sys.exit("Not a CSV file")
    else:
        a = sys.argv[1].split(".")
        b = sys.argv[2].split(".")
        if(a[1] != 'csv' or b[1] != 'csv' ):
                sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1]  ) as file:
                        k = csv.reader(file)
                        try:
                            with open(sys.argv[2],"w") as file:
                                for line in k:
                                        writer= csv.DictWriter(file, fieldnames=["first", "last","house"])
                                        if (line[0] == "name" ):
                                            last = "last"
                                            first = "first"
                                        else:
                                            print(line[0])
                                            last, first = line[0].strip().split(",")
                                            last = last.strip()
                                            first = first.strip()
                                        writer.writerow({"first": first, "last": last, "house":line[1]})
                        except:
                            sys.exit("Could not read "+sys.argv[2])
            except:
                sys.exit("Could not read "+sys.argv[1])





main()

