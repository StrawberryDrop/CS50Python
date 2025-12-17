import requests
import sys
import json

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
         return False



try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument ")
    elif (sys.argv[1]).isnumeric() or isfloat(sys.argv[1]):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(json.dumps(response.json(), indent=2))
        o= response.json()
        z = o["bpi"]
        g = z["USD"]
        t = g["rate"]
        k = float(t.replace(",",""))
        t = (k*float(sys.argv[1]))
        txt = "${:,.4f}"
        print(txt.format(t))
    else:
        sys.exit("Command-line argument is not a number")







except requests.RequestException:
    sys.exit()