# Temperature converter:fahrenheit to celsius

print("1: fahrenheit to celsius")
print("2:celsius to fahrenheit")
choice = int(input("enter your choice (1 or 2):"))

if choice == 1:
     f = float(input("enter temperture in fahrenheit: "))
     c = (f - 32) * 5 / 9
     print(f"{f}F is {c:.2f} C.")
elif choice ==2:
     f = float(input("enter temperture in celsius: "))
     c = (c * 9 / 5) + 32
     print(f"{c})C is {f:.2f} F.")
else:
     print("invalid choice.")
     
