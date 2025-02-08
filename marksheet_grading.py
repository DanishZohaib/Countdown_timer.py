# Marksheet and grading formula

obtained_marks = int(input("Enter your Obtained Marks: "))
total_marks_input = input("Enter Total 500 Marks: ")
if total_marks_input=="":
    total_marks=500
else:
    total_marks=int(total_marks_input)
percentage=(obtained_marks/total_marks)*100
print(f"{percentage:.1f}%")
if percentage >=90:
    print("Grade A+")
elif percentage >=80:
    print("Grade A")
elif percentage >=70:
    print("Grade B")
elif percentage >=60:
    print("Grade C")
elif percentage >=50:
    print("Grade D")
elif percentage >=40:
    print("Grade E")
else:
    print("Fail")