import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches:= re.search(r"<iframe(.+)></iframe>",s):
        l = matches[1]
        #print(l)

        if ur:= re.search(r"src=\"(.+)\"",l):
                ur = ur[1].split(" ")
                url = ""
                for r in ur:
                    if "youtube.com" in r:
                        url = r
                if "youtube" in url:
                    #print(url)
                    url = url.replace("embed/","")
                    url=url.replace("youtube","youtu.be")
                    url=url.replace(".com","")
                    url=url.replace("www.","")
                    if "https" not in url:
                        return url.replace("http","https")
                    else:
                        return url
                else:
                   return "None"
    else:
        return "None"

    return "None"






if __name__ == "__main__":
    main()