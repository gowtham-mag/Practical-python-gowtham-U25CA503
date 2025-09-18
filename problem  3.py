# program to calculate total marks, percentage and grade of a student

# INPUT MARKS FOR FIVE SUBJECTS

print("ENTER MARKS FOR FIVE SUBJECTS (OUT OF 100):")
S1 = float(input("Pyton: "))
S2 = float(input("Maths: "))
S3 = float(input("English: "))
S4 = float(input("Tamil: "))
S5 = float(input("Excel: "))

#calculate total and percentage
total = S1+S2+S3+S4+S5

percentage = (total /500) * 100

# determine grade based on percentage
if  percentage >=80:
    grade ='A'
elif percentage >=70:
    grade = 'B'
elif percentage >=60:
    grade = 'C'
elif percentage >=40:
    grade = 'D'
else:
    grade = 'E'



# output the results
print(f"\ntotal marks: {total}  / 500")
print(f"percentage: {percentage:.2f}%")
print(f"grade: {grade}")
