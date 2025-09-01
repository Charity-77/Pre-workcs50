# define function
def main():
    #input the variable
    answer = input("Greeting: ")
    answer = answer.strip().lower()
    # if outputs start with Hello, print$0
    if answer == "hello" or answer == "hello, newman":
        print("$0")
    elif answer[0] == "h":
        print("$20")
    else:
        print("$100")
main()







