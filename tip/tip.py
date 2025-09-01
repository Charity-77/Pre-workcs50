m = input("How much is your meal?")
p = input("What percentage would you like to tip?")
m = float(m.strip("$"))
p = float(p.strip("%"))
p = p/100
tip = m*p
tip =round(tip,2)
print(f"Leave ${tip:.2f}")

