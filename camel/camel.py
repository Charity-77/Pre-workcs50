#before
def main():
    result = ""
    camelCase = input("camelCase: ")
    for char in camelCase:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result +=char
    print(result)
main()
