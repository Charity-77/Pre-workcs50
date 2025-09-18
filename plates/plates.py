#input ER. if is_valid(ER),char...
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    meadian = len(s)//2

    if  not s[:2].isalpha() :
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if  not s.isalnum() :
        return False
    if s[:meadian].isnumeric()== True:
        return False
    first_digit = False
    for char in s:
        if char.isdigit():
            first_digit = True
            if char == "0":
                return False
            else:
                pass
        else:
            if first_digit:
                return False
            

    return True


main()








