#def a function that shows the amount, and the amount inserted ,then the change
#amount due 50, insert 5,10 or 25 only,then return amount due = origionalamount -insert
#
#otherwise return the  original amount
def main():
    amount_due = 50  # Coke costs 50 cents

    while amount_due > 0:
        print("Amount Due:", amount_due)
        insert = int(input("Insert coin: "))

        # only accept 5, 10, or 25
        if insert in [5, 10, 25]:
            amount_due -= insert
        else:
            # Ignore invalid coins, don’t reduce amount_due
            continue

    # once amount_due <= 0, loop ends
    if amount_due < 0:
        print("Change Owed:", abs(amount_due))
    else:
        print("Change Owed: 0")


main()

