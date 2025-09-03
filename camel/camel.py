#define a function that will input a camelCase , the outpu an underscodre before the capiital letter
def main():
    result = "" #define an empty variable
    camelCase = input("camelCase: ") 
    for char in camelCase: # calling out characters in the input.It fetches all the characters
        if char.isupper(): # if the character(letter) is in capital letter
            result += "_" + char.lower() # reassign the variable by underscore before the uppercase letter to then lower the letter
        else:
            result +=char # otherwise assign the lower variable 
    print(result)
main()
