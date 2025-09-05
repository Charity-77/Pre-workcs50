#define a function that when it meets aeiou, it lowers it and replaces it with ""
def main():
     result = "" # creating an empty vvarable
     Input = input("Input: ")#Input any word
     for ch in Input:# for any character or letter in input
         #if the lowered character is equal to one of the vowels
        if (ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u' ):
            #remove it
            result += ""
            #else add the character
        else:
            result += ch
     print("Output:",result)
main()


