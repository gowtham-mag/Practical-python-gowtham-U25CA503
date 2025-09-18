
N = int(input("enter the number of elements:"))
even_count = 0
odd_count = 0

print("enter the numbers:")
for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Numbers of odd numbers: {odd_count}")
