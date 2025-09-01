#define a function that will result in the answer of the calculation
def calc():
    x, op, y = input("Expression: ").split()
    x = int(x)
    y = int(y)

    if op == "+":
        print(f"{x + y:.1f}")
    elif op == "-":
        print(f"{x - y:.1f}")
    elif op == "*":
        print(f"{x * y:.1f}")
    elif op == "/":
        print(f"{x / y:.1f}")
calc()


