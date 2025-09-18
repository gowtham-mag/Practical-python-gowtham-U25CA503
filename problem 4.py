import  math

print("choose the shape to calculate area:")
print(". rectangle")
print(". square")
print(". cricle")
print(". triangle")

choice = int(input("enter your choice (1-4): "))

if choice == 1:
    lenght = float(input("enter lenght of rectangle: "))
    breadth = float(input("enter breadth of rectangle: "))
    area = lenght * breadth
    print(f"area of rectangle = {area}")
elif choice == 2:
    side = float(input("enter side of square : "))
    area = side * side
    print(f"area of square = {area}")
elif choice == 3:
    radius = float(input("enter radius of cricle: "))
    area = math.pi * radius * radius
    print(f"area of cricle = {area:.2f}")
elif choice == 4:
    base = float(input("enter base of triangle : "))
    height = float(input("enter height of triangle : "))
    area = 0.5 *base * height
    print(f"area of triangle = {area}")
else:
    print("invalid choice")

