def main():
    x = input("Filename: ")
    if(".gif" in x.lower()):
        print("image/gif")
    elif(".jpg" in x or ".jpeg" in x.lower()):
        print("image/jpeg")
    elif(".png" in x.lower()):
        print("image/png")
    elif(".pdf" in x.lower()):
        print("application/pdf")
    elif(".txt" in x.lower()):
        print("text/plain")
    elif(".zip" in x.lower()):
        print("application/zip")
    else:
        print("application/octet-stream")

main()