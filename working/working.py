import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if times:= re.search(r"^(((\d\d?:\d\d)|\d\d?) (AM|PM) to ((\d\d?:\d\d)|\d\d?) (AM|PM))$",s):
                be = times[2]+ times[4]
                #print(be)
                if "AM" in be:
                    k = re.search(r"(.+)AM",be)
                    z = k[1].strip()
                    z = z.split(":")
                    #print(z)
                    a = z[0]
                    if (int(a) > 12):
                        raise Exception(ValueError)
                    elif (int(a) == 12):
                        a = "00"
                    elif (int(a) < 10):
                        a = "0"+a
                    if len(z) < 2 :
                        z.append( ":00")
                    else:
                        if  int( z[1]  ) >= 60:
                             raise Exception(ValueError)
                        z[1] = ":"+z[1]
                    p = a+z[1]
                elif "PM" in be:
                    k = re.search(r"(.+)PM",be)
                    z = k[1].strip()
                    z = z.split(":")
                    #print(z)
                    a = z[0]
                    a = str(int(a) + 12)
                    if (int(a) > 24):
                        raise Exception(ValueError)
                    elif (int(a) == 24):
                        a = "12"
                    if  len(z) < 2 :
                        z.append( ":00")
                    else:
                        if int(z[1]) >= 60:
                            raise Exception(ValueError)
                        z[1] = ":"+z[1]
                    p = a+z[1]
                else:
                     raise Exception(ValueError)

                be = times[5] + times[7]
                if "AM" in be:
                    k = re.search(r"(.+)AM",be)
                    z = k[1].strip()
                    z = z.split(":")
                    #print(z)
                    a = z[0]
                    if (int(a) > 12):
                        raise Exception(ValueError)
                    elif (int(a) == 12):
                        a = "00"
                    elif (int(a) < 10):
                        a = "0"+a
                    if len(z) < 2 :
                        z.append( ":00")
                    else:
                        if int(z[1]) >= 60:
                             raise Exception(ValueError)
                        z[1] = ":"+z[1]
                    r = a+z[1]
                elif "PM" in be:
                    k = re.search(r"(.+)PM",be)
                    z = k[1].strip()
                    z = z.split(":")
                    #print(z)
                    a = z[0]
                    a = str(int(a) + 12)
                    if (int(a) > 24):
                        raise Exception(ValueError)
                    elif (int(a) == 24):
                        a = "12"
                    if  len(z) < 2 :
                        z.append( ":00")
                    else:
                        if (int(z[1])) >= 60:
                             raise Exception(ValueError)
                        z[1] = ":"+z[1]
                    r = a+z[1]
                else:
                    raise Exception(ValueError)
                return p + " to "+ r

    else:
        raise Exception(ValueError)












if __name__ == "__main__":
    main()