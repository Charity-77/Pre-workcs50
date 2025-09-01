def main():
    answer = input("File name: ")
    answer = answer.strip().lower()
    if answer[-4:] == ".gif":
        print("image/gif")
    elif answer[-4:] == ".jpg" or answer[-5:] ==".jpeg" :
        print("image/jpeg")
    elif answer[-4:] == ".png":
        print("image/png")
    elif answer[-4:] == ".pdf":
        print("application/pdf")
    elif answer[-4:] == ".txt":
        print("text/plain")
    elif answer[-4:] == ".zip":
        print("application/zip")
    else :
        print("application/octet-stream")
main()



