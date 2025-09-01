#def a function that shows the amount, and the amount inserted ,then the change
#amount due 50, insert 5,10 or 25 only,then return amount due = origionalamount -insert
#
#otherwise return the  original amount
def main():
    amount_due = "50"
    amount_due = int(amount_due)
    insert = int(input("Insert coin: "))

    while amount_due > 0:
        print("Amount Due:", amount_due)
        insert = int(input("Insert coin: "))


        # only accept 5, 10, or 25
        if insert in [5, 10, 25]:
            amount_due -= insert

    # once amount_due <= 0, exit loop
    if amount_due < 0:
        amount_due = amount_due*(-1)
        print("Change Owed:", amount_due)
    else:
        print("Change Owed: 0")

main()
