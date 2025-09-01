# define input
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    answer = answer.lower()
    answer = answer.strip()
    answer = answer.replace("-","")
    answer = answer.replace(" ","")
    if answer == "42" or answer == "fortytwo":
        print("Yes")
    else:
        print("No")
main()
