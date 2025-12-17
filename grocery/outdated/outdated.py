def main():
    Dict ={
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    Calnum = {
        "1": "01",
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        "6": "06",
        "7": "07",
        "8": "08",
        "9": "09",
        "10": "10",
        "11": "11",
        "12": "12"
    }
    while True:
        x = input("Date: ")
        x = x.strip()
        try:
            if("/" in x):
                x = x.split("/")
                if(int(x[0]) < 13 and int(x[1]) < 32):
                    if (x[0] in Calnum):
                        print(x[2]+"-"+Calnum[x[0]]+"-"+Calnum[x[1]])
                        break
                    else:
                        print(x[2]+"-"+x[0]+"-"+Calnum[x[1]])
                        break
        except:
            pass
        try:
            if(", " in x):
                x = x.split(" ")
                x[1] = x[1].replace(",","")
                print(x[2]+"-"+Dict[x[0]]+"-"+Calnum[x[1]])
                break
        except:
            pass


main()